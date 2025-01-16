from dataclasses import dataclass
from typing import Dict

from src.estimation.algorithm.base import Filter, FilterParams
from src.estimation.state import State


@dataclass
class ParticleFilterParams(FilterParams):
    num_particles: int


class ParticleFilter(Filter):
    def __init__(self, params: FilterParams):
        super().__init__(params)
        self.num_particles = params.num_particles
        self.particles = None
        
    def update(self, state: State, measurement: Dict) -> State:
        # Particle filter implementation
        pass