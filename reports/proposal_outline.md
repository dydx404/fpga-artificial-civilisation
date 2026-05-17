# Proposal Outline

## Title

FPGA-Accelerated Spatial Game Dynamics Simulator

## Motivation

Local strategic interaction can produce visible spatial patterns. The update rule is regular and parallel, making it a credible FPGA acceleration workload.

## Objectives

- Build a Python reference simulator.
- Design an FPGA-friendly spatial update pipeline.
- Visualise evolving strategy and payoff patterns.
- Benchmark CPU versus FPGA throughput.
- Keep the scope realistic for a 35-day group project.

## Method

Describe:

- 2D grid of agents.
- Repeated Prisoner's Dilemma.
- Simple finite-state strategies.
- Payoff accumulation.
- Imitation of strongest neighbour.
- Optional mutation/noise.
- Double-buffered synchronous updates.

## Hardware Plan

Describe:

- Neighbourhood fetch.
- Strategy decision unit.
- Payoff lookup.
- Accumulation and best-neighbour selection.
- LFSR mutation.
- Statistics reduction.
- PYNQ/host interface.

## Evaluation

- Correctness against Python on small deterministic grids.
- CPU versus FPGA cells updated per second.
- Transfer overhead versus kernel time.
- FPGA resource use.
- Visual examples of spatial dynamics.

## Risks

Neighbour fetch, DMA integration, scope creep, strategy semantics mismatch, and visualisation time.
