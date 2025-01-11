class BasePlanner:
    def __init__(self, config):
        self.config = config

    def plan(self, env, start, goal):
        raise NotImplementedError
