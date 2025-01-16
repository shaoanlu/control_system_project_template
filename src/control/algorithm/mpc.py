from dataclasses import dataclass, field, KW_ONLY
import numpy as np
from typing import Any, Dict

from src.control.algorithm.base import BaseController, BaseControllerParams, BaseParamsBuilder
from src.utils import load_dataclass_from_dict

@dataclass
class MPCParams(BaseControllerParams):
    _: KW_ONLY  # Make all following fields keyword-only
    Q: np.ndarray  # Diagonal elements of the quadratic cost matrix for the state variables
    R: np.ndarray  # Diagonal elements of the quadratic cost matrix for the control variables
    algorithm_type: str = field(default="mpc")

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

    def control(self, state: np.ndarray, **kwargs) -> np.ndarray:
        pass