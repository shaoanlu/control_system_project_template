"""
This demo script is modified from the locomotion tutorial of mujoco_playground
https://github.com/google-deepmind/mujoco_playground
"""

import mediapy
import mujoco

from examples.mujoco_Go1Handstand.env_wrapper import Go1HandstandEnv
from examples.mujoco_Go1Handstand.ppo import PPO, PPOParamsBuilder


def main():
    # initialize simulator
    env = Go1HandstandEnv()
    state = env.reset()

    # initialize controller
    ppo_params = PPOParamsBuilder().build()
    controller = PPO(params=ppo_params)

    # start closed-loop simulation
    rollout = []
    actions = []
    for i in range(env.env_cfg.episode_length // 2):
        ctrl = controller.control(state.obs)
        state = env.step(state, ctrl)

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
