from src.env.base import BaseEnv


class UnicycleEnv(BaseEnv):
    def __init__(self, config):
        self.config = config

    def step(self, action):
        pass

    def reset(self):
        pass
