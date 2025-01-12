from typing import Dict, List, Tuple

from src.state_estimator.filter.base import Filter, State


class StateEstimator:
    """
    Example usage:
        estimator = StateEstimator()
        estimator.add_filter('imu', ComplementaryFilter(alpha=0.98))
        estimator.add_filter('joint', KalmanFilter(process_noise, measurement_noise))
        estimator.add_filter('joint', ParticleFilter(num_particles))
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
