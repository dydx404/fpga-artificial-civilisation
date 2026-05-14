import numpy as np

from civsim.agent import Strategy
from civsim.metrics import cooperation_ratio, strategy_distribution, strategy_entropy


def test_strategy_distribution_counts_known_strategies() -> None:
    strategies = np.array(
        [
            [Strategy.COOPERATE, Strategy.DEFECT],
            [Strategy.TIT_FOR_TAT, Strategy.RANDOM],
        ],
        dtype=np.uint8,
    )

    distribution = strategy_distribution(strategies)

    assert distribution["cooperate"] == 1
    assert distribution["defect"] == 1
    assert distribution["tit_for_tat"] == 1
    assert distribution["random"] == 1


def test_cooperation_ratio_counts_cooperate_and_tit_for_tat() -> None:
    strategies = np.array(
        [
            [Strategy.COOPERATE, Strategy.DEFECT],
            [Strategy.TIT_FOR_TAT, Strategy.DEFECT],
        ],
        dtype=np.uint8,
    )

    assert cooperation_ratio(strategies) == 0.5


def test_strategy_entropy_is_zero_for_uniform_world() -> None:
    strategies = np.full((4, 4), Strategy.COOPERATE, dtype=np.uint8)

    assert strategy_entropy(strategies) == 0.0

