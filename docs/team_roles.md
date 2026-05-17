# Team Roles

The project is sized for six people. Each role owns a clear subsystem, but weekly integration is more important than isolated progress.

| Role | Main Responsibility | Key Deliverables |
| --- | --- | --- |
| 1. FPGA update engine | Spatial update datapath | Payoff unit, strategy decision unit, mutation hook, RTL tests |
| 2. Memory/interface/PYNQ integration | Hardware/software movement | Buffer format, DMA/control path, packed frame transfer |
| 3. Python model and theory | Reference semantics | Numpy model, payoff rules, deterministic tests, experiment configs |
| 4. Visualisation/dashboard | Demo interface | Grid viewer, payoff heatmap, cooperation/strategy plots |
| 5. Testing/benchmarking | Evidence and validation | CPU baseline, FPGA timings, correctness matrix, resource table |
| 6. Integration/project/report | Coherence and delivery | Sprint tracking, fallback decisions, report/presentation narrative |

## Integration Expectations

- Week 1: Python model, architecture, and data format agreed.
- Week 2: RTL unit tests and visualisation connected to Python output.
- Week 3: PYNQ or simulated hardware path exercised.
- Week 4: benchmark and demo candidate frozen.
- Week 5: polish, report, final demo, and fallback cleanup.

## Shared Rules

- Keep strategy encoding consistent across Python and RTL.
- Disable randomness for correctness tests.
- Do not add stretch features that change the MVP data format late.
- Prefer one reliable integrated path over several impressive disconnected parts.
