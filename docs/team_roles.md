# Team Roles

The project is designed for a 6-person team. Each person owns a subsystem, but the project only succeeds if integration happens early and often.

## 1. FPGA Compute Core

Owns:

- Payoff unit.
- Agent update core.
- Strategy update logic.
- Mutation LFSR integration.
- RTL testbenches for core logic.

Main risk: pipeline complexity and matching Python semantics.

## 2. Memory / DMA / Interfaces

Owns:

- World buffer design.
- Frame packing format.
- AXI-stream or AXI-lite interface plan.
- PYNQ DMA experiments.
- Hardware/software data transfer tests.

Main risk: transfer overhead dominating compute speed.

## 3. Python Reference Model and Theory

Owns:

- Numpy simulation.
- Payoff matrices.
- Update rules.
- Scientific assumptions.
- Experiment scripts and correctness reference.

Main risk: model becoming too complex for the hardware team to follow.

## 4. Frontend Visualisation

Owns:

- Matplotlib viewer first.
- Web or Unity viewer later.
- Heatmaps and live statistics.
- Demo presentation visuals.
- Frontend protocol with integration owner.

Main risk: building a pretty interface before the data path is stable.

## 5. Benchmarking and Testing

Owns:

- CPU baseline.
- Correctness tests.
- FPGA benchmark methodology.
- Metrics schema.
- Regression checks and reproducibility.

Main risk: measuring the wrong thing or comparing different rules.

## 6. Integration / Project Management / Report

Owns:

- Sprint board.
- Weekly integration checklist.
- Fallback decision points.
- Report structure.
- Demo script and final narrative.

Main risk: subsystems working separately but not together.

## Weekly Integration Rule

Every week should end with one integrated artifact:

- Week 1: Python model and architecture review.
- Week 2: visualiser connected to model, RTL modules reviewed.
- Week 3: PYNQ or simulated hardware interface exercised.
- Week 4: benchmark and demo candidate.
- Week 5: frozen demo and final report evidence.

