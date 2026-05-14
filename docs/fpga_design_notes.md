# FPGA Design Notes

The RTL in this repository is a scaffold. It is intended to guide implementation, review, and test planning. It is not yet a complete accelerator.

## Compact Agent Word

The current scaffold assumes:

```text
bit  [1:0] strategy
bit  [3:2] flags / reserved
bit  [5:4] energy_class
bit  [7:6] age_class
```

The first working hardware path may ignore energy and age, preserving those bits during update.

## Datapath

Planned stages:

1. Read current cell.
2. Fetch eight neighbours.
3. Decode strategy actions.
4. Accumulate payoff.
5. Compare neighbour fitness.
6. Select next strategy.
7. Apply mutation.
8. Pack next agent word.
9. Emit statistics.

## Neighbour Fetch

Neighbour fetch is likely the hardest part of the hardware MVP. Options:

- BRAM random reads: easier to reason about, lower throughput.
- Line buffers: higher throughput, more complex boundary handling.
- Tile buffers with halo: necessary for large worlds and multi-region extension.

Start with correctness. Optimise only after the rule is stable.

## Test Strategy

Suggested RTL tests:

- Payoff truth table.
- LFSR non-zero progression.
- Strategy update chooses best neighbour.
- Mutation threshold forces mutation when set high.
- Small 3x3 world compared against Python.
- Frame boundary buffer swap.

## Timing Strategy

Do not chase one-cell-per-cycle before the algorithm is verified. A multi-cycle core can still demonstrate hardware acceleration if the world is large enough and transfer overhead is measured honestly.

## Integration Notes

- Keep Python and RTL strategy encodings identical.
- Keep payoff constants signed.
- Log exact seeds for reproducibility.
- Compare small worlds before large benchmarks.
- Separate kernel runtime from DMA transfer time in benchmarks.

