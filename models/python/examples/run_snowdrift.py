"""Run a Snowdrift/Hawk-Dove style payoff experiment."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from civsim.config import PayoffMatrix, SimulationConfig
from civsim.visualise import save_world_plot
from civsim.world import World


def main() -> None:
    output = Path("outputs/snowdrift_demo")
    output.mkdir(parents=True, exist_ok=True)

    config = SimulationConfig(
        width=128,
        height=128,
        seed=7,
        mutation_probability=0.002,
        payoff_matrix=PayoffMatrix(R=3.0, S=1.0, T=5.0, P=0.0),
    )
    world = World.random(config)

    for step in range(151):
        if step % 30 == 0:
            save_world_plot(world, output / f"frame_{step:05d}.png")
        if step < 150:
            world.step()

    print(f"wrote Snowdrift frames to {output}")


if __name__ == "__main__":
    main()
