from functools import partial

import jax
import numpy as np
from mujoco_playground import registry
from mujoco_playground._src import mjx_env

from src.environment.base import Env


class Go1HandstandEnv(Env):
    def __init__(self):
        env_name = "Go1Handstand"
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
