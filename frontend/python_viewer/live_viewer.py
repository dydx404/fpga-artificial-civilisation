"""Live matplotlib viewer for the Python simulation."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "models" / "python"))

from civsim.config import SimulationConfig  # noqa: E402
from civsim.metrics import metrics_snapshot  # noqa: E402
from civsim.visualise import STRATEGY_CMAP, STRATEGY_NORM  # noqa: E402
from civsim.world import World  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--width", type=int, default=128)
    parser.add_argument("--height", type=int, default=128)
    parser.add_argument("--mutation", type=float, default=0.001)
    parser.add_argument("--interval-ms", type=int, default=80)
    args = parser.parse_args()

    config = SimulationConfig(
        width=args.width,
        height=args.height,
        mutation_probability=args.mutation,
    )
    world = World.random(config)

    fig, ax = plt.subplots(figsize=(7, 7))
    image = ax.imshow(world.strategy, cmap=STRATEGY_CMAP, norm=STRATEGY_NORM)
    ax.set_xticks([])
    ax.set_yticks([])

    def update(_frame: int):
        world.step()
        snapshot = metrics_snapshot(world)
        image.set_data(world.strategy)
        ax.set_title(
            f"generation {world.generation} | cooperation {snapshot['cooperation_ratio']:.3f}"
        )
        return (image,)

    animation.FuncAnimation(fig, update, interval=args.interval_ms, blit=False)
    plt.show()


if __name__ == "__main__":
    main()

