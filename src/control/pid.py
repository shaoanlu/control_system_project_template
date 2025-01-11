from dataclasses import dataclass

from src.control.base import BaseController


@dataclass
class PIDParams:
    control_type: str = "pid"
    kp: float  # Proportional gain
    ki: float  # Integral gain
    kd: float  # Derivative gain

class PID(BaseController):
    def __init__(self, params: PIDParams):
        pass

    def control(self, error: float) -> float:
        pass