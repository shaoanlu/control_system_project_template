from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict
import numpy as np


@dataclass
class State:
    position: np.ndarray  # 3D position
    orientation: np.ndarray  # quaternion
    velocity: np.ndarray  # 6D spatial velocity
    covariance: np.ndarray  # State covariance matrix

class Filter(ABC):
    @abstractmethod
    def update(self, state: State, measurement: Dict) -> None:
        pass
    
    def get_state(self) -> State:
        return self.state