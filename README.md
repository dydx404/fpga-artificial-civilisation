# FPGA Artificial Civilisation Engine

A distributed FPGA-accelerated game-theory laboratory for testing long-horizon strategic behaviour, emergent cooperation, betrayal, adaptation, and social evolution.

This repository is designed as the starting point for an ambitious second-year FPGA group project. The project is framed as a scientific simulation platform rather than a game: strategies compete in repeated games, evolve through tournaments, and can later inhabit a 2D artificial civilisation where local interactions create emergent social behaviour.

## Short Pitch

The project has two connected modes:

1. Strategy Arena / Strategy Colosseum.
2. Artificial Civilisation / Spatial Evolution.

In Strategy Arena mode, many strategies play long repeated games such as Prisoner's Dilemma, Snowdrift, Stag Hunt, and Public Goods games. They are scored, ranked, mutated, evolved, and visualised through leaderboards, payoff matrices, and robustness metrics.

In Artificial Civilisation mode, strategies become agents in a 2D world. Each agent has a strategy, payoff, energy, age, and room for future memory/trust state. Agents interact with neighbours, and over many generations the world can produce cooperation clusters, defector waves, inequality, collapse, recovery, or stable artificial societies.

The key engineering claim is simple: repeated strategic interaction is massively parallel. An FPGA can compute many long matches or local neighbour interactions with deterministic timing, while the host handles experiment control, networking, visualisation, and analysis.

## Two Connected Modes

### 1. Strategy Arena / Strategy Colosseum

The Strategy Arena is the clearer MVP because it is measurable, benchmarkable, and easier to implement on FPGA. A match core can repeatedly evaluate strategy decisions, payoff lookup, score accumulation, memory/history update, mutation/randomness, and statistics reduction.

The arena can support strategies such as:

- Always Cooperate.
- Always Defect / Betray.
- Tit-for-Tat.
- Suspicious Tit-for-Tat.
- Generous Tit-for-Tat.
- Random(p).
- Pavlov / Win-Stay-Lose-Shift.
- Grudger.
- Adaptive strategies.
- Q-learning agents.
- Small neural-network agents as stretch goals.

The natural FPGA scaling story is many parallel match cores, each running long repeated games or tournament shards.

### 2. Artificial Civilisation / Spatial Evolution

The spatial civilisation mode is the visually impressive extension. Arena-tested strategies can be placed onto a grid where agents interact with neighbours. This produces the demo-friendly phenomena: cooperation clusters, betrayal waves, collapse, recovery, inequality, resource competition, migration, alliances, and social fragmentation.

The same strategy catalogue, payoff matrices, mutation rules, and metrics should be reusable across both modes.

## Why FPGA?

The Strategy Arena loop is regular and parallel:

- Select a strategy pair.
- Read compact strategy state and memory/history.
- Compute decisions for one repeated-game round.
- Perform payoff lookup.
- Accumulate scores and cooperation counts.
- Apply noise, mutation, or random decisions.
- Reduce tournament statistics.

The spatial update loop is also regular and parallel:

- Fetch a cell and its Moore neighbourhood.
- Compute game payoffs against nearby agents.
- Select the next strategy from local fitness.
- Apply mutation or randomness.
- Commit into a double-buffered next world.
- Reduce global statistics such as cooperation ratio and mean payoff.

The FPGA is a good fit because compact match cores or spatial update cores can be pipelined and replicated, while the processing system remains free for orchestration.

## Scientific Motivation

The project sits at the intersection of:

- Evolutionary game theory: how cooperation survives among self-interested agents.
- Cellular automata: how simple local rules generate complex global structure.
- Multi-agent systems: how distributed decision-making creates emergent behaviour.
- Complex systems science: how societies collapse, recover, fragment, or stabilise.
- Hardware acceleration: how custom datapaths change the scale of simulation.

The updated MVP uses repeated Prisoner's Dilemma tournaments. The competitive version expands to many parallel match cores, configurable payoff matrices, mutation, strategy evolution, dashboards, and CPU versus FPGA benchmarks. The stretch version places evolved strategies into artificial civilisations and eventually explores multi-board strategy leagues or distributed spatial worlds.

## Architecture Overview

The intended final architecture has three cooperating layers:

- Host machine: tournament/civilisation configuration, frontend visualisation, data logging, multi-board orchestration, and analysis.
- Zynq processing system: Python/PYNQ control plane, DMA setup, result transfer, network bridge, and runtime parameters.
- FPGA programmable logic: repeated match cores, payoff computation, mutation RNG, optional spatial update engine, and statistics reduction.

High-level layers:

1. Strategy Arena Layer: defines games, strategies, payoff matrices, round counts, noise, mutation, and population settings.
2. FPGA Match Engine: many parallel match cores simulate long repeated games and reduce statistics.
3. Evolution Layer: weaker strategies are eliminated, stronger strategies reproduce, parameters mutate, and new variants enter the population.
4. Artificial Civilisation Layer: optional spatial version where strategies live on a grid/world.
5. Visualisation / Dashboard: leaderboard, payoff heatmap, strategy matrix, cooperation ratio, population distribution, robustness score, replay, and civilisation map.

