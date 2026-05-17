# Live Evolution and Video Output

This document describes a proposed output pipeline for turning simulations into live displays and exportable videos.

## Core Loop

Instead of copying every generation back to the host, the FPGA can run a small batch:

```text
FPGA runs K generations, for example K = 5
  -> writes or copies visual frame
  -> CPU saves/displays frame
  -> repeat
```

This keeps the demo smooth while reducing transfer overhead.

## Frame Interpretation

Each visual frame can encode:

- pixel/cell colour = strategy ID,
- brightness = fitness, energy, or payoff,
- optional overlay text = generation, cooperation rate, dominant strategy, mean payoff.

Example colour mapping:

| Strategy | Suggested Colour |
| --- | --- |
| Cooperate | green |
| Defect | red |
| Tit-for-Tat | blue |
| Random(p) | purple |
| Pavlov | yellow |
| User strategy | generated palette colour |

## Saved Output

Basic export:

```text
frames/
  frame_0000.png
  frame_0001.png
  frame_0002.png
```

Optional video export:

```bash
ffmpeg -framerate 20 -i frames/frame_%04d.png \
  -pix_fmt yuv420p evolution.mp4
```

## Metadata

For each run, save a small metadata file:

```json
{
  "grid_size": [128, 128],
  "frame_interval_generations": 5,
  "payoff_matrix": {"R": 3, "S": 0, "T": 5, "P": 1},
  "mutation_probability": 0.001,
  "seed": 42
}
```

## Host / FPGA Responsibilities

| Component | Responsibility |
| --- | --- |
| FPGA | Run generations, update state, reduce statistics |
| PYNQ/CPU | Copy selected frames and metrics |
| Host | Save PNGs, build video, show dashboard |

The FPGA should not render videos. It should produce state and metrics. The CPU/host should handle image/video formats.

## Demo Value

Video export is useful because it gives the team:

- repeatable demo evidence,
- report figures,
- social-media-style clips for presentation,
- easy comparison between parameter settings.
