"""
This demo script is modified from the locomotion tutorial of mujoco_playground
https://github.com/google-deepmind/mujoco_playground
"""

import jax
import mediapy
import mujoco
from tqdm import tqdm

from examples.mujoco_Go1Handstand.env_wrapper import Go1HandstandEnv
from examples.mujoco_Go1Handstand.ppo import PPO, PPOParams, PPOParamsBuilder
from src.control.controller_factory import ControllerFactory


def main():
    # Instantiate simulator
    rng = jax.random.PRNGKey(12345)
    env = Go1HandstandEnv()
    jit_reset = jax.jit(env.reset)
    jit_step = jax.jit(env.step)
    state = jit_reset(rng)

    # Instantiate controller
    factory = ControllerFactory()
    factory.register_controller(PPOParams, PPO)
    ppo_params = PPOParamsBuilder().build()
    controller = factory.build(params=ppo_params)

    # start closed-loop simulation
    rollout = []
    actions = []
    for i in tqdm(range(env.env_cfg.episode_length)):
        ctrl = controller.control(state.obs["state"])  # do not use privileged_state
        state = jit_step(state, ctrl)

        # record result
        actions.append(ctrl)
        rollout.append(state)

    # visualize simulation result
    render_every = 2
    fps = 1.0 / env.dt / render_every
    traj = rollout[::render_every]

    scene_option = mujoco.MjvOption()
    scene_option.geomgroup[2] = True
    scene_option.geomgroup[3] = False
    scene_option.flags[mujoco.mjtVisFlag.mjVIS_CONTACTPOINT] = True
    scene_option.flags[mujoco.mjtVisFlag.mjVIS_CONTACTFORCE] = False
    scene_option.flags[mujoco.mjtVisFlag.mjVIS_TRANSPARENT] = False

    frames = env.render(traj, camera="side", scene_option=scene_option, height=480, width=640)
    mediapy.show_video(frames, fps=fps, loop=False)


if __name__ == "__main__":
    main()
