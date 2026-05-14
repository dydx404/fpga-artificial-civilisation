"""Run the MVP Prisoner's Dilemma simulation and save frames."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from civsim.config import PayoffMatrix, SimulationConfig
from civsim.metrics import flatten_metrics, metrics_snapshot
from civsim.visualise import save_world_plot
from civsim.world import World


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--width", type=int, default=128)
    parser.add_argument("--height", type=int, default=128)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--mutation", type=float, default=0.001)
    parser.add_argument("--initial-cooperation", type=float, default=0.5)
    parser.add_argument("--save-every", type=int, default=20)
    parser.add_argument("--output", type=Path, default=Path("outputs/pd_demo"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    config = SimulationConfig(
        width=args.width,
        height=args.height,
        seed=args.seed,
        initial_cooperation=args.initial_cooperation,
        mutation_probability=args.mutation,
        payoff_matrix=PayoffMatrix(R=3.0, S=0.0, T=5.0, P=1.0),
    )
    world = World.random(config)

    metrics_path = args.output / "metrics.csv"
    fieldnames: list[str] | None = None
    with metrics_path.open("w", newline="", encoding="utf-8") as metrics_file:
        writer: csv.DictWriter[str] | None = None

        for step in range(args.steps + 1):
            snapshot = flatten_metrics(metrics_snapshot(world))
            if writer is None:
                fieldnames = list(snapshot.keys())
                writer = csv.DictWriter(metrics_file, fieldnames=fieldnames)
                writer.writeheader()
            writer.writerow(snapshot)

            if step % args.save_every == 0 or step == args.steps:
                save_world_plot(world, args.output / f"frame_{step:05d}.png")

            if step < args.steps:
                world.step()

    print(f"wrote frames and metrics to {args.output}")


if __name__ == "__main__":
    main()
