"""Random number helpers."""

from __future__ import annotations

import numpy as np


def create_rng(seed: int | None) -> np.random.Generator:
    """Create the simulator RNG."""

    return np.random.default_rng(seed)


def mutation_mask(
    shape: tuple[int, int],
    probability: float,
    rng: np.random.Generator,
) -> np.ndarray:
    """Return a boolean mask selecting mutated cells."""

    if probability <= 0.0:
        return np.zeros(shape, dtype=bool)
    if probability >= 1.0:
        return np.ones(shape, dtype=bool)
    return rng.random(shape) < probability

