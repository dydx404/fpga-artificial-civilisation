# Extension Ideas

These are possible directions after the MVP. Each one should be treated as an experiment with a small deliverable, not as mandatory scope.

## Strategy Arena

- Repeated-game tournament engine.
- Strategy-vs-strategy payoff matrix.
- Leaderboard and robustness score.
- Noise sweeps and exploitability analysis.
- Tournament replay.
- Population distribution over evolutionary generations.

## Strategy Catalogue

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

## Configurable Games

- Prisoner's Dilemma.
- Snowdrift / Hawk-Dove.
- Stag Hunt.
- Public Goods.
- Custom 2x2 payoff matrix.
- Spatially varying payoff matrices.
- Noisy or partially observed games.

## Agent Memory and Trust

- Remember the last action of neighbours.
- Maintain a compact trust score.
- Punish defectors after repeated betrayal.
- Allow reputation to spread locally.
- Use memory length as an evolvable strategy parameter.

## Resources and Territory

- Add an energy or food field.
- Let agents consume and regenerate resources.
- Penalise overcrowding.
- Allow migration toward richer cells.
- Track territories or cluster ownership.

## Mutation and Reproduction

- Strategy mutation via LFSR.
- Reproduction into empty cells.
- Death when energy falls below zero.
- Age-based mortality.
- Adaptive mutation under stress.
- Mutation of probabilistic strategy parameters.

## Civilisation Layer

- Alliances or factions.
- Public goods projects.
- Collapse and recovery events.
- Inequality metrics.
- Local governance rules.
- Arena-evolved strategies seeded into spatial worlds.

## Hardware Extensions

- Multiple match cores.
- Multiple spatial update cores.
- Tiled streaming with halo exchange.
- Runtime-selectable kernels.
- Hardware histogram and entropy assist.
- Multi-board world partitioning.

## Multi-Board Extensions

- Parallel tournament sharding.
- One strategy family per board.
- Distributed civilisation regions.
- Ethernet border exchange for spatial worlds.
- Host-aggregated global leaderboard.
- Inter-board migration, invasion, or information exchange.

## Visualisation Extensions

- Web heatmap viewer.
- Unity 3D civilisation map.
- Live charts and experiment controls.
- Strategy leaderboard.
- Payoff heatmap.
- Strategy-vs-strategy matrix.
- Exploitability / robustness panel.
- Replay files for presentations.
- Side-by-side CPU and FPGA simulation.
