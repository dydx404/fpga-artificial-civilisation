# Vision

The FPGA Artificial Civilisation Engine is a hardware-accelerated platform for exploring artificial societies. It should feel like a scientific instrument: configure a world, run many generations, observe emergent behaviour, compare hypotheses, and measure performance.

The project is ambitious because it combines three hard things:

- A mathematically meaningful simulation model.
- A real FPGA acceleration path.
- A compelling visual and narrative demo.

The core idea is that a society can be represented as a large field of simple agents. Each agent follows a strategy, interacts locally, accumulates payoff, and updates based on neighbours. Simple rules can generate complex global behaviour: cooperation clusters, defector invasions, cyclic recovery, inequality, social fragmentation, and stable local norms.

## Research Questions

Useful project questions include:

- When does cooperation survive in a hostile environment?
- How does mutation prevent or accelerate collapse?
- Do local neighbourhoods produce stable clusters?
- How does resource scarcity change strategy evolution?
- Which rules are cheap enough for FPGA acceleration?
- What is the speedup compared with a CPU reference model?

## Engineering Vision

The system should scale from a pure Python reference model to a Zynq FPGA prototype:

- Python defines the mathematical truth.
- RTL implements a fixed, fast subset of the update rule.
- PYNQ controls buffers, configuration, and data transfer.
- The frontend turns raw state into live heatmaps and statistics.
- Benchmarks prove what is accelerated and what is only visual polish.

## Success Criteria

A strong final project should show:

- A working simulation with visible emergent behaviour.
- Clear comparison between CPU and FPGA update throughput.
- A defensible mapping from model rules to hardware.
- Honest discussion of limitations and fallback choices.
- A polished demo that a non-specialist can understand.

