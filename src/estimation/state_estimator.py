from dataclasses import dataclass
import numpy as np
from typing import Dict, List, Tuple

from src.estimation.algorithm.base import Filter
from src.estimation.state import State



class StateEstimator:
    """
    Adopted the observer pattern to update the state based on multiple sensor measurements.

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
