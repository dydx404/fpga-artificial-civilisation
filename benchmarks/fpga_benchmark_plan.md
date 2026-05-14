# FPGA Benchmark Plan

## Measurement Modes

Measure three modes separately:

- Kernel only: cycles or hardware timer for update engine.
- Transfer only: DMA send and receive without computation.
- Full loop: host setup, transfer, compute, receive, and metric extraction.

## Correctness Before Speed

Initial benchmark worlds:

- 4x4 all cooperators.
- 4x4 single defector.
- 8x8 fixed random seed.

Run mutation disabled first. Compare exact strategy frames against Python.

## Throughput Metrics

Report:

- Clock frequency.
- World size.
- Generations.
- Cells updated per second.
- Frames per second.
- DMA bandwidth.
- FPGA resource utilisation.
- Power estimate if available.

## Result Table Template

| Backend | Size | Steps | Kernel ms | Transfer ms | Full ms | Cells/s | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| CPU Numpy | 128x128 | 1000 | n/a | n/a | TBD | TBD | reference |
| FPGA kernel | 128x128 | 1000 | TBD | excluded | TBD | TBD | deterministic |
| FPGA full loop | 128x128 | 1000 | TBD | included | TBD | TBD | DMA included |

