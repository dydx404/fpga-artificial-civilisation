# Fallback Plan

This project should be ambitious, but it needs a practical landing path. The fallback tiers are not failures. They are controlled freeze points that still produce a coherent demo and report.

## Tier 0: Python Simulation Only

Deliver:

- Complete Python simulation.
- Strong visualisation.
- Experiment results showing cooperation, collapse, and recovery.
- Clear architecture document for the FPGA path.

Use this if hardware integration collapses completely. The scientific story can still be strong.

## Tier 1: Conway / Cellular Automata FPGA Engine

Deliver:

- FPGA engine updates a simple binary cellular automaton.
- Python compares FPGA output against reference.
- Visualiser shows live hardware-driven grid updates.

This proves neighbour fetch, buffering, and display integration even if game theory logic is delayed.

## Tier 2: Prisoner's Dilemma FPGA Engine

Deliver:

- Fixed cooperate/defect strategies.
- Fixed payoff values.
- Moore neighbourhood.
- Double-buffered update.
- CPU versus FPGA benchmark for the same rules.

This is the minimum strong FPGA result.

## Tier 3: Evolutionary Game Theory with Mutation

Deliver:

- Mutation using LFSR randomness.
- Strategy copying from best neighbour.
- Hardware or PS-side strategy statistics.
- Parameter sweep for mutation probability.

This is a competitive target if DMA and buffering are under control.

## Tier 4: Resources / Civilisation Features

Deliver:

- Energy/resource field.
- Death or dormancy under scarcity.
- Recovery after resource regeneration.
- More expressive demo with collapse and rebound.

This should only be attempted after Tier 3 is stable.

## Tier 5: Crazy Extensions

Deliver one or two only if the base system is reliable:

- Trust or memory state.
- Public Goods game.
- Epidemic, meme, or information spread.
- Runtime-selectable game kernels.
- WebGPU or Unity visualisation.
- Multi-FPGA region partitioning.

## Freeze Rules

- End of Week 2: freeze at Tier 1 if no hardware neighbour update works.
- End of Week 3: freeze at Tier 2 if DMA or mutation remains unstable.
- Mid Week 4: freeze the demo feature set and stop adding science rules.
- Week 5: only fix, measure, document, and polish.

