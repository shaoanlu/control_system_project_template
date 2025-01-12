from typing import Dict

from src.state_estimator.filter.base import Filter, State


class ComplementaryFilter(Filter):
    def __init__(self, alpha: float):
        super().__init__()
        self.alpha = alpha
        
    def update(self, state: State, measurement: Dict) -> State:
        # Complementary filter implementation
        pass