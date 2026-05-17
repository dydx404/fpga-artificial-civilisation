# MVP Scope

The MVP must be small enough to finish in about 35 days and strong enough to justify FPGA acceleration.

## In Scope

| Component | MVP Decision |
| --- | --- |
| World | 2D rectangular grid |
| Neighbourhood | Moore or Von Neumann, selected at configuration time |
| Game | Repeated Prisoner's Dilemma |
| Strategies | Cooperate, defect, tit-for-tat, random(p), Pavlov |
| Update | Accumulate payoff, imitate strongest neighbour |
| Randomness | Optional mutation/noise using fixed seed |
| Reference | Numpy/Python model |
| Hardware | One spatial update engine or repeated-game update core |
| Visualisation | Grid heatmap, payoff heatmap, population plots |
| Benchmark | CPU vs FPGA cells/second and correctness |

## Out of Scope for MVP

- Realistic society/economics modelling.
- Human-like agent reasoning.
- Neural-network training.
- Large datasets.
- Complex resource markets.
- Fully asynchronous distributed simulation.
- Multi-board execution unless the single-board path is stable.

## MVP Update Rule

```text
for each generation:
  for each cell:
    fetch local neighbours
    play repeated game with neighbours
    accumulate payoff
    select best-performing local strategy
    optionally mutate
    write next state into next buffer
  swap current and next buffers
```

## Minimum Demo

- Run a fixed-seed 64x64 or 128x128 grid.
- Show the strategy map changing over time.
- Plot cooperation ratio and strategy distribution.
- Run a CPU baseline.
- Run either a hardware update core or a simulated hardware-compatible pipeline.
- Explain fallback tier honestly if full FPGA integration is incomplete.

## Stop Conditions

Freeze scope when:

- Python and hardware semantics diverge for more than one integration session.
- DMA/control integration blocks progress past Week 3.
- Visualisation work starts consuming time needed for correctness.
- A stretch feature requires changing the MVP data format late in the project.
