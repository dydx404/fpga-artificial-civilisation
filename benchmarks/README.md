# Benchmarks

Benchmarking exists to keep performance claims honest.

The first script, `cpu_baseline.py`, measures the Numpy reference model. FPGA benchmarks should later report both kernel-only and full-loop timings so DMA overhead is visible.

## CPU Baseline

```bash
python benchmarks/cpu_baseline.py --width 256 --height 256 --steps 1000 --output outputs/cpu_baseline.json
```

## Metrics

Use `metrics_schema.json` as the stable shape for benchmark outputs. Add fields rather than changing names when possible.

