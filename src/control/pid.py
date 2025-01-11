from dataclasses import dataclass

from src.control.base import BaseController, BaseControllerParams


@dataclass
class PIDParams(BaseControllerParams):
    control_type: str = "pid"
    kp: float  # Proportional gain
    ki: float  # Integral gain
    kd: float  # Derivative gain

class PID(BaseController):
    def __init__(self, params: PIDParams):
        self.kp = params.kp
        self.ki = params.ki
        self.kd = params.kd

        self.integral = 0.0
        self.prev_error = None

    def control(self, error: float, dt: float) -> float:
        if not (self.prev_error):
            self.prev_error = error
        error_diff = (error - self.prev_error) / dt
        self.prev_error = error
        self.integral += error * dt

        return self.params.kp * error + self.params.ki * self.integral + self.kd * error_diff