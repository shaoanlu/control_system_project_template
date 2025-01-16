from dataclasses import KW_ONLY, dataclass, field
from typing import Any, Dict

import numpy as np

from src.control.algorithm.base import Controller, ControllerParams, ControllerParamsBuilder
from src.utils import load_dataclass_from_dict


@dataclass
class MPCParams(ControllerParams):
    _: KW_ONLY  # Make all following fields keyword-only
    Q: np.ndarray  # Diagonal elements of the quadratic cost matrix for the state variables
    R: np.ndarray  # Diagonal elements of the quadratic cost matrix for the control variables
    algorithm_type: str = field(default="mpc")


class MPCParamsBuilder(ControllerParamsBuilder):
    def build(self, config: Dict[str, Any]) -> MPCParams:
        return load_dataclass_from_dict(dataclass=MPCParams, data_dict=config, convert_list_to_array=True)


class MPC(Controller):
    def __init__(self, params: MPCParams):
        self.params = params

    def control(self, state: np.ndarray, **kwargs) -> np.ndarray:
        pass
