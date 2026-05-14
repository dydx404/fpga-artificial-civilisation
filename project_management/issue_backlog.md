# Issue Backlog

This backlog is written as concrete GitHub issue seeds. Convert items into issues as the team commits to them.

## Python Model

- Design high-level Strategy Arena experiment config.
- Implement Python repeated-game tournament simulator.
- Add strategy catalogue for cooperate, defect, tit-for-tat variants, random, Pavlov, and Grudger.
- Add tournament leaderboard and payoff matrix output.
- Add noise and round-count sweeps for repeated games.
- Implement deterministic Prisoner's Dilemma payoff truth table.
- Add Snowdrift payoff example.
- Add strategy copying from best neighbour.
- Add mutation probability sweep script.
- Add resource field prototype.
- Add replay saving and loading.
- Add fixed-seed regression tests.
- Add documentation for update order.

## RTL Compute Core

- Define high-level interface for repeated match core.
- Prototype single repeated Prisoner's Dilemma match core.
- Define match result record format.
- Plan many-core tournament sharding architecture.
- Complete `payoff_unit.sv` truth table testbench.
- Implement strategy update unit with best-neighbour selection.
- Integrate LFSR mutation into agent update core.
- Define signed payoff width and overflow handling.
- Build 3x3 deterministic update testbench.
- Add Verilator build target.
- Add synthesis notes for PYNQ-Z1.

## Memory / DMA / PYNQ

- Define arena configuration packet format.
- Define match result transfer format.
- Plan host-to-multiple-board assignment protocol.
- Decide frame packing format.
- Implement pack/unpack conversion in Python.
- Create DMA loopback notebook.
- Define AXI-lite control register map.
- Measure transfer overhead for 64x64 and 128x128 frames.
- Add buffer swap test.
- Add PYNQ dry-run mode for development without board.

## Frontend

- Design Strategy Colosseum dashboard.
- Add leaderboard view.
- Add strategy-vs-strategy payoff matrix view.
- Add exploitability / robustness panel.
- Add tournament replay concept.
- Build matplotlib live viewer.
- Add strategy colour palette.
- Add cooperation ratio chart.
- Add web canvas heatmap prototype.
- Define frame protocol.
- Add side-by-side CPU/FPGA display mode.
- Add demo controls for mutation and payoff.

## Benchmarks and Tests

- Define arena metrics: rounds per second and matches per second.
- Add CPU repeated-tournament baseline.
- Add correctness checks for fixed strategy matchups.
- Add benchmark plan for single-core and many-core FPGA match engines.
- Implement CPU baseline CSV/JSON output.
- Add benchmark schema validation.
- Add correctness comparison for small worlds.
- Add performance matrix script.
- Add plots for cells per second.
- Add reproducibility checklist.
- Add CI workflow after repo is pushed to GitHub.

## Documentation and Report

- Add Strategy Arena project framing.
- Add multi-board architecture options.
- Compare arena MVP versus spatial civilisation extension.
- Expand mathematical background section.
- Add architecture diagram.
- Add risk register updates each week.
- Write proposal.
- Write interim presentation.
- Draft final report experiments section.
- Add contribution log.
- Prepare demo storyboard slides.

## Integration

- Decide whether current sprint target is arena-first or spatial-first.
- Define shared strategy encoding across arena and civilisation modes.
- Define handoff from arena winners to spatial civilisation experiments.
- Identify whether multi-board demo uses real boards or simulated board workers.
- Create weekly integration branch or tag.
- Run full Python test suite before merges.
- Freeze fallback tier at planned checkpoints.
- Maintain changelog of rule changes.
- Record exact bitstream and commit hash for demos.
