import numpy as np
from mujoco_playground import registry
from mujoco_playground._src import mjx_env

from src.environment.base import Env


class Go1HandstandEnv(Env):
    def __init__(self):
        env_name = "Go1Handstand"
        self.env_cfg = registry.get_default_config(env_name)
        self.env = registry.load(env_name, config=self.env_cfg)

    def step(self, state: mjx_env.State, action: np.ndarray) -> np.ndarray:
        return self.env.step(state, action)
