from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict

from src.estimation.state import State

@dataclass
class FilterParams(ABC):
    """Base dataclass for all filter parameters."""
    algorithm_type: str

class Filter(ABC):
    def __init__(self, params: FilterParams):
        self.params = params
        self.state: State = None

    @abstractmethod
    def update(self, state: State, measurement: Dict) -> State:
        raise NotImplementedError
    
    def get_state(self) -> State:
        return self.state