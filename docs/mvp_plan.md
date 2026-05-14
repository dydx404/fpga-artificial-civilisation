# MVP Plan

The MVP is a fixed-grid evolutionary Prisoner's Dilemma simulator with a Python reference model and a first FPGA datapath target.

## Simulation Rules

- 2D row-major grid.
- Moore neighbourhood with 8 neighbours.
- Agent fields: strategy, payoff, energy, age.
- Strategies: cooperate, defect, tit-for-tat placeholder, random placeholder.
- Prisoner's Dilemma payoff matrix with configurable `R`, `S`, `T`, and `P`.
- Each generation computes payoff against neighbours.
- Each agent copies the strategy of the highest-payoff neighbour if that payoff is higher than its own.
- Mutation randomly changes strategy with a configured probability.
- Age increments once per generation.
- Energy changes according to payoff gain minus living cost.

## MVP Deliverables

- Numpy simulator.
- Unit tests for payoff, update rules, and metrics.
- Matplotlib visualiser.
- CPU baseline benchmark.
- RTL skeleton with payoff unit, LFSR, update core, buffers, and stats reducer.
- PYNQ interface placeholders.
- Architecture, fallback, and demo documentation.

## Definition of Done

The MVP is done when:

- `pytest` passes for the Python model.
- The Prisoner's Dilemma example produces visible strategy evolution.
- The CPU benchmark reports cells per second and frames per second.
- RTL modules are sufficiently specified for implementation tasks.
- The team can explain how a Python cell update maps to the FPGA pipeline.

## First Experiments

Suggested experiments:

- Random 50/50 cooperate/defect world.
- Mostly cooperative world with a small defector seed.
- Mutation probability sweep from 0 to 0.05.
- Payoff matrix sweep varying temptation `T`.
- World size sweep for CPU baseline timing.

