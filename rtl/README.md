# RTL Scaffold

This directory contains the SystemVerilog starting point for the FPGA acceleration path. The modules are intentionally modest: they define interfaces, encodings, and datapath intent, but they are not a finished accelerator.

## Agent Word Format

The current scaffold uses an early 8-bit packed word:

```text
bit  [1:0] strategy
bit  [3:2] flags / reserved
bit  [5:4] energy_class
bit  [7:6] age_class
```

Early strategy encoding:

```text
0 = cooperate
1 = defect
2 = tit_for_tat placeholder
3 = random placeholder
```

The scoped proposal targets five MVP strategies, so a later hardware format will likely use a 3-bit `strategy_id` plus a `last_action` bit. Keep the early 2-bit format only for first cooperate/defect bring-up.

## Module Map

- `payoff_unit.sv`: Combinational 2x2 game payoff.
- `mutation_lfsr.sv`: 32-bit LFSR for mutation and random strategy placeholder.
- `strategy_update_unit.sv`: Best-neighbour selection plus mutation.
- `agent_update_core.sv`: Cell-local update wrapper.
- `neighbour_fetch.sv`: Placeholder for line-buffer or BRAM neighbour fetch.
- `world_buffer.sv`: Double-buffered world memory scaffold.
- `stats_reducer.sv`: Streaming statistics counter.
- `top_spatial_game_engine.sv`: Top-level compute-engine outline.

## First Implementation Target

1. Simulate `payoff_unit.sv` truth table.
2. Simulate `mutation_lfsr.sv` progression.
3. Implement deterministic cooperate/defect update with mutation disabled.
4. Compare a 3x3 or 4x4 world against the Python model.
5. Add mutation after deterministic comparison works.

## Honesty Note

Neighbour fetch, DMA wrappers, AXI-lite registers, and full frame traversal are not complete in this initial scaffold. They are the main hardware work packages for the team.
