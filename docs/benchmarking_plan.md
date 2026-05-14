# Benchmarking Plan

Benchmarking should answer two questions:

1. Does the FPGA compute the same update rule as the reference model?
2. Does the FPGA improve throughput once transfer overhead is included?

## Correctness Benchmarks

Use small worlds first:

- 4x4 deterministic cooperate/defect pattern.
- 8x8 random pattern with fixed seed.
- Mutation disabled.
- Fixed payoff matrix.
- Compare Python next state against RTL/PYNQ output.

Only add mutation after deterministic correctness is proven.

## CPU Baseline

Measure:

- World size.
- Number of generations.
- Total runtime.
- Cells updated per second.
- Frames per second.
- Final cooperation ratio.

The script `benchmarks/cpu_baseline.py` provides the starter baseline.

## FPGA Measurements

Measure separately:

- Host-to-device transfer time.
- FPGA kernel time.
- Device-to-host transfer time.
- Full loop time.
- Setup overhead.

This separation prevents the team from overclaiming a compute speedup that disappears when DMA is included.

## Experiment Matrix

Suggested sizes:

```text
64x64
128x128
256x256
512x512
```

Suggested generation counts:

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
0.05
```

## Reporting

Report:

- Mean of at least 3 runs.
- Standard deviation if time permits.
- Exact commit hash.
- Hardware clock frequency.
- Board and bitstream version.
- Whether visualisation was enabled.

