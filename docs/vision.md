# Vision

The FPGA Artificial Civilisation Engine is evolving into a broader hardware-accelerated game-theory laboratory. The project now has two connected modes:

- Strategy Arena / Strategy Colosseum: repeated-game tournaments between long-horizon strategies.
- Artificial Civilisation / Spatial Evolution: strategies live inside a 2D world where local interaction creates emergent social behaviour.

Together, these modes support a first-place-level narrative: build a distributed FPGA-accelerated laboratory for testing long-horizon strategic behaviour, emergent cooperation, betrayal, adaptation, and social evolution.

The project is ambitious because it combines three hard things:

- A mathematically meaningful simulation model.
- A real FPGA acceleration path.
- A compelling visual and narrative demo.

The core idea is that strategies can be studied at two scales. In the Strategy Arena, strategies compete directly in repeated games and produce measurable rankings, payoff matrices, exploitability scores, and robustness curves. In the Artificial Civilisation mode, those strategies become agents in a spatial world, where local interactions produce cooperation clusters, betrayal waves, collapse, recovery, inequality, alliances, and stable local norms.

## Research Questions

Useful project questions include:

- Which long-game strategies survive repeated interaction?
- Which strategies exploit naive opponents, and which remain robust under noise?
- How do mutation and selection change a strategy population over time?
- When does cooperation survive in a hostile environment?
- How does mutation prevent or accelerate collapse?
- Do local neighbourhoods produce stable clusters?
- How does resource scarcity change strategy evolution?
- Which repeated-game kernels are cheap enough for FPGA acceleration?
- What is the speedup compared with a CPU reference model?

## Engineering Vision

The system should scale from a pure Python reference model to a Zynq FPGA prototype:

- Python defines the mathematical truth for tournaments and spatial worlds.
- RTL implements fixed, fast subsets of the repeated match and spatial update rules.
- PYNQ controls strategy/game configuration, buffers, DMA, and result transfer.
- The frontend turns match results, leaderboards, and world state into live dashboards.
- Benchmarks prove what is accelerated and what remains software orchestration.

## Two-Mode Roadmap

Strategy Arena is the clearer MVP because it is measurable:

- Repeated Prisoner's Dilemma tournament.
- Fixed strategy set.
- Score accumulation and leaderboard.
- CPU versus FPGA match throughput.
- Parallel match cores as the natural scaling story.

Artificial Civilisation is the more visually impressive extension:

- Strategies become agents on a grid.
- Agents interact with neighbours.
- Cooperation clusters, collapse, recovery, and resource pressure emerge.
- The arena can evolve strategies before placing them into spatial worlds.

## Distributed Vision

If multiple PYNQ-Z1 boards are available, each board can become one arena shard, civilisation region, or strategy league participant. The host controller distributes configurations, boards run accelerated simulations locally, and the host aggregates leaderboards, payoff matrices, and global visualisations.

## Success Criteria

A strong final project should show:

- A working tournament or spatial simulation with visible strategic behaviour.
- Clear comparison between CPU and FPGA match/update throughput.
- A defensible mapping from repeated-game rules to hardware.
- Honest discussion of limitations and fallback choices.
- A polished dashboard/demo that a non-specialist can understand.
