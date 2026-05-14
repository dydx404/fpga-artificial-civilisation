"""Strategy action helpers.

The MVP hardware path may initially support only cooperate and defect. The
Python model includes tit-for-tat and random placeholders so the team can
experiment before committing extra state to RTL.
"""

from __future__ import annotations

import numpy as np

from .agent import Strategy


def actions_cooperate(strategies: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Return a boolean array where True means the agent cooperates.

    Current placeholder semantics:
    - cooperate: cooperate
    - defect: defect
    - tit-for-tat: cooperate until memory is added
    - random: cooperate with probability 0.5 per interaction
    """

    strategies = np.asarray(strategies)
    cooperative = (strategies == Strategy.COOPERATE) | (
        strategies == Strategy.TIT_FOR_TAT
    )
    random_mask = strategies == Strategy.RANDOM
    if np.any(random_mask):
        random_actions = rng.random(strategies.shape) < 0.5
        cooperative = cooperative | (random_mask & random_actions)
    return cooperative

