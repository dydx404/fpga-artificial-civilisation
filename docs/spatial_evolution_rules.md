# Spatial Evolution Rules

This document explains how strategies spread across the grid in spatial mode.

## Basic Generation Loop

Each generation:

1. Agents play games with neighbours.
2. Each agent accumulates payoff/fitness.
3. Each cell compares local fitness.
4. The cell copies the best neighbour if that neighbour did better.
5. Optional mutation changes the copied strategy.
6. Buffers swap.

The recommended MVP rule is:

```text
next_strategy[x, y] =
    strategy of argmax fitness in Moore neighbourhood around (x, y)
```

Usually the comparison includes the centre cell too, so a cell can keep its own strategy if it is still best.

## Why This Creates Invasion Waves

The rule is local, but the effects can spread:

- A high-scoring strategy at one border cell gets copied by neighbours.
- Those neighbours may then score well and be copied again.
- Over many generations, the strategy expands like a wave.

This is how we can see invasion dynamics.

## Example Behaviours

| Pattern | Why It Can Happen |
| --- | --- |
| Defectors invade naive cooperators | Defectors exploit cooperators at the boundary |
| Retaliators resist defectors | Tit-for-Tat-like strategies punish repeated defection |
| Forgiving strategies survive noise | They recover after accidental defection |
| Aggressive strategies collapse | They may do badly once surrounded by similar agents |
| Borders stabilise | Owner-intruder or territorial rules can reward holding regions |

## Mutation

Mutation keeps the system from freezing completely.

Simple mutation rule:

```text
with probability p:
    next_strategy = random_strategy()
```

Use mutation carefully:

- disable it for correctness tests,
- use fixed seeds for reproducible demos,
- start with very low probabilities.

## Alternative Selection Rules

These are stretch goals:

| Rule | Meaning |
| --- | --- |
| Death-birth | A cell is cleared, then neighbours compete to fill it |
| Tournament selection | Random subset of neighbours compete |
| Softmax selection | Better neighbours are more likely, not guaranteed |
| Probabilistic imitation | Copy chance depends on payoff difference |
| Asynchronous update | Cells update in random order rather than synchronously |

The MVP should use deterministic best-neighbour copying first.

## Hardware Mapping

Spatial evolution needs:

- current strategy/state grid,
- payoff or fitness values,
- neighbourhood fetch,
- max/argmax comparison,
- mutation LFSR,
- next-state write buffer.

The update is FPGA-friendly because every cell follows the same pattern.
