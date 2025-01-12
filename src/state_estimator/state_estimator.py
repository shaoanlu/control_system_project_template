from dataclasses import dataclass
import numpy as np
from typing import Dict, List, Tuple

from src.state_estimator.filter.base import Filter, State


@dataclass
class State:
    position: np.ndarray  # 3D position
    orientation: np.ndarray  # quaternion
    velocity: np.ndarray  # 6D spatial velocity
    covariance: np.ndarray  # State covariance matrix

class StateEstimator:
    """
    Example usage:
        estimator = StateEstimator()
        estimator.add_filter('imu', ComplementaryFilter(cf_params))
        estimator.add_filter('joint', KalmanFilter(kf_params))
        estimator.add_filter('joint', ParticleFilter(pf_params))
        ...
        state = estimator.update({...})
    """
    def __init__(self):
        self.filters: List[Tuple[str, Filter]] = []
        self.state = State()
    
    def add_filter(self, sensor_type: str, filter: Filter):
        self.filters.append((sensor_type, filter))
    
    def update(self, measurements: Dict):
        for sensor_type, filter in self.filters:
            if sensor_type in measurements:
                self.state = filter.update(self.state, measurements[sensor_type])
        return self.state
