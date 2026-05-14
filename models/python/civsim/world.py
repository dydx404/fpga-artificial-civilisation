"""Vectorised 2D world state."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

import numpy as np

from .agent import AgentSnapshot, Strategy
from .config import SimulationConfig
from .rng import create_rng


@dataclass
class World:
    """A 2D world of agents stored as Numpy arrays."""

    config: SimulationConfig
    strategy: np.ndarray
    payoff: np.ndarray
    energy: np.ndarray
    age: np.ndarray
    rng: np.random.Generator
    generation: int = 0

    @classmethod
    def random(cls, config: SimulationConfig) -> "World":
        """Create a random cooperate/defect world from a config."""

        rng = create_rng(config.seed)
        shape = (config.height, config.width)
        strategy = np.where(
            rng.random(shape) < config.initial_cooperation,
            Strategy.COOPERATE,
            Strategy.DEFECT,
        ).astype(np.uint8)
        return cls(
            config=config,
            strategy=strategy,
            payoff=np.zeros(shape, dtype=np.float32),
            energy=np.full(shape, config.initial_energy, dtype=np.float32),
            age=np.zeros(shape, dtype=np.uint16),
            rng=rng,
        )

    @classmethod
    def from_strategy_array(
        cls,
        strategies: np.ndarray,
        config: SimulationConfig | None = None,
    ) -> "World":
        """Create a world from an explicit strategy grid."""

        strategies = np.asarray(strategies, dtype=np.uint8)
        height, width = strategies.shape
        if config is None:
            config = SimulationConfig(width=width, height=height)
        elif config.width != width or config.height != height:
            raise ValueError("config dimensions must match strategy array")

        shape = (height, width)
        return cls(
            config=config,
            strategy=strategies.copy(),
            payoff=np.zeros(shape, dtype=np.float32),
            energy=np.full(shape, config.initial_energy, dtype=np.float32),
            age=np.zeros(shape, dtype=np.uint16),
            rng=create_rng(config.seed),
        )

    @property
    def shape(self) -> tuple[int, int]:
        """World shape as `(height, width)`."""

        return self.strategy.shape

    def step(self) -> None:
        """Advance the world by one generation."""

        from .update_rules import simulation_step

        simulation_step(self)

    def run(self, steps: int) -> Iterator["World"]:
        """Iterate over `steps` generations, yielding after each step."""

        for _ in range(steps):
            self.step()
            yield self

    def snapshot(self, y: int, x: int) -> AgentSnapshot:
        """Return a single-cell snapshot for debugging."""

        return AgentSnapshot(
            strategy=Strategy(int(self.strategy[y, x])),
            payoff=float(self.payoff[y, x]),
            energy=float(self.energy[y, x]),
            age=int(self.age[y, x]),
        )

    def copy(self) -> "World":
        """Deep-copy world arrays while preserving RNG state."""

        copied_rng = create_rng(None)
        copied_rng.bit_generator.state = self.rng.bit_generator.state
        return World(
            config=self.config,
            strategy=self.strategy.copy(),
            payoff=self.payoff.copy(),
            energy=self.energy.copy(),
            age=self.age.copy(),
            rng=copied_rng,
            generation=self.generation,
        )

