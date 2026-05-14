# MVP Plan

The updated MVP is arena-first: a repeated-game Strategy Colosseum with a Python reference tournament and a first FPGA repeated-match datapath target.

This is a clearer first milestone than the full spatial civilisation because it is easier to verify, benchmark, and explain. The existing spatial Python simulator remains valuable as the extension path once the strategy semantics and match engine are stable.

## Arena MVP Rules

- Repeated Prisoner's Dilemma as the first game.
- Fixed round count per match.
- Initial strategy catalogue: Always Cooperate, Always Defect, Tit-for-Tat, Random(p), Pavlov, and Grudger.
- Configurable payoff matrix with `R`, `S`, `T`, and `P`.
- Optional noise probability for action flips.
- Score accumulation across rounds.
- Strategy-vs-strategy payoff matrix.
- Leaderboard ranked by total or mean score.

## Arena MVP Deliverables

- Python tournament reference model.
- Strategy catalogue with deterministic fixed-seed behaviour.
- Unit tests for strategy decisions, payoff lookup, and score accumulation.
- Leaderboard and payoff matrix output.
- CPU baseline measured in rounds per second and matches per second.
- RTL plan or prototype for a single repeated Prisoner's Dilemma match core.
- Architecture, fallback, and demo documentation aligned around arena-first delivery.

## Spatial Extension Rules

The spatial civilisation path remains:

- 2D row-major grid.
- Moore neighbourhood with 8 neighbours.
- Agent fields: strategy, payoff, energy, age.
- Strategy copying from the highest-payoff neighbour.
- Mutation probability.
- Double-buffered world update.
- Cooperation clusters, betrayal waves, collapse, and recovery.

## Definition of Done

The arena MVP is done when:

- Python tournament tests pass.
- A repeated Prisoner's Dilemma tournament produces a leaderboard and payoff matrix.
- CPU benchmark reports rounds per second and matches per second.
- The team can explain how a repeated match maps to an FPGA match core.
- Spatial civilisation remains available as the demo extension rather than blocking the MVP.

## First Experiments

Suggested arena experiments:

- All fixed strategies against each other for 100, 1000, and 10000 rounds.
- Noise sweep from 0 to 0.05.
- Temptation payoff sweep varying `T`.
- Random(p) sweep across several cooperation probabilities.
- Tournament population seeded with repeated variants of the same strategy family.

Suggested spatial follow-on experiments:

- Seed the grid with the arena winner and strongest exploiter.
- Compare spatial cooperation clusters against arena leaderboard rank.
- Add resource pressure after the basic spatial handoff works.

