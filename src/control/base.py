from abc import ABC, abstractmethod
from dataclasses import dataclass
import numpy as np
from typing import Union

from src.control.mpc import MPCParams
from src.control.pid import PIDParams

@dataclass
class BaseControllerParams(ABC):
    """Base dataclass for all controller parameters."""
    control_type: str

class BaseController(ABC):
    def __init__(self, config=Union[MPCParams, PIDParams], **kwargs):
        pass
    
    @abstractmethod
    def control(self, state: np.ndarray, **kwargs) -> np.ndarray:
        raise NotImplementedError
    
    def reset(self, **kwargs):
        return self.init_control_params
