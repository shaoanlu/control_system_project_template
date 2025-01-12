from typing import Dict
import numpy as np

from src.state_estimator.filter.base import Filter, State


class ParticleFilter(Filter):
    def __init__(self, num_particles: int):
        super().__init__()
        self.num_particles = num_particles
        self.particles = None
        
    def update(self, state: State, measurement: Dict) -> State:
        # Particle filter implementation
        pass