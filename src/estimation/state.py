from dataclasses import dataclass

import numpy as np


@dataclass
class State:
    position: np.ndarray  # 3D position
    orientation: np.ndarray  # quaternion
    velocity: np.ndarray  # 6D spatial velocity
    covariance: np.ndarray  # State covariance matrix
