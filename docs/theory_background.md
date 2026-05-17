# Theory Background

This project uses a small amount of evolutionary game theory and cellular automata theory. The goal is not to conduct original theory research; the goal is to choose rules that are simple, explainable, and FPGA-friendly.

## Repeated Prisoner's Dilemma

Prisoner's Dilemma is a two-action game:

| | Neighbour Cooperates | Neighbour Defects |
| --- | ---: | ---: |
| Agent Cooperates | R | S |
| Agent Defects | T | P |

Typical ordering:

```text
T > R > P > S
```

The immediate incentive is to defect, but repeated and spatial interaction can allow cooperation to survive.

## Spatial / Network Reciprocity

In a well-mixed population, every strategy can meet every other strategy. In a spatial grid, agents only interact locally. This can change behaviour:

- Cooperators can support nearby cooperators.
- Defectors can exploit local clusters but may become isolated.
- Boundaries between strategy regions can move over time.
- Mutation/noise can seed new clusters.

This is the main visual and mathematical reason for using a grid.

## Cellular Automata Connection

The simulator resembles a cellular automaton:

- Each cell has a compact state.
- Each update depends on local neighbours.
- Updates can be synchronous.
- Simple local rules can produce complex global patterns.

The FPGA mapping is similar to stencil or neighbourhood processing.

## Bounded Strategies

The MVP strategies are intentionally simple finite-state rules:

| Strategy | Behaviour |
| --- | --- |
| Always Cooperate | Always plays cooperate |
| Always Defect | Always plays defect |
| Tit-for-Tat | Starts cooperating, then mirrors previous neighbour action |
| Random(p) | Cooperates with probability `p` |
| Pavlov | Repeats action after good outcome, switches after poor outcome |

These are enough to demonstrate memory, exploitation, forgiveness, randomness, and adaptation without requiring ML.

## Why Not Complex AI?

Large learned agents would add training, data, numerical stability, and debugging risks. A second-year FPGA project benefits more from:

- clear state encoding,
- deterministic tests,
- simple hardware units,
- measurable speedup,
- visible emergent patterns.
