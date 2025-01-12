from dataclasses import dataclass
import numpy as np
from typing import Any, Dict

from src.control.algorithm.base import BaseController, BaseControllerParams, BaseParamsBuilder
from src.utils import load_dataclass_from_dict

@dataclass
class MPCParams(BaseControllerParams):
    algorithm_type: str = "mpc"
    Q: np.ndarray  # Quadratic cost matrix for the state variables
    R: np.ndarray  # Quadratic cost matrix for the control variables

class MPCParamsBuilder(BaseParamsBuilder):
    def build(self, config: Dict[str, Any]) -> MPCParams:
        return load_dataclass_from_dict(
            dataclass=MPCParams,
            data_dict=config,
            convert_list_to_array=True
        )


class MPC(BaseController):
    def __init__(self, params: MPCParams):
        self.params = params