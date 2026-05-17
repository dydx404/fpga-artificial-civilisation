# MVP Plan

Use [mvp_scope.md](mvp_scope.md) as the authoritative scope document. This page gives the implementation sequence.

## Phase 1: Reference Model

- Fix strategy IDs and payoff matrix.
- Implement or confirm Python grid update semantics.
- Add deterministic tiny-grid tests.
- Produce initial visual frames and metrics.

Exit criteria:

- Python tests pass.
- A fixed-seed example produces repeatable output.
- The update rule is documented clearly enough for RTL work.

## Phase 2: Hardware-Compatible Data Path

- Define packed agent word.
- Define current/next buffer layout.
- Define mutation threshold representation.
- Implement or refine payoff and strategy units in RTL.
- Build simple testbenches for payoff and LFSR.

Exit criteria:

- Hardware modules have stable interfaces.
- Small examples can be manually compared with Python.

## Phase 3: FPGA / PYNQ Integration

- Move one frame into the hardware path.
- Run one generation or one update core invocation.
- Return next state and statistics.
- Compare with Python for mutation-disabled cases.

Exit criteria:

- Hardware performs a real update computation.
- Transfer and compute timing can be measured separately.

## Phase 4: Demo and Benchmark

- Run a larger grid.
- Visualise strategy and payoff evolution.
- Measure CPU reference and FPGA implementation.
- Report resource utilisation and fallback tier.

Exit criteria:

- Demo is reproducible.
- Benchmark table is honest about transfer overhead.
- The report explains limitations and next steps.
