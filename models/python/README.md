# Python Reference Model

This package is the mathematical reference implementation for the FPGA-Accelerated Spatial Game Dynamics Simulator. It should stay readable, tested, and deterministic under fixed seeds.

The current model implements:

- 2D grid of agents.
- Strategy, payoff, energy, and age fields.
- Prisoner's Dilemma payoff.
- Moore neighbourhood interaction.
- Best-neighbour strategy copying.
- Mutation probability.
- Cooperation ratio, entropy, mean payoff, and strategy distribution metrics.
- Matplotlib visualisation.

## Setup

```bash
cd models/python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Run an Example

```bash
python examples/run_prisoners_dilemma.py --width 128 --height 128 --steps 200 --output ../../outputs/pd_demo
```

The script writes PNG frames and a `metrics.csv` file.

## Design Notes

The Python model intentionally keeps richer fields than the first RTL target. The first FPGA version may only update packed strategy words. Python remains the reference for behaviour and experiment design.

The default boundary rule is wrap-around. Disable it only after hardware and Python comparison tests are updated.
