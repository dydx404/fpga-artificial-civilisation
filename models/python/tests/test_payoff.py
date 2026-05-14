import numpy as np

from civsim.agent import Strategy
from civsim.config import PayoffMatrix
from civsim.payoff import pair_payoff, payoff_from_actions


def test_prisoners_dilemma_truth_table() -> None:
    matrix = PayoffMatrix(R=3, S=0, T=5, P=1)

    assert pair_payoff(Strategy.COOPERATE, Strategy.COOPERATE, matrix) == 3
    assert pair_payoff(Strategy.COOPERATE, Strategy.DEFECT, matrix) == 0
    assert pair_payoff(Strategy.DEFECT, Strategy.COOPERATE, matrix) == 5
    assert pair_payoff(Strategy.DEFECT, Strategy.DEFECT, matrix) == 1


def test_vector_payoff_from_actions() -> None:
    matrix = PayoffMatrix(R=3, S=0, T=5, P=1)
    self_actions = np.array([True, True, False, False])
    opponent_actions = np.array([True, False, True, False])

    payoff = payoff_from_actions(self_actions, opponent_actions, matrix)

    np.testing.assert_array_equal(payoff, np.array([3, 0, 5, 1], dtype=np.float32))

