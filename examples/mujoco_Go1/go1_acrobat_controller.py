from enum import Enum, auto
from typing import Any, Dict

import jax
import numpy as np
from mujoco import mjx
from mujoco_playground._src import mjx_env

from examples.mujoco_Go1.ppo import PPO, PPOParams, PPOParamsBuilder
from src.control.algorithm.base import Controller
from src.control.controller_factory import ControllerFactory


class Go1ControllerType(Enum):
    """Available controller types."""

    JOYSTICK = auto()
    HANDSTAND = auto()
    FOOTSTAND = auto()


class PPOJoystick2HandstandAdapter(Controller):
    """
    PPO controller trained in Joystick env with necessary state and action adaptations to Handstand env
    In Joystick env:
        motor_targets = state.data.qpos[7:] + action * 0.5
    In Handstand env:
        motor_targets = stata.data.ctrl + action * 0.3

    This controller performs the necessary adaptations in .control() to the state and action
    """

    def __init__(self, controller: Controller, src_env_config: Any, tar_env_config: Any):
        self._controller = controller
        self._src_env_action_scale = src_env_config.action_scale
        self._tar_env_action_scale = tar_env_config.action_scale

    def control(self, state: mjx_env.State, command: np.ndarray, data: mjx.Data) -> np.ndarray:
        """Control with state and action space adaptation."""
        # Adapt state for joystick control
        state = jax.numpy.concat([state, command])

        # Get control action
        action: np.ndarray = self._controller.control(state)

        # Adapt action space
        action = (self._tar_env_action_scale * action - data.ctrl + data.qpos[7:]) / self._src_env_action_scale

        return action


class Go1ControllerManager:
    """Manages multiple controllers and handles transitions between them."""

    def __init__(self, controllers: Dict[Go1ControllerType, Controller]):
        self._controllers = controllers
        self._active_type = Go1ControllerType.FOOTSTAND  # default controller
        self._command = jax.numpy.zeros(3)  # joystick command (vel_x, vel_y, vel_yaw)

    def set_command(self, command: jax.Array | np.ndarray):
        """Set the current command for joystick controller."""
        if command.shape != np.empty((3,)).shape:
            raise ValueError(f"Invalid command shape {command.shape}. Expected (3,)")
        self._command = command

    def switch_controller(self, controller_type: Go1ControllerType):
        """Switch to a different controller type."""
        if controller_type not in self._controllers:
            raise ValueError(f"No controller registered for type {controller_type}")
        self._active_type = controller_type

    def control(self, state: mjx_env.State) -> np.ndarray:
        """Get control action from current active controller."""
        controller = self._controllers[self._active_type]

        if self._active_type == Go1ControllerType.JOYSTICK:
            # Joystick controller requires command input
            return controller.control(state.obs["state"], self._command, state.data)

        # Other controllers use standard control
        return controller.control(state.obs["state"])


def create_go1_acrobat_controller_manager(
    factory: ControllerFactory,
    controller_configs: Dict[Go1ControllerType, Dict[str, Any]],
    joystick_env_config: Any,
    handstand_env_config: Any,
) -> Go1ControllerManager:
    """
    Create a configured Go1ControllerManager.

    NOTE:
    given the use case for the acrobatic controller being quite flexible
    It feels more confortable to have the creation of controller manager
    defined in a funciton instead of from a config file
    """

    controllers = {}

    # Create each controller
    factory.register_controller(PPOParams, PPO)
    params_builder = PPOParamsBuilder()
    for controller_type, config in controller_configs.items():
        params = params_builder.build(config=config)
        base_controller = factory.build(params=params)

        # Wrap joystick controller with adaptation, leave others as is
        # since joystick env has different observation space as well as action scaling/offset
        # see PPOJoystick2HandstandAdapter for more details
        if controller_type == Go1ControllerType.JOYSTICK:
            controllers[controller_type] = PPOJoystick2HandstandAdapter(
                controller=base_controller, src_env_config=joystick_env_config, tar_env_config=handstand_env_config
            )
        else:
            controllers[controller_type] = base_controller

    return Go1ControllerManager(controllers)
