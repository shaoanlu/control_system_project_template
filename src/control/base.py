import numpy as np
from typing import Union

from src.control.mpc import MPCParams
from src.control.pid import PIDParams

class BaseController:
    def __init__(self, config=Union[MPCParams, PIDParams], **kwargs):
        pass

    def control(self, state: np.ndarray, **kwargs) -> np.ndarray:
        raise NotImplementedError
    
    def update_params(self, control_params):
        return control_params
    
    def reset(self, **kwargs):
        return self.init_control_params
