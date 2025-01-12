from abc import ABC, abstractmethod
import numpy as np
from typing import Dict, Any, Tuple

class BaseEnvironment(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self._init()

    @abstractmethod
    def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, Dict]:
        raise NotImplementedError