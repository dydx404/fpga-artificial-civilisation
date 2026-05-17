# Fallback Plan

The fallback plan keeps the project credible even if FPGA integration is harder than expected.

| Tier | Description | Demo Value |
| --- | --- | --- |
| 0 | Python simulation and visualisation only | Shows model, spatial dynamics, plots, and theory |
| 1 | Single FPGA match/update core | Proves FPGA computes part of the update rule |
| 2 | Full grid update through FPGA | Strong hardware result with CPU comparison |
| 3 | Multiple strategies and mutation | Richer dynamics and stronger demo |
| 4 | Advanced visualisation and experiments | Better presentation and analysis |
| 5 | Graph topologies or multi-board extension | Ambitious stretch only after stable MVP |

## Freeze Guidance

- End of Week 2: freeze at Tier 1 if neighbourhood fetch is not stable.
- End of Week 3: freeze at Tier 2 if full PYNQ transfer remains unreliable.
- Mid Week 4: freeze all model features and focus on benchmarks/report.
- Week 5: no new features; only fix, measure, document, and rehearse.

## Acceptable Final Outcomes

A good final submission can be:

- Python model plus strong RTL unit demonstration.
- Single hardware update core plus host visualisation.
- Full FPGA grid update with simple strategies.
- Full MVP plus mutation and richer experiments.

The report should clearly state which tier was achieved and why.
