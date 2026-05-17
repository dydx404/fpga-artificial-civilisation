# Multi-Board Extension

Multi-board execution is a stretch goal. It should only be considered after the single-board spatial update path is stable.

## Basic Idea

Each PYNQ board owns part of the workload:

- a grid region,
- a batch of repeated-match tests,
- or a parameter sweep shard.

The host distributes configuration, receives compact metrics, and aggregates plots.

```text
Host controller
  -> sends configuration to each PYNQ board
  -> boards run local update workloads
  -> boards stream metrics/results back
  -> host aggregates visualisation and benchmarks
```

## Mode 1: Parameter Sweep Sharding

Each board runs the same model with different parameters:

- mutation probability,
- payoff matrix,
- initial strategy distribution,
- neighbourhood type.

This is the simplest distributed mode because boards are independent.

## Mode 2: Spatial Partitioning

Each board owns one grid region. Border cells are exchanged between generations.

Risks:

- synchronisation overhead,
- Ethernet latency,
- border consistency bugs,
- harder deterministic replay.

## Recommended Scope

For the 35-day project, treat multi-board execution as a report extension or simulated design. A reliable single-board accelerator is more valuable than a fragile distributed demo.
