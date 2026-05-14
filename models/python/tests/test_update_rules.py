import numpy as np

from civsim.agent import Strategy
from civsim.config import PayoffMatrix, SimulationConfig
from civsim.update_rules import compute_payoffs
from civsim.world import World


def test_all_cooperators_receive_eight_rewards_with_wraparound() -> None:
    config = SimulationConfig(
        width=3,
        height=3,
        seed=1,
        mutation_probability=0.0,
        payoff_matrix=PayoffMatrix(R=3, S=0, T=5, P=1),
    )
    strategies = np.full((3, 3), Strategy.COOPERATE, dtype=np.uint8)
    world = World.from_strategy_array(strategies, config)

    payoff = compute_payoffs(world.strategy, config, world.rng)

    np.testing.assert_array_equal(payoff, np.full((3, 3), 24, dtype=np.float32))


def test_single_defector_invades_small_periodic_world() -> None:
    config = SimulationConfig(
        width=3,
        height=3,
        seed=1,
        mutation_probability=0.0,
        payoff_matrix=PayoffMatrix(R=3, S=0, T=5, P=1),
    )
    strategies = np.full((3, 3), Strategy.COOPERATE, dtype=np.uint8)
    strategies[1, 1] = Strategy.DEFECT
    world = World.from_strategy_array(strategies, config)

    world.step()

    assert np.all(world.strategy == Strategy.DEFECT)
    assert world.generation == 1
    assert np.all(world.age == 1)


def test_mutation_probability_one_changes_world_to_valid_strategies() -> None:
    config = SimulationConfig(width=8, height=8, seed=3, mutation_probability=1.0)
    world = World.random(config)

    world.step()

    assert world.strategy.shape == (8, 8)
    assert world.strategy.min() >= 0
    assert world.strategy.max() < config.strategy_count

