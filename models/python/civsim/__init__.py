"""Reference simulator for spatial game dynamics."""

from .agent import Strategy
from .config import PayoffMatrix, SimulationConfig
from .world import World

__all__ = ["PayoffMatrix", "SimulationConfig", "Strategy", "World"]
