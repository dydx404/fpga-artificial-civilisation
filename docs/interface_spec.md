# Interface Specification

This document defines the initial contract between Python, PYNQ, RTL, benchmark scripts, and visualisers. It can change, but changes should be versioned and tested.

## World Layout

The world is a 2D grid stored in row-major order:

```text
index = y * width + x
```

The MVP uses wrap-around boundaries. Hardware and Python must agree on this before correctness comparisons.

## Agent Fields

Python reference fields:

- `strategy`: unsigned 8-bit integer.
- `payoff`: 32-bit float in Python, fixed-point candidate in RTL.
- `energy`: 32-bit float in Python, quantised candidate in RTL.
- `age`: unsigned 16-bit integer in Python, quantised candidate in RTL.

MVP RTL packed agent word:

```text
bit  [1:0] strategy
bit  [3:2] flags / reserved
bit  [5:4] energy_class
bit  [7:6] age_class
```

The packed word is intentionally small for the first hardware version. Python keeps richer state and can quantise only the fields used by the FPGA.

## Strategy Encoding

```text
0 = cooperate
1 = defect
2 = tit_for_tat placeholder
3 = random placeholder
```

The MVP RTL may initially support only `0` and `1`. Python supports all four so the higher-level model can grow.

## Payoff Matrix

For a 2x2 game:

```text
                 opponent cooperates    opponent defects
self cooperates          R                    S
self defects             T                    P
```

Prisoner's Dilemma default:

```text
R = 3
S = 0
T = 5
P = 1
```

## Frame Transfer

Initial frame format:

```text
uint8 agent_words[height][width]
```

Possible future frame format:

```text
header:
  uint16 width
  uint16 height
  uint32 generation
payload:
  uint8 agent_words[height * width]
metrics:
  uint32 strategy_counts[4]
  int64 payoff_sum_q
```

## Control Registers

Candidate AXI-lite registers:

```text
0x00 control        bit 0 start, bit 1 reset, bit 2 swap_buffers
0x04 status         bit 0 busy, bit 1 done, bit 2 error
0x08 width
0x0C height
0x10 mutation_threshold
0x14 payoff_R
0x18 payoff_S
0x1C payoff_T
0x20 payoff_P
0x24 generation_count
```

The exact map depends on the final IP wrapper.

## Visualisation Protocol

Early visualisers can read local files. Later network messages should use:

```json
{
  "type": "frame",
  "generation": 42,
  "width": 128,
  "height": 128,
  "strategy_counts": {"cooperate": 7000, "defect": 9000},
  "cooperation_ratio": 0.4375
}
```

Binary frame transport can be added after JSON metadata is stable.

