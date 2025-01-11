import numpy as np
from typing import Dict, Any, Tuple

class BaseEnvironment:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self._init()

    def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, Dict]:
        raise NotImplementedError