The Python model in `models/python` is the reference implementation. RTL in `rtl/src` is an honest scaffold for the hardware engine and intentionally does not claim to be complete.

## MVP Path

The first working milestone should be arena-first:

1. Python repeated Prisoner's Dilemma tournament simulator.
2. Fixed strategy catalogue: cooperate, defect, tit-for-tat variants, random, Pavlov, and Grudger.
3. Leaderboard and strategy-vs-strategy payoff matrix.
4. Single FPGA match core for repeated Prisoner's Dilemma.
5. Score accumulation over many rounds.
6. CPU versus FPGA benchmark plan using rounds per second and matches per second.
7. Many-core match-engine design as the next hardware step.
8. Optional handoff from arena winners into the spatial civilisation model.

## Stretch Goals

- Runtime-configurable payoff matrices.
- Many parallel match cores.
- Evolutionary tournaments with mutation.
- Robustness and exploitability scoring.
- Hardware LFSR mutation.
- DMA transfer of world frames.
- Resource and energy field.
- Reproduction, death, migration, and territorial pressure.
- Trust or memory state per agent.
- Public Goods and Snowdrift game kernels.
- Web or Unity frontend with live heatmaps.
- Hardware statistics reduction.
- Multi-board tournament sharding or region partitioning.
- AI-assisted analysis of emergent behaviour.

## Repository Layout

```text
docs/                          Architecture, risk, MVP, interfaces, and demo planning.
docs/strategy_arena.md          Strategy Colosseum concept and roadmap.
docs/multi_board_architecture.md Multi-PYNQ extension architecture.
models/python/                  Numpy reference simulator, examples, and tests.
rtl/                            SystemVerilog scaffold for the FPGA update engine.
pynq/                           PYNQ overlay, DMA, and host-control placeholders.
frontend/                       Python and web visualisation scaffolds.
benchmarks/                     CPU baseline, metric schema, and FPGA benchmarking plan.
scripts/                        Setup, test, and formatting helpers.
reports/                        Proposal, interim, and final report outlines.
project_management/             Sprint plan, backlog, and integration checklists.
```

## Quickstart: Current Python Simulator

The current starter code implements the spatial Python reference model. The Strategy Arena tournament simulator is now the recommended next MVP direction and is tracked in the backlog.

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

The arena FPGA design starts with a simple repeated match engine:

- A match scheduler selects strategy pairs.
- Strategy state and memory/history are read.
- Strategy decision logic emits actions.
- A payoff unit evaluates the game round.
- Scores and cooperation counts accumulate.
- RNG provides noise, mutation, and random strategy behaviour.
- Statistics reducers emit compact result records.

The spatial FPGA design can reuse some pieces in a streaming update engine:

- World state is held in current and next buffers.
- A neighbour fetch stage supplies each cell and its 8 neighbours.
- A payoff unit evaluates local game interactions.
- A strategy update unit chooses the best neighbour strategy.
- An LFSR supplies mutation randomness.
- A statistics reducer counts strategy distribution and sums payoff.
- The updated cell is written into the next buffer.
- Buffers swap at frame boundaries.

The first hardware milestone should be a fixed repeated Prisoner's Dilemma match core. More advanced strategy sets, many-core scheduling, spatial update, and resource fields can be added only after the base datapath is stable.

## Benchmarking Philosophy

Benchmarking should compare useful simulation throughput, not just clock frequency. The core metrics are:

- Cells updated per second.
- Rounds simulated per second.
- Matches completed per second.
- Frames per second for a fixed world size.
- Tournament shards completed per second.
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

- Tier 0: Python tournament simulator only.
- Tier 1: Single FPGA match core for repeated Prisoner's Dilemma.
- Tier 2: Many parallel FPGA match cores.
- Tier 3: Evolutionary tournament with mutation.
- Tier 4: Spatial artificial civilisation.
- Tier 5: Multi-board distributed strategy league / civilisation world.

If integration slips, freeze the highest reliable tier and polish the science story, benchmark, and demo around it.

## Demo Vision

The ideal demo opens with the Strategy Colosseum: strategies enter a repeated-game tournament, a leaderboard and payoff matrix update live, then mutation/evolution changes the population. The team compares CPU and FPGA match throughput. The finale places winning strategies into a spatial civilisation map where cooperation clusters, betrayal waves, collapse, and recovery become visible.

## Current Status

This initial commit provides a serious scaffold: a runnable Python reference model, tests, documentation, SystemVerilog skeletons, PYNQ placeholders, frontend placeholders, benchmark scripts, report outlines, and project management material.

The RTL is not complete yet. It is a starting architecture with syntactically plausible modules and TODOs for the real datapath work.
