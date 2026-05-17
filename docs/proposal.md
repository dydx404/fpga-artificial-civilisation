# Project Proposal

## Title

FPGA-Accelerated Spatial Game Dynamics Simulator

## One-Sentence Summary

Build a 2D multi-agent strategy grid where simple agents repeatedly interact with local neighbours, then accelerate the regular update loop on an FPGA and visualise the resulting spatial dynamics.

## Motivation

Many systems can be studied through local interactions: each element has a state, interacts with neighbours, and updates according to simple rules. Evolutionary game dynamics provide a compact mathematical setting for this idea. Agents can cooperate, defect, retaliate, randomise, or switch strategy based on recent outcomes.

This project uses that setting as a practical FPGA workload. The local update step is regular, parallel, and deterministic, making it suitable for pipelined hardware and CPU/FPGA benchmarking.

## Scope

The project focuses on:

- 2D grids or small graph-like neighbourhoods.
- Repeated Prisoner's Dilemma as the first game.
- Small finite-state strategy set.
- Synchronous state updates using double buffering.
- Visualisation of spatial cooperation and competition.
- Correctness and speed comparison against a Python reference model.

The project avoids:

- Claims of realistic social simulation.
- Large-scale machine learning.
- Open-ended agent intelligence.
- Complex economic or sociological modelling.

## MVP Deliverables

| Area | MVP Deliverable |
| --- | --- |
| Model | Python reference simulator for repeated local games |
| Hardware | FPGA update/match core for the MVP rule |
| Interface | PYNQ/host control path for configuration and frame transfer |
| Visualisation | Evolving grid, cooperation ratio, strategy distribution, payoff map |
| Benchmark | CPU vs FPGA timing plus small-grid correctness checks |
| Report | Architecture, limitations, fallback tier, and measured results |

## Success Criteria

- A teammate can explain the update rule without specialist game-theory knowledge.
- Python and FPGA agree on deterministic small-grid cases.
- The FPGA performs a real compute role in the update loop.
- The demo shows changing spatial patterns over time.
- Benchmarks separate compute time from transfer/visualisation overhead.

## Expected Demonstration

1. Initialise a mixed strategy grid.
2. Run repeated local Prisoner's Dilemma interactions.
3. Show cooperation clusters, defector spread, or oscillatory patterns.
4. Enable mutation/noise as an optional parameter.
5. Compare CPU and FPGA update throughput.
6. Show resource use and explain the FPGA datapath.

## Stretch Goals

- More strategy types.
- Graph topologies beyond regular grids.
- Hardware statistics reducer.
- Web dashboard.
- Multi-board partitioning.
- Resource/reputation extensions.
