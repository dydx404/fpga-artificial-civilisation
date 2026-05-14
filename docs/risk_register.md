# Risk Register

| Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- |
| FPGA neighbour fetch is harder than expected | High | High | Start with small BRAM design or cellular automata fallback |
| DMA integration takes too long | Medium | High | Keep a simulated PYNQ interface and CPU benchmark ready |
| Python model becomes too complex for RTL | Medium | High | Freeze an MVP rule and keep extensions optional |
| Visualisation consumes too much time | Medium | Medium | Start with matplotlib and only build web/Unity after data format stabilises |
| Benchmarks overclaim speedup | Medium | High | Separate kernel, transfer, and full-loop timing |
| Team members work in isolation | Medium | High | Weekly integration checklist and shared issue backlog |
| Randomness causes Python/RTL mismatch | Medium | Medium | Disable mutation for initial correctness tests |
| Resource/trust features blow up scope | High | Medium | Keep civilisation features as Tier 4 or Tier 5 extensions |
| Bitstream/toolchain problems | Medium | High | Preserve Python-only and Verilator-only demos |

## Risk Handling Principles

- Freeze scope early when integration risk rises.
- Keep correctness tests small and deterministic.
- Use the fallback ladder as an engineering control.
- Prefer a reliable impressive subset over a fragile maximal system.

