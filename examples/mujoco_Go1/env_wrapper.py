from functools import partial

import jax
import numpy as np
from mujoco_playground import registry
from mujoco_playground._src import mjx_env

from src.environment.base import Env


class Go1Env(Env):
    go1_env_names = ["Go1Handstand", "Go1JoystickFlatTerrain"]

    def __init__(self, env_name: str):
        if env_name not in self.go1_env_names:
            raise ValueError(f"Unsupported Go1 environment {env_name}Supported environment are: {self.go1_env_names}")
        self.env_cfg = registry.get_default_config(env_name)
        self.env = registry.load(env_name, config=self.env_cfg)

    @partial(jax.jit, static_argnums=(0,))
    def step(self, state: mjx_env.State, action: np.ndarray) -> np.ndarray:
        return self.env.step(state, action)

    @partial(jax.jit, static_argnums=(0,))
    def reset(self, rng: jax.Array):
        return self.env.reset(rng)

    @property
    def render(self):
        return self.env.render

    @property
    def dt(self):
        return self.env.dt
