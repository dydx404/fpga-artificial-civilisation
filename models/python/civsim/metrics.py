"""Metrics for simulation analysis and live visualisation."""

from __future__ import annotations

import math
from collections import OrderedDict

import numpy as np

from .agent import Strategy, strategy_name


def strategy_distribution(strategies: np.ndarray, strategy_count: int = 4) -> OrderedDict[str, int]:
    """Return counts for each known strategy."""

    counts = np.bincount(strategies.astype(np.int64).ravel(), minlength=strategy_count)
    result: OrderedDict[str, int] = OrderedDict()
    for strategy_id in range(strategy_count):
        result[strategy_name(strategy_id)] = int(counts[strategy_id])
    return result


def cooperation_ratio(strategies: np.ndarray) -> float:
    """Fraction of cells using strategies considered cooperative in the MVP."""

    cooperative = (strategies == Strategy.COOPERATE) | (strategies == Strategy.TIT_FOR_TAT)
    return float(np.mean(cooperative))


def mean_payoff(payoff: np.ndarray) -> float:
    """Mean accumulated payoff per cell."""

    return float(np.mean(payoff))


def strategy_entropy(strategies: np.ndarray, strategy_count: int = 4) -> float:
    """Shannon entropy of the strategy distribution in bits."""

    counts = np.bincount(strategies.astype(np.int64).ravel(), minlength=strategy_count)
    total = counts.sum()
    if total == 0:
        return 0.0
    probabilities = counts[counts > 0] / total
    return float(-np.sum(probabilities * np.log2(probabilities)))


def metrics_snapshot(world: "World") -> dict[str, float | int | dict[str, int]]:
    """Collect standard metrics for a world."""

    distribution = strategy_distribution(world.strategy, world.config.strategy_count)
    return {
        "generation": world.generation,
        "cooperation_ratio": cooperation_ratio(world.strategy),
        "mean_payoff": mean_payoff(world.payoff),
        "mean_energy": float(np.mean(world.energy)),
        "strategy_entropy": strategy_entropy(world.strategy, world.config.strategy_count),
        "strategy_distribution": dict(distribution),
    }


def flatten_metrics(snapshot: dict[str, float | int | dict[str, int]]) -> dict[str, float | int]:
    """Flatten nested strategy counts for CSV writing."""

    flat: dict[str, float | int] = {}
    for key, value in snapshot.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flat[f"strategy_{sub_key}"] = sub_value
        elif isinstance(value, (int, float)) and not isinstance(value, bool):
            flat[key] = value
        else:
            raise TypeError(f"unsupported metric value for {key}: {type(value)!r}")

    entropy = flat.get("strategy_entropy")
    if isinstance(entropy, float) and math.isnan(entropy):
        flat["strategy_entropy"] = 0.0
    return flat


if False:  # pragma: no cover
    from .world import World

