from dataclasses import KW_ONLY, dataclass, field
from typing import Dict

import numpy as np


@dataclass
class State:
    """
    Reference:
        - https://github.com/google/brax/blob/main/brax/base.py
    """

    _: KW_ONLY
    x: np.ndarray  # the state, e.g. position
    xd: np.ndarray  # the time-derivative of the state, e.g. velocity
    info: Dict = field(default_factory={})  # Additional information (e.g. timestamp, prediction of the state, etc.)
