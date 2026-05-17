# Strategy DSL and Compiler

This document describes a proposed safe strategy definition system. It is not implemented yet.

The goal is to let users define strategies without allowing arbitrary code execution.

## Core Idea

Users write small finite-state strategies. The CPU validates them and compiles them into lookup tables. The FPGA reads those tables during simulation.

```text
User strategy definition
  -> parser / validator
  -> finite-state-machine representation
  -> enumerate input combinations
  -> emit packed lookup table
  -> CPU writes LUT to FPGA BRAM/registers
  -> FPGA arena executes strategy transitions
```

## Example DSL

```text
strategy ForgivingTitForTat {
  state calm {
    play C
    if opp_last == D goto punish
  }

  state punish {
    play D
    if opp_last == C goto calm
  }
}
```

This reads like a tiny state machine:

- in `calm`, cooperate unless the opponent defected,
- in `punish`, defect for a while,
- return to `calm` when the opponent cooperates.

## Alternative JSON/YAML Shape

A beginner-friendly UI could generate JSON instead of asking users to type a language:

```json
{
  "name": "ForgivingTitForTat",
  "initial_state": "calm",
  "states": {
    "calm": {
      "play": "C",
      "transitions": [
        {"if": {"opp_last": "D"}, "goto": "punish"}
      ]
    },
    "punish": {
      "play": "D",
      "transitions": [
        {"if": {"opp_last": "C"}, "goto": "calm"}
      ]
    }
  }
}
```

The important part is not the exact syntax. The important part is that the strategy is bounded and compilable.

## Lookup Table Representation

The compiler can enumerate all possible input combinations and emit a table:

```text
address = {strategy_id, current_state, input_flags}
data    = {next_state, action}
```

Possible input flags:

- `my_last`
- `opp_last`
- `round_is_first`
- `score_relation`
- `random_bit` / noise flag
- optional short memory flags

Outputs:

- action: cooperate or defect,
- next state.

The FPGA then does a simple table read instead of interpreting user code.

## Example Hardware View

```text
strategy_id = 5
current_state = 2
input_flags = 0b01011

lookup_address = concat(strategy_id, current_state, input_flags)
lookup_data = strategy_lut[lookup_address]

next_state = lookup_data.state
action = lookup_data.action
```

## Constraints

Recommended limits:

- max 8 states per strategy,
- max 16 or 32 strategies loaded at once,
- bounded memory only,
- fixed input flag set,
- fixed output fields,
- no loops,
- no recursion,
- no file access,
- no networking,
- no arbitrary arithmetic,
- no arbitrary executable code.

These constraints are a feature, not a weakness. They make strategies safe and FPGA-compatible.

## Validation Rules

The parser/validator should check:

- every `goto` target exists,
- every strategy has an initial state,
- state count is within limits,
- outputs are only `C` or `D`,
- conditions use allowed input flags,
- no unreachable or duplicate state names if we want friendly warnings.

## CPU / FPGA Responsibilities

| Layer | Work |
| --- | --- |
| CPU parser | Read DSL or JSON/YAML |
| CPU validator | Enforce safety and size limits |
| CPU compiler | Generate strategy LUT |
| PYNQ runtime | Write LUT to FPGA memory/registers |
| FPGA | Execute table lookup every strategy decision |

## Why This Is Better Than Arbitrary Code

Arbitrary Python or Verilog would be unsafe, hard to test, and impossible to compile quickly during a demo.

The LUT approach is:

- safe,
- explainable,
- deterministic,
- fast,
- compatible with FPGA BRAM/register storage.
