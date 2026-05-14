"""World update rules for the reference model."""

from __future__ import annotations

import numpy as np

from .config import SimulationConfig
from .payoff import vector_payoff
from .rng import mutation_mask

MOORE_OFFSETS: tuple[tuple[int, int], ...] = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def shifted_neighbour(
    values: np.ndarray,
    dy: int,
    dx: int,
    wrap_edges: bool,
    fill_value: float | int,
) -> np.ndarray:
    """Return values from neighbour offset `(dy, dx)` for each cell."""

    if wrap_edges:
        return np.roll(np.roll(values, -dy, axis=0), -dx, axis=1)

    out = np.full(values.shape, fill_value, dtype=values.dtype)
    height, width = values.shape

    src_y0 = max(0, dy)
    src_y1 = height + min(0, dy)
    dst_y0 = max(0, -dy)
    dst_y1 = height - max(0, dy)

    src_x0 = max(0, dx)
    src_x1 = width + min(0, dx)
    dst_x0 = max(0, -dx)
    dst_x1 = width - max(0, dx)

    if src_y0 < src_y1 and src_x0 < src_x1:
        out[dst_y0:dst_y1, dst_x0:dst_x1] = values[src_y0:src_y1, src_x0:src_x1]
    return out


def compute_payoffs(
    strategies: np.ndarray,
    config: SimulationConfig,
    rng: np.random.Generator,
) -> np.ndarray:
    """Compute accumulated Moore-neighbourhood payoff for every cell."""

    payoff = np.zeros(strategies.shape, dtype=np.float32)
    valid_strategy_fill = 0

    for dy, dx in MOORE_OFFSETS:
        neighbour_strategies = shifted_neighbour(
            strategies,
            dy,
            dx,
            config.wrap_edges,
            fill_value=valid_strategy_fill,
        )
        interaction_payoff = vector_payoff(
            strategies,
            neighbour_strategies,
            config.payoff_matrix,
            rng,
        )
        if not config.wrap_edges:
            valid = shifted_neighbour(
                np.ones(strategies.shape, dtype=np.uint8),
                dy,
                dx,
                False,
                fill_value=0,
            ).astype(bool)
            interaction_payoff = np.where(valid, interaction_payoff, 0.0)
        payoff += interaction_payoff

    return payoff


def copy_best_neighbour_strategy(
    strategies: np.ndarray,
    payoff: np.ndarray,
    config: SimulationConfig,
) -> np.ndarray:
    """Copy the strategy of the highest-payoff neighbour when it is better."""

    best_payoff = payoff.copy()
    best_strategy = strategies.copy()

    for dy, dx in MOORE_OFFSETS:
        neighbour_payoff = shifted_neighbour(
            payoff,
            dy,
            dx,
            config.wrap_edges,
            fill_value=-np.inf,
        )
        neighbour_strategy = shifted_neighbour(
            strategies,
            dy,
            dx,
            config.wrap_edges,
            fill_value=0,
        )
        better = neighbour_payoff > best_payoff
        best_payoff = np.where(better, neighbour_payoff, best_payoff)
        best_strategy = np.where(better, neighbour_strategy, best_strategy)

    return best_strategy.astype(np.uint8)


def apply_mutation(
    strategies: np.ndarray,
    probability: float,
    strategy_count: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Randomly replace strategies according to mutation probability."""

    mask = mutation_mask(strategies.shape, probability, rng)
    if not np.any(mask):
        return strategies.astype(np.uint8, copy=True)

    mutated = strategies.copy()
    random_strategies = rng.integers(
        low=0,
        high=strategy_count,
        size=strategies.shape,
        dtype=np.uint8,
    )
    mutated[mask] = random_strategies[mask]
    return mutated.astype(np.uint8)


def simulation_step(world: "World") -> None:
    """Advance a world by one generation in place."""

    config = world.config
    payoff = compute_payoffs(world.strategy, config, world.rng)
    next_strategy = copy_best_neighbour_strategy(world.strategy, payoff, config)
    next_strategy = apply_mutation(
        next_strategy,
        config.mutation_probability,
        config.strategy_count,
        world.rng,
    )

    energy = world.energy + payoff * config.payoff_energy_scale - config.living_cost
    world.energy = np.clip(energy, config.min_energy, config.max_energy).astype(np.float32)
    world.age = np.minimum(world.age.astype(np.uint32) + 1, np.iinfo(np.uint16).max).astype(
        np.uint16
    )
    world.payoff = payoff
    world.strategy = next_strategy
    world.generation += 1


if False:  # pragma: no cover
    from .world import World

