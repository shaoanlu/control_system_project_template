from dataclasses import dataclass
import numpy as np

from src import control

@dataclass
class MPCParams:
    control_type: str = "mpc"
    Q: np.ndarray  # Quadratic cost matrix for the state variables
    R: np.ndarray  # Quadratic cost matrix for the control variables


class MPC(control.BaseController):
    def __init__(self, config: MPCParams):
        self.config = config