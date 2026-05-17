# Exploratory Game Theory Platform

Also called the **User-Programmable Strategy Arena**, this is an extension direction for the project after the basic spatial grid simulator is stable.

The idea is to turn the simulator into a small experimental lab:

- define simple strategies safely,
- run them against each other,
- place them into a spatial grid,
- watch which strategies invade, survive, or collapse,
- export frames or video of the dynamics.

This is still not a "simulate society" project. It is a tool for exploring local strategic interaction and spatial evolution.

## Why This Is Useful

The current MVP can show fixed strategies spreading on a grid. The exploratory platform would let users ask their own questions:

- What happens if a forgiving strategy is added?
- How much noise breaks Tit-for-Tat?
- Can an aggressive strategy invade a cooperative region?
- Which strategies survive near borders?
- Does mutation create stable diversity or chaos?

That makes the project feel less like a scripted visualiser and more like a real experimental platform.

## Two Modes

| Mode | What It Does | Why It Helps |
| --- | --- | --- |
| Arena mode | User strategies compete in repeated games | Fast comparison and ranking |
| Spatial mode | Strategies live on a grid and reproduce locally | Visual invasion/evolution dynamics |

The two modes share the same safe strategy representation.

## Arena Mode

User-submitted strategies can compete in games such as:

- Prisoner's Dilemma.
- Hawk-Dove / Snowdrift.
- Stag Hunt.
- Owner-Intruder.
- Custom 2x2 payoff matrix.

Useful metrics:

- total score,
- cooperation rate,
- exploitability,
- robustness under noise,
- performance against fixed benchmark strategies,
- tournament ranking,
- population share after evolution.

The goal is not to "solve" game theory. The goal is to make the behaviour visible and measurable.

## Spatial Mode

Spatial mode answers a different question:

> If strategies occupy territory, which ones spread?

The visual results can be very demo-friendly:

- defectors invade naive cooperators,
- retaliators resist defectors,
- forgiving strategies survive noise better,
- aggressive strategies form waves,
- territorial rules stabilise borders.

## Safe Strategy Definitions

Users should not upload arbitrary Python, Verilog, or shell scripts. Instead, strategies should be written in a tiny rule format that compiles into finite-state-machine lookup tables.

High-level pipeline:

```text
User strategy definition
  -> parser / validator
  -> finite-state-machine representation
  -> enumerate input combinations
  -> emit packed lookup table
  -> CPU writes LUT to FPGA BRAM/registers
  -> FPGA executes strategy transitions
```

This keeps the system:

- safe,
- deterministic,
- hardware-compatible,
- easy to test,
- easy to explain.

## FPGA / CPU Split

| Component | Responsibility |
| --- | --- |
| CPU / Host | UI, parsing, validation, LUT generation, video export, data logging |
| PYNQ PS | Write strategy LUTs, configure games, move frames/results |
| FPGA PL | Repeated match core, payoff lookup, strategy LUT execution, spatial update, mutation LFSR, statistics reduction |

The FPGA executes compact lookup tables. It does not execute arbitrary user code.

## Benchmarks

The platform should still be measured like an engineering system:

- CPU-only Python reference for correctness.
- Optional CPU-only C/C++ reference for speed comparison.
- FPGA kernel timing for match/spatial updates.
- Full-loop timing including frame and result transfer.
- Strategy throughput, grid cells per second, and frames per second.

The goal is to show where hardware acceleration helps, not to hide transfer or setup costs.

## Roadmap

1. Keep the fixed-strategy MVP working.
2. Add a CPU-side strategy compiler prototype.
3. Run compiled strategies in the Python reference model.
4. Map compiled strategy LUTs into a simple hardware lookup format.
5. Add arena ranking and benchmark strategies.
6. Feed arena-tested strategies into the spatial grid.
7. Export evolution frames/video for demos and reports.

## Demo Story

The strongest demo would be:

1. User writes or selects a strategy.
2. System validates it.
3. Strategy enters the arena.
4. Leaderboard shows how it performs.
5. Strategy is dropped into a grid.
6. We watch invasion waves or stable borders form.
7. The run exports frames and an `evolution.mp4`.

That is concrete, visual, and still technically grounded.
