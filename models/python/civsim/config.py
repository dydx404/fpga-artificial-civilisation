"""Configuration objects for the reference simulator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class PayoffMatrix:
    """A two-strategy payoff matrix.

    R: reward for mutual cooperation.
    S: sucker payoff when cooperating against a defector.
    T: temptation payoff when defecting against a cooperator.
    P: punishment for mutual defection.
    """

    R: float = 3.0
    S: float = 0.0
    T: float = 5.0
    P: float = 1.0


@dataclass
class SimulationConfig:
    """Simulation parameters shared by examples, tests, and benchmarks."""

    width: int = 128
    height: int = 128
    seed: Optional[int] = 1
    initial_cooperation: float = 0.5
    mutation_probability: float = 0.001
    payoff_matrix: PayoffMatrix = field(default_factory=PayoffMatrix)
    wrap_edges: bool = True
    initial_energy: float = 16.0
    living_cost: float = 0.05
    payoff_energy_scale: float = 0.05
    min_energy: float = 0.0
    max_energy: float = 255.0
    strategy_count: int = 4

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("width and height must be positive")
        if not 0.0 <= self.initial_cooperation <= 1.0:
            raise ValueError("initial_cooperation must be in [0, 1]")
        if not 0.0 <= self.mutation_probability <= 1.0:
            raise ValueError("mutation_probability must be in [0, 1]")
        if self.strategy_count < 2:
            raise ValueError("strategy_count must include at least cooperate and defect")
        if self.min_energy > self.max_energy:
            raise ValueError("min_energy cannot exceed max_energy")

