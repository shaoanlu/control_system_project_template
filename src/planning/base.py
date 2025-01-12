from abc import ABC, abstractmethod

class BasePlanner(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def plan(self, env, start, goal):
        raise NotImplementedError
