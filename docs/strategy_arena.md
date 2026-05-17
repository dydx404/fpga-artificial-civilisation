# Repeated Match Mode

This document preserves a possible extension: running repeated-game matches without a full spatial grid. It is useful for testing strategy logic and payoff accumulation, but it is no longer the main project framing.

## Purpose

Repeated match mode can help:

- validate strategy decision units,
- compare finite-state strategies,
- test payoff lookup and score accumulation,
- produce simple CPU/FPGA benchmarks before full grid integration.

## Relationship to the MVP

The MVP remains the spatial grid simulator. Repeated match mode is a supporting path:

```text
strategy decision + payoff lookup + score accumulation
        -> reused inside spatial update engine
```

## Candidate Strategies

- Always Cooperate.
- Always Defect.
- Tit-for-Tat.
- Random(p).
- Pavlov / Win-Stay-Lose-Shift.

## Hardware Use

A single match core can be an early hardware milestone. It should not replace the spatial update engine as the main project goal unless time forces a Tier 1 fallback.

## Outputs

- Strategy-vs-strategy score table.
- Cooperation rate.
- Round throughput.
- Correctness comparison against Python.
