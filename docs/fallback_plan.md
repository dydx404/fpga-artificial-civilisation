# Fallback Plan

This project should be ambitious, but it needs a practical landing path. The fallback tiers are not failures. They are controlled freeze points that still produce a coherent demo and report.

The updated fallback ladder treats the Strategy Arena as the clearest MVP and Spatial Civilisation as the visually richer extension.

## Tier 0: Python Tournament Simulator Only

Deliver:

- Python repeated-game tournament simulator.
- Strategy catalogue with fixed strategies such as cooperate, defect, tit-for-tat, random, Pavlov, and Grudger.
- Leaderboard, payoff matrix, and cooperation statistics.
- Experiment results showing exploitation, robustness, and adaptation.
- Clear architecture document for the FPGA match-engine path.

Use this if hardware integration collapses completely. The scientific story can still be strong because tournaments are measurable and easy to explain.

## Tier 1: Single FPGA Match Core for Repeated Prisoner's Dilemma

Deliver:

- One FPGA match core.
- Fixed repeated Prisoner's Dilemma payoff matrix.
- Two or more simple strategies.
- Score accumulation over many rounds.
- CPU versus FPGA comparison for identical match rules.

This is the minimum strong FPGA result because it proves the core repeated-game datapath.

## Tier 2: Many Parallel FPGA Match Cores

Deliver:

- Replicated match cores.
- Tournament sharding across cores.
- Strategy-vs-strategy payoff table.
- Hardware statistics reduction.
- Throughput measured as rounds per second and matches per second.

This is the competitive hardware target. It gives a clean scaling story.

## Tier 3: Evolutionary Tournament with Mutation

Deliver:

- Population of strategy variants.
- Elimination and reproduction between tournament generations.
- Mutation of probabilistic strategy parameters.
- Robustness/noise experiments.
- Live leaderboard and population distribution.

This provides the strongest game-theory laboratory story while keeping the spatial world optional.

## Tier 4: Spatial Artificial Civilisation

Deliver:

- Strategies live as agents on a 2D grid.
- Agents interact with neighbours.
- Cooperation clusters, betrayal waves, collapse, and recovery emerge.
- Optional resource or energy pressure.
- Visual civilisation map and spatial statistics.

This is the visually impressive extension once arena semantics and FPGA acceleration are stable.

## Tier 5: Multi-Board Distributed Strategy League / Civilisation World

Deliver one mode only if the base system is reliable:

- Parallel tournament sharding across PYNQ boards.
- Spatial world partitioning with border exchange.
- Strategy league where boards host different strategy families or civilisations.
- Host dashboard aggregating board-level results.

## Freeze Rules

- End of Week 2: freeze at Tier 1 if a match core is not stable.
- End of Week 3: freeze at Tier 2 if parallel cores or result transfer remain unstable.
- Mid Week 4: freeze the demo feature set and stop adding strategy/civilisation rules.
- Week 5: only fix, measure, document, and polish.

