# Interface Specification

This document defines the initial contract between Python, PYNQ, RTL, benchmark scripts, and visualisers.

## World Layout

The world is a 2D grid stored in row-major order:

```text
index = y * width + x
```

The MVP uses wrap-around boundaries unless a test explicitly disables wrapping.

## Agent State

Python reference fields:

- `strategy`: unsigned 8-bit integer.
- `last_action`: cooperate/defect action from the previous round.
- `payoff`: 32-bit float in Python, fixed-width integer candidate in RTL.
- `age`: optional unsigned counter for experiments/debugging.

MVP RTL packed agent word candidate:

```text
bit  [2:0] strategy_id
bit  [3]   last_action
bit  [5:4] flags / reserved
bit  [7:6] age_class / reserved
```

The first hardware version may use only `strategy_id` and preserve the other bits.

## Strategy Encoding

```text
0 = Always Cooperate
1 = Always Defect
2 = Tit-for-Tat
3 = Random(p)
4 = Pavlov / Win-Stay-Lose-Shift
```

The first RTL milestone may support only strategies `0` and `1`, then add stateful strategies incrementally.

## Game Parameters

For a 2x2 payoff matrix:

```text
                 neighbour cooperates    neighbour defects
agent cooperates          R                    S
agent defects             T                    P
```

Default Prisoner's Dilemma:

```text
R = 3
S = 0
T = 5
P = 1
```

Other configuration:

- `mutation_threshold`
- `neighbourhood_type`
- `grid_width`
- `grid_height`
- `step_count`
- `initial_seed`

## Frame Transfer

Initial frame format:

```text
uint8 agent_words[height][width]
```

Metrics payload:

```text
uint32 strategy_counts[N_STRATEGIES]
uint32 cooperation_count
int64  payoff_sum_q
uint32 generation
```

## Candidate Control Registers

```text
0x00 control        bit 0 start, bit 1 reset
0x04 status         bit 0 busy, bit 1 done, bit 2 error
0x08 width
0x0C height
0x10 mutation_threshold
0x14 payoff_R
0x18 payoff_S
0x1C payoff_T
0x20 payoff_P
0x24 generation_count
0x28 neighbourhood_type
```

The exact map depends on the final IP wrapper.

## Visualisation Metadata

```json
{
  "type": "frame",
  "generation": 42,
  "width": 128,
  "height": 128,
  "strategy_counts": {
    "cooperate": 7000,
    "defect": 9000
  },
  "cooperation_ratio": 0.4375,
  "mean_payoff": 12.4
}
```
