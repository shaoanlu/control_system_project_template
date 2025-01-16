from dataclasses import dataclass
from typing import Dict

import numpy as np

from src.estimation.algorithm.base import Filter, FilterParams
from src.estimation.state import State


@dataclass
class KalmanFilterParams(FilterParams):
    process_noise: np.ndarray
    measurement_noise: np.ndarray


class KalmanFilter(Filter):
    def __init__(self, params: FilterParams):
        super().__init__(params)
        self.Q = params.process_noise
        self.R = params.measurement_noise

    def update(self, state: State, measurement: Dict) -> State:
        # Kalman filter implementation
        predicted_state = self._predict(state)
        updated_state = self._update(predicted_state, measurement)
        self.state = updated_state
        return self.state

    def _predict(self, state: State) -> State:
        # Predict state
        return state

    def _update(self, state: State, measurement: Dict) -> State:
        # Update state
        return state

    def get_state(self) -> State:
        return self.state
