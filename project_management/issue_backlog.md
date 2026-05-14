# Issue Backlog

This backlog is written as concrete GitHub issue seeds. Convert items into issues as the team commits to them.

## Python Model

- Implement deterministic Prisoner's Dilemma payoff truth table.
- Add Snowdrift payoff example.
- Add strategy copying from best neighbour.
- Add mutation probability sweep script.
- Add resource field prototype.
- Add replay saving and loading.
- Add fixed-seed regression tests.
- Add documentation for update order.

## RTL Compute Core

- Complete `payoff_unit.sv` truth table testbench.
- Implement strategy update unit with best-neighbour selection.
- Integrate LFSR mutation into agent update core.
- Define signed payoff width and overflow handling.
- Build 3x3 deterministic update testbench.
- Add Verilator build target.
- Add synthesis notes for PYNQ-Z1.

## Memory / DMA / PYNQ

- Decide frame packing format.
- Implement pack/unpack conversion in Python.
- Create DMA loopback notebook.
- Define AXI-lite control register map.
- Measure transfer overhead for 64x64 and 128x128 frames.
- Add buffer swap test.
- Add PYNQ dry-run mode for development without board.

## Frontend

- Build matplotlib live viewer.
- Add strategy colour palette.
- Add cooperation ratio chart.
- Add web canvas heatmap prototype.
- Define frame protocol.
- Add side-by-side CPU/FPGA display mode.
- Add demo controls for mutation and payoff.

## Benchmarks and Tests

- Implement CPU baseline CSV/JSON output.
- Add benchmark schema validation.
- Add correctness comparison for small worlds.
- Add performance matrix script.
- Add plots for cells per second.
- Add reproducibility checklist.
- Add CI workflow after repo is pushed to GitHub.

## Documentation and Report

- Expand mathematical background section.
- Add architecture diagram.
- Add risk register updates each week.
- Write proposal.
- Write interim presentation.
- Draft final report experiments section.
- Add contribution log.
- Prepare demo storyboard slides.

## Integration

- Create weekly integration branch or tag.
- Run full Python test suite before merges.
- Freeze fallback tier at planned checkpoints.
- Maintain changelog of rule changes.
- Record exact bitstream and commit hash for demos.

