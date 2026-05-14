"""Run a resource-pressure variant using the existing energy field."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from civsim.config import PayoffMatrix, SimulationConfig
from civsim.visualise import save_world_plot
from civsim.world import World


def main() -> None:
    output = Path("outputs/resource_demo")
    output.mkdir(parents=True, exist_ok=True)

    config = SimulationConfig(
        width=128,
        height=128,
        seed=11,
        initial_cooperation=0.65,
        mutation_probability=0.005,
        initial_energy=8.0,
        living_cost=0.18,
        payoff_energy_scale=0.04,
        payoff_matrix=PayoffMatrix(R=3.0, S=0.0, T=5.0, P=1.0),
    )
    world = World.random(config)

    for step in range(201):
        if step % 25 == 0:
            save_world_plot(world, output / f"frame_{step:05d}.png")
        if step < 200:
            world.step()

    print(f"wrote resource-pressure frames to {output}")


if __name__ == "__main__":
    main()
