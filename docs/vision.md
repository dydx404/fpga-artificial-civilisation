# Vision

The project vision is a grounded FPGA-accelerated simulator for spatial game dynamics. It should be understandable as an engineering system: compact state, local interactions, synchronous updates, hardware acceleration, and live visualisation.

## Core Statement

Build a multi-agent strategy grid where simple agents repeatedly interact with neighbours. Use Python to define the model, FPGA logic to accelerate the local update loop, and host visualisation to show evolving spatial patterns.

## Design Principles

- Simple local rules.
- Emergent global patterns.
- Clear FPGA datapath.
- Deterministic correctness tests.
- Modular Python/RTL/PYNQ/frontend split.
- Scope suitable for a 35-day group project.

## Research / Engineering Questions

- How do local repeated games change global strategy distribution?
- When do cooperation clusters survive?
- How do mutation and noise affect stability?
- How much faster is a hardware update engine than a CPU reference?
- Which parts of the update rule map cleanly to FPGA logic?

## Success Criteria

- The MVP rule is clearly documented and implemented in Python.
- Hardware performs a real update computation, not just data movement.
- Python and hardware agree on deterministic small grids.
- Visualisation shows evolving strategy and payoff patterns.
- Benchmarks report cells/second, frames/second, and FPGA resource use.

## Long-Term Direction

If the MVP succeeds, the same architecture can support graph topologies, more strategy rules, resource fields, asynchronous updates, or multi-board partitioning. These remain extensions, not the core proposal.
