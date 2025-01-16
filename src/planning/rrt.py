from dataclasses import dataclass
import numpy as np
from typing import Tuple

from src.planning.base import BasePlanner, BasePlannerParams


@dataclass
class RRTParams(BasePlannerParams):
    max_iter: int
    step_size: float
    goal_sample_rate: float
    start: Tuple[float, float]
    goal: Tuple[float, float]

class RRT(BasePlanner):
    def __init__(self, params: RRTParams):
        super().__init__(params)
        self.max_iter = params.max_iter
        self.step_size = params.step_size
        self.goal_sample_rate = params.goal_sample_rate
        self.start = params.start
        self.goal = params.goal

    def plan(self, start, goal):
        # RRT implementation
        pass