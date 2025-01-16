from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BasePlannerParams:
    """Base dataclass for all planner parameters."""

    planner_type: str


class BasePlanner(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def plan(self, env, start, goal):
        raise NotImplementedError
