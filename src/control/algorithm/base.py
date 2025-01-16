from abc import ABC, abstractmethod
from dataclasses import dataclass, KW_ONLY
import numpy as np
from typing import Any, Dict

@dataclass
class BaseControllerParams(ABC):
    """Base dataclass for all controller parameters."""
    _: KW_ONLY  # Make all following fields keyword-only
    algorithm_type: str

class BaseParamsBuilder(ABC):
    """Abstract base class for parameter builders."""
    @abstractmethod
    def build(self, config: Dict[str, Any]) -> BaseControllerParams:
        pass

class BaseController(ABC):
    def __init__(self, config=BaseControllerParams, **kwargs):
        pass
    
    @abstractmethod
    def control(self, state: np.ndarray, **kwargs) -> np.ndarray:
        raise NotImplementedError
    
    def reset(self, **kwargs):
        return self.init_control_params
