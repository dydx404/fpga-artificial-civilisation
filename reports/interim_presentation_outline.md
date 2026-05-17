# Interim Presentation Outline

## Slide 1: Project Pitch

FPGA-accelerated spatial game dynamics: simple local strategic interactions, visible emergent patterns, measurable hardware speedup.

## Slide 2: Model

2D grid, repeated Prisoner's Dilemma, finite-state strategies, local payoff, imitate strongest neighbour.

## Slide 3: Why FPGA

Local neighbourhood computation, synchronous updates, double buffering, pipelined payoff/update units.

## Slide 4: System Architecture

Host, PYNQ processing system, FPGA update engine, Python reference model, visualisation.

## Slide 5: Current Progress

Python model, visualisation, tests, RTL skeletons, benchmark setup.

## Slide 6: Risks and Fallbacks

Show Tier 0 to Tier 5 fallback ladder.

## Slide 7: Next Steps

Hardware update core, correctness comparison, DMA/PYNQ integration, benchmark matrix.
