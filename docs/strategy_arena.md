# Strategy Arena / Strategy Colosseum

The Strategy Arena is a high-level direction for turning the Artificial Civilisation Engine into a hardware-accelerated game-theory laboratory. Instead of starting with a spatial world, the system can first run tournaments where many long-game strategies compete across repeated games, are scored, ranked, evolved, mutated, and visualised.

This gives the project a clearer MVP: repeated matches are measurable, benchmarkable, and easier to map to FPGA match cores than a full spatial civilisation. The artificial civilisation layer remains the visually impressive extension once the match engine and strategy model are stable.

## Core Idea

The Strategy Colosseum asks:

- Which strategies survive long repeated interaction?
- Which strategies exploit naive opponents?
- Which strategies remain robust under noise?
- What happens when strategies mutate or adapt?
- Can simple hardware match engines simulate enough games to reveal strategic ecosystems?

A tournament can contain strategies such as:

- Always Cooperate.
- Always Defect / Betray.
- Tit-for-Tat.
- Suspicious Tit-for-Tat.
- Generous Tit-for-Tat.
- Random(p).
- Pavlov / Win-Stay-Lose-Shift.
- Grudger.
- Adaptive strategies.
- Q-learning agents.
- Small neural-network agents as stretch goals.

## Supported Games

The first game should be repeated Prisoner's Dilemma. The architecture should leave room for:

- Snowdrift / Hawk-Dove.
- Stag Hunt.
- Public Goods.
- Custom payoff matrices.
- Noisy or partially observed games.

## Arena Layer

The Strategy Arena layer defines the experiment:

- Game type.
- Payoff matrix.
- Number of rounds per match.
- Strategy list.
- Initial population size.
- Noise probability.
- Mutation probability.
- Tournament schedule.
- Ranking metric.
- Reproduction and elimination rules.

This layer should be software-controlled. Python should remain the reference for semantics, experiment generation, and validation.

## FPGA Match Engine

The FPGA should accelerate repeated match computation:

- Strategy decision.
- History and memory lookup.
- Payoff lookup.
- Score accumulation.
- Match scheduling.
- Mutation/randomness.
- Statistics reduction.

The first hardware target can be a single repeated Prisoner's Dilemma match core. The competitive target is many parallel match cores running independent strategy pairs or tournament shards.

## Evolution Layer

After each tournament generation, the host or processing system can apply evolution:

- Rank strategies by score, robustness, or exploitability.
- Eliminate weak variants.
- Reproduce strong variants.
- Mutate parameters such as forgiveness, suspicion, randomness, or learning rate.
- Inject new strategy variants.

This layer is a strong bridge between the arena and civilisation modes. The arena evolves strategy populations globally; the civilisation mode evolves them spatially.

## Relationship to Spatial Civilisation

The Strategy Arena and Artificial Civilisation modes are connected:

- Arena mode: strategies compete in abstract tournaments.
- Spatial mode: strategies inhabit agents on a grid and interact with neighbours.

The same strategy definitions, payoff matrices, RNG, and metrics should be reusable in both modes. The arena is the cleaner engineering MVP. The spatial civilisation is the richer emergent-behaviour showcase.

## Visualisation

The dashboard should make strategy competition legible:

- Leaderboard.
- Strategy-vs-strategy payoff matrix.
- Cooperation ratio over time.
- Population distribution.
- Exploitability / robustness score.
- Tournament replay.
- Payoff heatmap.
- Spatial civilisation map when spatial mode is enabled.

## First-Place-Level Project Angle

The strongest project narrative is not simply "we made a simulator faster." It is:

> We built a distributed FPGA-accelerated game-theory laboratory for testing long-horizon strategic behaviour, emergent cooperation, betrayal, adaptation, and social evolution.

The Strategy Arena gives the team a defensible benchmark story. The Artificial Civilisation layer gives the team a memorable demo story.

## Suggested Roadmap

1. Python tournament simulator for repeated Prisoner's Dilemma.
2. Single FPGA match core for two fixed strategies.
3. Multiple parallel match cores with score reduction.
4. Evolutionary tournament with mutation.
5. Spatial civilisation mode using evolved strategies.
6. Multi-board strategy league or distributed civilisation.
