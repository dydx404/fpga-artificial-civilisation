"""CPU baseline benchmark for the Python reference simulator."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "models" / "python"))

from civsim.config import SimulationConfig  # noqa: E402
from civsim.metrics import metrics_snapshot  # noqa: E402
from civsim.world import World  # noqa: E402


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=REPO_ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--width", type=int, default=256)
    parser.add_argument("--height", type=int, default=256)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--mutation", type=float, default=0.001)
    parser.add_argument("--output", type=Path, default=Path("outputs/cpu_baseline.json"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = SimulationConfig(
        width=args.width,
        height=args.height,
        seed=args.seed,
        mutation_probability=args.mutation,
    )
    world = World.random(config)

    start = time.perf_counter()
    for _ in range(args.steps):
        world.step()
    elapsed = time.perf_counter() - start

    cells = args.width * args.height * args.steps
    result = {
        "backend": "python_numpy_cpu",
        "commit": git_commit(),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "width": args.width,
        "height": args.height,
        "steps": args.steps,
        "mutation_probability": args.mutation,
        "elapsed_seconds": elapsed,
        "cells_updated_per_second": cells / elapsed if elapsed > 0 else None,
        "frames_per_second": args.steps / elapsed if elapsed > 0 else None,
        "final_metrics": metrics_snapshot(world),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

