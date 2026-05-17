# Numerical Representation

The Python model uses convenient numeric types. The FPGA design needs compact fixed-width fields. This document records the planned mapping.

## Python Reference Types

- Strategy: `uint8`.
- Payoff: `float32`.
- Energy: `float32`.
- Age: `uint16`.

Python should prioritise clarity and correctness. It is the reference, not the hardware implementation language.

## RTL Agent Word

The existing scaffold starts with a 2-bit strategy field:

```text
bit  [1:0] strategy
bit  [3:2] flags / reserved
bit  [5:4] energy_class
bit  [7:6] age_class
```

The project MVP wants five strategies, so the proposed target format is:

```text
bit  [2:0] strategy_id
bit  [3]   last_action
bit  [5:4] flags / reserved
bit  [7:6] age_class / reserved
```

This still fits in one byte while leaving a bit for simple strategy memory.

## Payoff Width

Candidate fixed-point/integer payoff:

- Signed 16-bit integer for per-cell accumulated payoff.
- Payoff constants represented as signed 8-bit or 16-bit values.
- Accumulated Moore payoff range must allow 8 neighbour interactions.

For default Prisoner's Dilemma with `T = 5`, max accumulated payoff is `8 * 5 = 40`, so 16 bits is safe.

## Mutation Threshold

A hardware LFSR can produce a 16-bit random value. Mutation probability can be represented as:

```text
mutation happens if random_u16 < mutation_threshold
```

Examples:

```text
0.001 -> 65
0.01  -> 655
0.05  -> 3276
```

## Quantisation Risks

Quantisation can change behaviour:

- Small payoff differences may disappear.
- Energy thresholds may produce artificial synchronisation.
- LFSR randomness may introduce repeatable spatial patterns if seeded poorly.
- Python and RTL may diverge if random strategy actions are not specified carefully.

The first FPGA version should minimise these risks by focusing on integer Prisoner's Dilemma with cooperate/defect strategies.
