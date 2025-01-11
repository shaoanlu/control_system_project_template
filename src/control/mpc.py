from dataclasses import dataclass
import numpy as np

from src.control.base import BaseController, BaseControllerParams

@dataclass
class MPCParams(BaseControllerParams):
    control_type: str = "mpc"
    Q: np.ndarray  # Quadratic cost matrix for the state variables
    R: np.ndarray  # Quadratic cost matrix for the control variables


class MPC(BaseController):
    def __init__(self, params: MPCParams):
        self.params = params