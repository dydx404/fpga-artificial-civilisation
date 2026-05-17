# Benchmarking Plan

Benchmarking should answer two questions:

1. Does the FPGA compute the same update rule as the Python reference?
2. Does the FPGA improve useful update throughput once transfer overhead is included?

## Correctness First

Use deterministic small grids:

- `4x4` all cooperators.
- `4x4` single defector.
- `8x8` fixed random seed.
- Mutation and action noise disabled.
- Fixed payoff matrix.

Compare:

- next strategy grid,
- payoff totals,
- strategy counts,
- cooperation count.

## Performance Metrics

| Metric | Meaning |
| --- | --- |
| cells updated per second | Main spatial update throughput |
| game rounds per second | Useful if repeated rounds are explicitly modelled |
| frames per second | Full generations per second |
| kernel time | FPGA compute time only |
| transfer time | Host/PYNQ input/output movement |
| full-loop time | End-to-end runtime including transfer |
| resource use | LUTs, FFs, BRAM, DSPs, clock frequency |

## Experiment Matrix

Suggested grid sizes:

```text
32x32
64x64
128x128
256x256
```

Suggested step counts:

```text
100
1000
10000
```

Suggested mutation probabilities:

```text
0
0.001
0.01
```

## Reporting Rules

- State whether visualisation was enabled.
- Report mean of at least 3 runs where possible.
- Include commit hash and board/bitstream version.
- Separate CPU reference, FPGA kernel-only, and full-loop results.
- Do not claim speedup from a different rule or different grid size.
