from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Protocol

from src.estimation.state import State


@dataclass
class FilterParams(ABC):
    """Base dataclass for all filter parameters."""

    algorithm_type: str


class FilterParamsBuilder(ABC):
    """Abstract base class for parameter builders."""

    @abstractmethod
    def build(self, config: Dict[str, Any]) -> FilterParams:
        pass


class Filter(Protocol):
    def __init__(self, params: FilterParams):
        self.params = params
        self.state: State = None

    @abstractmethod
    def process(self, **kwargs) -> Any: ...

    @abstractmethod
    def update(self, state: State, measurement: Dict, **kwargs) -> State:
        raise NotImplementedError

    @property
    def is_initialized(self) -> bool:
        return self._state is not None
