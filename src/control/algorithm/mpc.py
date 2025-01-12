from dataclasses import dataclass
import numpy as np

from src.control.algorithm.base import BaseController, BaseControllerParams
from src.utils import load_dataclass_from_dict

@dataclass
class MPCParams(BaseControllerParams):
    control_type: str = "mpc"
    Q: np.ndarray  # Quadratic cost matrix for the state variables
    R: np.ndarray  # Quadratic cost matrix for the control variables

class MPCParamsBuilder(ParamsBuilder):
    def build(self, config: Dict[str, Any]) -> MPCParams:
        return load_dataclass_from_dict(
            dataclass=MPCParams,
            data_dict=config,
            convert_list_to_array=True
        )


class MPC(BaseController):
    def __init__(self, params: MPCParams):
        self.params = params