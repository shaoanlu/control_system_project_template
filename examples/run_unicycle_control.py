from src.control.controller_factory import ConfigFactory, ControllerFactory
from src.environment.unicycle import Unicycle
from src.utils import load_yaml


PATH_CONTROLLER_CONFIG = "src/config/mpc_unicycle.yaml"


def run_simulation():
    # Initialize environment
    env = Unicycle()

    # Build controller
    control_yaml = load_yaml(PATH_CONTROLLER_CONFIG)
    control_config = ConfigFactory(control_yaml).build()
    controller = ControllerFactory().build(control_config)

    # Run simulation
    for _ in range(100):
        action = controller.control(env.state)
        next_state, reward, done, _ = env.step(action)
        controller.update(next_state, reward, done)
        if done:
            env.reset()


if __name__ == "__main__":
    run_simulation()
