# PYNQ Integration

This directory contains the planned control layer for a PYNQ-Z1 / Zynq deployment.

The code is currently board-aware but safe to import without PYNQ installed. Use dry-run mode on a laptop, then replace placeholders as the bitstream and DMA design mature.

## Planned Responsibilities

- Load the FPGA overlay.
- Allocate contiguous DMA buffers.
- Pack and unpack agent frames.
- Configure mutation threshold and payoff registers.
- Run generations on the programmable logic.
- Stream frames or metrics to the host frontend.

## Bring-Up Order

1. Confirm board boots and PYNQ imports.
2. Load a trivial overlay.
3. Run DMA loopback.
4. Transfer one packed world frame.
5. Compare one deterministic FPGA update against Python.
6. Add mutation and statistics.

## Notebooks

- `notebooks/bringup.ipynb`: overlay loading and basic register checks.
- `notebooks/dma_test.ipynb`: DMA buffer transfer outline.

