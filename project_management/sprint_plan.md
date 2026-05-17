# 5-Week Sprint Plan

## Week 1: Model, Scope, and Data Format

Goals:

- Finalise MVP rule and strategy encoding.
- Confirm Python reference model runs and is documented.
- Define packed agent word and frame layout.
- Write tiny-grid correctness cases.

Exit criteria:

- Python tests pass.
- Architecture and MVP docs match the intended build.
- RTL owners know the update-core interface.

## Week 2: RTL Units and Visualisation

Goals:

- Implement or refine payoff unit, LFSR, and strategy decision skeletons.
- Build RTL unit testbenches.
- Improve Python/matplotlib visualisation.
- Run CPU baseline.

Exit criteria:

- Payoff/LFSR tests pass where tools are available.
- Visualiser shows repeatable spatial evolution.
- CPU baseline reports cells per second.

## Week 3: PYNQ / Hardware Path

Goals:

- Bring up overlay/control workflow or simulated hardware path.
- Transfer packed frames.
- Run one hardware update core or one generation path.
- Compare deterministic output against Python.

Exit criteria:

- At least Tier 1 fallback is achieved.
- Timing can separate transfer and compute.

## Week 4: Integration and Benchmarking

Goals:

- Freeze model features.
- Run benchmark matrix.
- Add mutation or extra strategies only if the base path is stable.
- Prepare report figures and demo script.

Exit criteria:

- Demo feature set is frozen.
- Benchmark table is credible.
- Fallback tier is known.

## Week 5: Polish and Report

Goals:

- Stop feature work.
- Fix integration bugs.
- Rehearse demo.
- Complete final report and presentation.

Exit criteria:

- Reproducible demo.
- Honest benchmark data.
- Clear contribution summary.
