"""Payoff functions for evolutionary game interactions."""

from __future__ import annotations

import numpy as np

from .agent import Strategy
from .config import PayoffMatrix
from .strategies import actions_cooperate


def payoff_from_actions(
    self_cooperates: np.ndarray,
    opponent_cooperates: np.ndarray,
    matrix: PayoffMatrix,
) -> np.ndarray:
    """Vectorised payoff for a two-action game."""

    self_cooperates = np.asarray(self_cooperates, dtype=bool)
    opponent_cooperates = np.asarray(opponent_cooperates, dtype=bool)

    payoff = np.empty(self_cooperates.shape, dtype=np.float32)
    payoff[self_cooperates & opponent_cooperates] = matrix.R
    payoff[self_cooperates & ~opponent_cooperates] = matrix.S
    payoff[~self_cooperates & opponent_cooperates] = matrix.T
    payoff[~self_cooperates & ~opponent_cooperates] = matrix.P
    return payoff


def pair_payoff(
    self_strategy: int,
    opponent_strategy: int,
    matrix: PayoffMatrix | None = None,
) -> float:
    """Scalar payoff helper used by tests and documentation examples.

    Placeholder strategies are interpreted deterministically here:
    tit-for-tat cooperates and random is treated as cooperate. The vectorised
    simulator samples random actions per interaction.
    """

    matrix = matrix or PayoffMatrix()
    self_coop = int(self_strategy) in (Strategy.COOPERATE, Strategy.TIT_FOR_TAT, Strategy.RANDOM)
    opponent_coop = int(opponent_strategy) in (
        Strategy.COOPERATE,
        Strategy.TIT_FOR_TAT,
        Strategy.RANDOM,
    )
    return float(payoff_from_actions(np.array([self_coop]), np.array([opponent_coop]), matrix)[0])


def vector_payoff(
    self_strategies: np.ndarray,
    opponent_strategies: np.ndarray,
    matrix: PayoffMatrix,
    rng: np.random.Generator,
) -> np.ndarray:
    """Vectorised payoff between two equally shaped strategy arrays."""

    self_actions = actions_cooperate(self_strategies, rng)
    opponent_actions = actions_cooperate(opponent_strategies, rng)
    return payoff_from_actions(self_actions, opponent_actions, matrix)

