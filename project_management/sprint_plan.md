# 5-Week Sprint Plan

## Week 1: Python Model + Architecture + Simple RTL Skeleton

Goals:

- Implement Python Prisoner's Dilemma grid simulation.
- Write architecture, interface, and fallback documents.
- Create initial RTL module skeletons.
- Agree on agent encoding and strategy IDs.
- Run first unit tests.

Exit criteria:

- Python example produces plots.
- Team can explain the update rule.
- RTL owners have concrete module tasks.

## Week 2: Basic FPGA Update Core + Visualiser

Goals:

- Implement payoff unit and LFSR testbenches.
- Build or stub neighbour fetch path.
- Improve matplotlib visualiser.
- Define frame packing and PYNQ buffer format.
- Add CPU baseline benchmark.

Exit criteria:

- Payoff and LFSR simulations pass.
- Visualiser shows live or saved frames.
- CPU baseline reports cells per second.

## Week 3: DMA / Integration + Mutation + Metrics

Goals:

- Bring up PYNQ overlay loading path.
- Test DMA loopback or frame transfer.
- Integrate mutation threshold.
- Add cooperation ratio, mean payoff, entropy, and strategy counts.
- Compare small hardware outputs against Python where possible.

Exit criteria:

- Deterministic small-world correctness path exists.
- At least one integrated PS/PL or simulated-PL demo works.
- Benchmark format is stable.

## Week 4: Resources / Trust / Dynamic Features + Benchmarking

Goals:

- Add one civilisation feature only if base path is stable.
- Run CPU and FPGA benchmark matrix.
- Improve frontend and demo visuals.
- Write interim results and final report evidence.
- Decide final fallback tier.

Exit criteria:

- Demo feature set is frozen.
- Benchmark data is collected or the fallback benchmark is ready.
- Report figures are identified.

## Week 5: Polish, Report, Demo, Fallback Freeze

Goals:

- Stop feature work.
- Fix bugs and integration rough edges.
- Prepare final presentation.
- Record demo video or scripted fallback.
- Complete final report and contribution summary.

Exit criteria:

- Reproducible demo.
- Clean repository.
- Honest benchmark table.
- Every team member has documented contribution.

