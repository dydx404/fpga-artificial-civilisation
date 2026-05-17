# Risk Register

| Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- |
| Neighbour fetch is harder than expected | High | High | Start with small BRAM/tile design and tiny-grid tests |
| DMA/PYNQ integration takes too long | Medium | High | Keep a Python-only and RTL-simulation fallback |
| Python and RTL semantics diverge | Medium | High | Disable mutation first; compare one generation on small grids |
| Scope expands into unrealistic agent behaviour | High | Medium | Freeze MVP strategies and defer extensions |
| Visualisation consumes too much time | Medium | Medium | Use matplotlib first; web dashboard only after data path works |
| Benchmarks overclaim speedup | Medium | High | Report transfer time, compute time, and full-loop time separately |
| Randomness makes testing difficult | Medium | Medium | Use fixed seeds and deterministic mutation-disabled tests |
| Toolchain/bitstream problems | Medium | High | Preserve Python demo and module-level RTL tests |
| Team works in disconnected streams | Medium | High | Weekly integration checklist and shared issue backlog |

## Fallback Tiers

| Tier | Deliverable |
| --- | --- |
| 0 | Python simulation and visualisation only |
| 1 | Single FPGA match/update core |
| 2 | Full grid update through FPGA |
| 3 | Multiple strategies and mutation |
| 4 | Advanced visualisation and experiments |
| 5 | Graph topologies or multi-board extension |

## Risk Handling Principles

- Freeze scope early when integration risk rises.
- Keep correctness tests small and deterministic.
- Treat transfer overhead as part of the result, not an inconvenience.
- Prefer a reliable scoped demo over unstable stretch features.
