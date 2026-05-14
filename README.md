# FPGA Artificial Civilisation Engine

A hardware-accelerated artificial civilisation simulator for studying emergent cooperation, strategy evolution, resource competition, trust, mutation, collapse, and recovery in large agent populations.

This repository is designed as the starting point for an ambitious second-year FPGA group project. The project is framed as a scientific simulation platform rather than a game: a 2D society of agents evolves under local game-theoretic rules, while the FPGA accelerates the repeated local update step that dominates runtime.

## Short Pitch

The simulator models a 2D world of agents. Each agent has a strategy, payoff, energy, age, and room for future memory/trust state. Agents interact with neighbours using games such as Prisoner's Dilemma, Snowdrift, Stag Hunt, Public Goods, or custom payoff matrices. Over many generations, strategy copying, mutation, reproduction, migration, and resource pressure can produce cooperation clusters, defector waves, inequality, collapse, or stable artificial societies.

The key engineering claim is simple: local agent updates are massively parallel. An FPGA can compute thousands of repeated neighbour interactions with deterministic timing, streaming frames between host memory and programmable logic while the host handles control, visualisation, networking, and analysis.

## Why FPGA?

The core update loop is spatial, regular, and parallel:

- Fetch a cell and its Moore neighbourhood.
- Compute game payoffs against nearby agents.
- Select the next strategy from local fitness.
- Apply mutation or randomness.
- Commit into a double-buffered next world.
- Reduce global statistics such as cooperation ratio and mean payoff.

This resembles a cellular automaton, stencil computation, and multi-agent simulation at the same time. The FPGA is a good fit because the same compact datapath can be pipelined and replicated, while the processing system remains free for orchestration.

## Scientific Motivation

The project sits at the intersection of:

- Evolutionary game theory: how cooperation survives among self-interested agents.
- Cellular automata: how simple local rules generate complex global structure.
- Multi-agent systems: how distributed decision-making creates emergent behaviour.
- Complex systems science: how societies collapse, recover, fragment, or stabilise.
- Hardware acceleration: how custom datapaths change the scale of simulation.

The MVP uses Prisoner's Dilemma on a fixed grid. The competitive version expands to configurable payoff matrices, mutation, resources, heatmaps, and CPU versus FPGA benchmarks. The stretch version explores artificial civilisation features such as territory, memory, trust, public goods, epidemic or meme spread, and multi-FPGA partitioning.

## Architecture Overview

The intended final architecture has three cooperating layers:

- Host machine: experiment configuration, frontend visualisation, data logging, and analysis.
- Zynq processing system: Python/PYNQ control plane, DMA setup, frame transfer, network bridge, and runtime parameters.
- FPGA programmable logic: pipelined local update engine, payoff computation, mutation RNG, double-buffered world traversal, and statistics reduction.

The Python model in `models/python` is the reference implementation. RTL in `rtl/src` is an honest scaffold for the hardware engine and intentionally does not claim to be complete.

## MVP Path

The first working milestone is deliberately achievable:

1. Fixed 2D grid.
2. One compact strategy per cell plus Python-side payoff, energy, and age arrays.
3. Strategies: cooperate, defect, tit-for-tat placeholder, random placeholder.
4. Moore neighbourhood.
5. Prisoner's Dilemma payoff.
6. Double-buffered update.
7. Strategy copying from the best neighbour.
8. Mutation probability.
9. Python visualisation and metrics.
10. CPU timing baseline and FPGA benchmark plan.

## Stretch Goals

- Runtime-configurable payoff matrices.
- Hardware LFSR mutation.
- DMA transfer of world frames.
- Resource and energy field.
- Reproduction, death, migration, and territorial pressure.
- Trust or memory state per agent.
- Public Goods and Snowdrift game kernels.
- Web or Unity frontend with live heatmaps.
- Hardware statistics reduction.
- Multi-FPGA region partitioning.
- AI-assisted analysis of emergent behaviour.

## Repository Layout

```text
docs/                 Architecture, risk, MVP, interfaces, and demo planning.
models/python/         Numpy reference simulator, examples, and tests.
rtl/                   SystemVerilog scaffold for the FPGA update engine.
pynq/                  PYNQ overlay, DMA, and host-control placeholders.
frontend/              Python and web visualisation scaffolds.
benchmarks/            CPU baseline, metric schema, and FPGA benchmarking plan.
scripts/               Setup, test, and formatting helpers.
reports/               Proposal, interim, and final report outlines.
project_management/    Sprint plan, backlog, and integration checklists.
```

## Quickstart: Python Simulator

From the repository root:

```bash
cd models/python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
python examples/run_prisoners_dilemma.py --steps 200 --output ../../outputs/pd_demo
```

The example saves PNG frames and a `metrics.csv` file showing cooperation ratio, mean payoff, entropy, and strategy counts over time.

## Planned FPGA Architecture

The FPGA design starts with a simple streaming update engine:

- World state is held in current and next buffers.
- A neighbour fetch stage supplies each cell and its 8 neighbours.
- A payoff unit evaluates local game interactions.
- A strategy update unit chooses the best neighbour strategy.
- An LFSR supplies mutation randomness.
- A statistics reducer counts strategy distribution and sums payoff.
- The updated cell is written into the next buffer.
- Buffers swap at frame boundaries.

The first hardware milestone can be a reduced cellular automaton or fixed Prisoner's Dilemma kernel. More advanced strategy sets and resource fields can be added only after the data path is stable.

## Benchmarking Philosophy

Benchmarking should compare useful simulation throughput, not just clock frequency. The core metrics are:

- Cells updated per second.
- Frames per second for a fixed world size.
- Energy or resource model cost if enabled.
- Host-to-FPGA transfer overhead.
- CPU reference time with identical rules.
- Correctness against the Python model on small worlds.

The benchmark plan intentionally separates compute-core speed, DMA transfer speed, and full-system speed.

## Team Organisation

The project is sized for a 6-person team:

1. FPGA compute core.
2. Memory, DMA, and interfaces.
3. Python reference model and theory.
4. Frontend visualisation.
5. Benchmarking and testing.
6. Integration, project management, and report.

Each role has an owner, but integration should happen weekly. The project is risky enough that frozen fallback tiers are part of the plan, not an embarrassment.

## Fallback Strategy

The fallback ladder is practical:

- Tier 0: Python simulation only.
- Tier 1: FPGA Conway/cellular automata engine.
- Tier 2: FPGA Prisoner's Dilemma update engine.
- Tier 3: Evolutionary game theory with mutation.
- Tier 4: Resources and civilisation features.
- Tier 5: Multi-kernel, trust, memory, and advanced visualisation.

If integration slips, freeze the highest reliable tier and polish the science story, benchmark, and demo around it.

## Demo Vision

The ideal demo begins with a random society, shows defectors spreading, introduces mutation and local copying, then reveals cooperation clusters emerging. Resource scarcity is added to trigger collapse and recovery. Finally, the team compares CPU and FPGA speed while live statistics update in a heatmap frontend.

## Current Status

This initial commit provides a serious scaffold: a runnable Python reference model, tests, documentation, SystemVerilog skeletons, PYNQ placeholders, frontend placeholders, benchmark scripts, report outlines, and project management material.

The RTL is not complete yet. It is a starting architecture with syntactically plausible modules and TODOs for the real datapath work.

