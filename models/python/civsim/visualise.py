"""Matplotlib visualisation helpers."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm

from .metrics import metrics_snapshot

STRATEGY_CMAP = ListedColormap(["#2ca25f", "#de2d26", "#3182bd", "#756bb1"])
STRATEGY_NORM = BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], STRATEGY_CMAP.N)


def plot_world(world: "World", title: str | None = None) -> plt.Figure:
    """Create a three-panel figure for strategy, payoff, and energy."""

    snapshot = metrics_snapshot(world)
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), constrained_layout=True)

    strategy_ax, payoff_ax, energy_ax = axes
    strategy_image = strategy_ax.imshow(world.strategy, cmap=STRATEGY_CMAP, norm=STRATEGY_NORM)
    strategy_ax.set_title("Strategy")
    strategy_ax.set_xticks([])
    strategy_ax.set_yticks([])
    cbar = fig.colorbar(strategy_image, ax=strategy_ax, ticks=[0, 1, 2, 3], fraction=0.046)
    cbar.ax.set_yticklabels(["C", "D", "TFT", "R"])

    payoff_image = payoff_ax.imshow(world.payoff, cmap="viridis")
    payoff_ax.set_title("Payoff")
    payoff_ax.set_xticks([])
    payoff_ax.set_yticks([])
    fig.colorbar(payoff_image, ax=payoff_ax, fraction=0.046)

    energy_image = energy_ax.imshow(world.energy, cmap="magma")
    energy_ax.set_title("Energy")
    energy_ax.set_xticks([])
    energy_ax.set_yticks([])
    fig.colorbar(energy_image, ax=energy_ax, fraction=0.046)

    if title is None:
        title = (
            f"generation {world.generation} | "
            f"cooperation {snapshot['cooperation_ratio']:.3f} | "
            f"mean payoff {snapshot['mean_payoff']:.2f}"
        )
    fig.suptitle(title)
    return fig


def save_world_plot(world: "World", path: str | Path, title: str | None = None) -> None:
    """Save a world figure and close it."""

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig = plot_world(world, title=title)
    fig.savefig(path, dpi=150)
    plt.close(fig)


def strategy_rgb_frame(strategies: np.ndarray) -> np.ndarray:
    """Convert strategy IDs to an RGB uint8 image for lightweight frontends."""

    palette = np.array(
        [
            [44, 162, 95],
            [222, 45, 38],
            [49, 130, 189],
            [117, 107, 177],
        ],
        dtype=np.uint8,
    )
    clipped = np.clip(strategies.astype(np.int64), 0, len(palette) - 1)
    return palette[clipped]


if False:  # pragma: no cover
    from .world import World

