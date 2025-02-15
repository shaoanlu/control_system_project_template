from dataclasses import dataclass, field

import numpy as np

from src.control.algorithm.base import Controller, ControllerParams


@dataclass(kw_only=True)  # Make all following fields keyword-only
class PIDParams(ControllerParams):
    kp: float  # Proportional gain
    ki: float  # Integral gain
    kd: float  # Derivative gain
    algorithm_type: str = field(default="pid")


class PID(Controller):
    def __init__(self, params: PIDParams):
        self.kp = params.kp
        self.ki = params.ki
        self.kd = params.kd

        self.integral = 0.0
        self.prev_error = None

    def control(self, state: np.ndarray, ref_state: np.array, error: float, dt: float) -> np.ndarray:
        if self.prev_error is None:
            self.prev_error = error
        error_diff = (error - self.prev_error) / dt
        self.prev_error = error
        self.integral += error * dt

        return np.array(self.kp * error + self.ki * self.integral + self.kd * error_diff)
