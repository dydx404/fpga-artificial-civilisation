# Multi-Board Architecture

The project may have access to more than one PYNQ-Z1 board. A multi-board architecture should be treated as a high-level extension, not an MVP dependency. It can make the final story much stronger if the single-board path is stable.

## Core Idea

Each PYNQ board runs a local simulation shard:

- One tournament arena.
- One subset of strategy pairings.
- One spatial civilisation region.
- One strategy family or league participant.

The host controller coordinates experiments, distributes configuration, receives summary statistics, and aggregates global visualisations.

```text
Host controller
  -> sends tournament/game configuration to PYNQ boards
  -> boards run accelerated simulations locally
  -> boards stream summary statistics/results back
  -> host aggregates and visualises global results
```

## Mode 1: Parallel Tournament Sharding

Each board evaluates part of the strategy matchup matrix.

Example:

- Board 1 runs strategy pairs A-D.
- Board 2 runs strategy pairs E-H.
- Board 3 runs noisy or mutated variants.
- Host aggregates leaderboards and payoff matrices.

This is the cleanest multi-board mode because boards do not need tight synchronisation. They can run independent match batches and report results asynchronously.

## Mode 2: Spatial Civilisation Partitioning

Each board owns a region of the world.

- Board 1 simulates region north-west.
- Board 2 simulates region north-east.
- Board 3 simulates region south or a separate island.
- Border agents are exchanged over Ethernet between generations.

This creates distributed artificial societies. It is visually powerful but more difficult because boundary exchange, latency, and deterministic replay matter.

## Mode 3: Strategy League

Each board hosts a civilisation, strategy family, or evolutionary pool.

Boards can:

- Compete in periodic inter-board tournaments.
- Trade high-performing strategy variants.
- Exchange memes or information.
- Migrate agents between regions.
- Invade or challenge other regions under controlled rules.

This is the most ambitious narrative mode: a distributed strategy league where hardware islands develop different social behaviours.

## Host Responsibilities

The host controller should:

- Maintain experiment configuration.
- Assign shards to boards.
- Track board health and progress.
- Collect metrics and result packets.
- Aggregate global rankings.
- Render dashboards and replay summaries.
- Save reproducible experiment logs.

## Board Responsibilities

Each PYNQ board should:

- Load its FPGA overlay.
- Receive a configuration packet.
- Run local accelerated matches or region updates.
- Reduce statistics locally.
- Send compact summaries back to the host.
- Preserve enough metadata for reproducibility.

## Network Data

Keep network traffic summary-oriented at first:

- Strategy IDs.
- Match scores.
- Cooperation counts.
- Mutation seeds.
- Population counts.
- Region border slices for spatial mode.

Do not stream full high-resolution frames from every board until the low-bandwidth summary path works.

## Synchronisation Options

Tournament sharding:

- Mostly asynchronous.
- Host waits for all shards before computing final leaderboard.

Spatial partitioning:

- Generation-level synchronisation.
- Boards exchange border agents after each generation or after fixed batches.

Strategy league:

- Epoch-level synchronisation.
- Boards run locally, then meet at league checkpoints.

## Risk

Multi-board work adds network, orchestration, reproducibility, and demo complexity. It should only be attempted after a single-board result exists. A strong single-board Strategy Arena still makes a complete project.

## Best Use in the Final Demo

The most realistic high-impact demo is:

1. Run a single-board arena live.
2. Show the host dashboard aggregating several boards or simulated boards.
3. Explain that each board is an arena shard or civilisation region.
4. Compare aggregate throughput and show a combined leaderboard.
