# Issue Backlog

Convert these into GitHub issues as the team commits to work.

## Python Model and Theory

- Confirm exact MVP update order.
- Add deterministic tiny-grid tests.
- Add Pavlov / Win-Stay-Lose-Shift strategy.
- Add neighbourhood selection: Moore vs Von Neumann.
- Add mutation/noise parameter sweep.
- Document strategy semantics for RTL.

## RTL Compute Core

- Finalise packed agent word.
- Complete payoff unit testbench.
- Implement strategy decision unit for cooperate/defect first.
- Add stateful strategy support incrementally.
- Integrate LFSR mutation threshold.
- Build single-cell update testbench.
- Compare one small grid against Python.

## Memory / PYNQ / Interface

- Define frame packing and unpacking helpers.
- Define AXI-lite/control register map.
- Prototype DMA or dry-run frame transfer.
- Measure transfer overhead.
- Decide buffer strategy for current/next frames.

## Visualisation

- Improve grid heatmap.
- Add cooperation ratio plot.
- Add strategy population plot.
- Add payoff heatmap.
- Prepare demo-friendly fixed-seed scenarios.

## Benchmarks and Tests

- Run CPU baseline across grid sizes.
- Add benchmark output schema for cells/second and frames/second.
- Add correctness comparison script.
- Record FPGA resource utilisation.
- Separate kernel, transfer, and full-loop timing.

## Documentation and Report

- Keep proposal, architecture, and MVP scope consistent.
- Add diagrams for update pipeline and system split.
- Maintain risk register.
- Prepare final report evaluation section.
- Write limitations and fallback-tier explanation.

## Integration

- Run tests before merging.
- Keep Python and RTL strategy IDs aligned.
- Freeze stretch features after Week 3.
- Record exact commit and bitstream used for demo.
