from dataclasses import dataclass, field

import numpy as np

from src.control.algorithm.base import Controller, ControllerParams


@dataclass(kw_only=True)  # Make all following fields keyword-only
class MPCParams(ControllerParams):
    Q: np.ndarray  # Diagonal elements of the quadratic cost matrix for the state variables
    R: np.ndarray  # Diagonal elements of the quadratic cost matrix for the control variables
    algorithm_type: str = field(default="mpc")


class MPC(Controller):
    def __init__(self, params: MPCParams):
        self.params = params

    def control(self, state: np.ndarray, **kwargs) -> np.ndarray:
        pass
