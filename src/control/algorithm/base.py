from abc import ABC, abstractmethod
from dataclasses import dataclass
import numpy as np
from typing import Any, Dict, Union

from src.control.algorithm.mpc import MPCParams
from src.control.algorithm.pid import PIDParams

@dataclass
class BaseControllerParams(ABC):
    """Base dataclass for all controller parameters."""
    control_type: str

class BaseParamsBuilder(ABC):
    """Abstract base class for parameter builders."""
    @abstractmethod
    def build(self, config: Dict[str, Any]) -> BaseControllerParams:
        pass

class BaseController(ABC):
    def __init__(self, config=Union[MPCParams, PIDParams], **kwargs):
        pass
    
    @abstractmethod
    def control(self, state: np.ndarray, **kwargs) -> np.ndarray:
        raise NotImplementedError
    
    def reset(self, **kwargs):
        return self.init_control_params
