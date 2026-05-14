# Demo Storyboard

The final demo should tell a clear story: simple local incentives can produce dramatic long-horizon behaviour, and FPGA acceleration lets the team explore many more strategic interactions than a simple CPU loop.

## Scene 1: Open the Strategy Colosseum

Start with a tournament dashboard. Show a list of strategies entering the arena: Always Cooperate, Always Defect, Tit-for-Tat, Suspicious Tit-for-Tat, Generous Tit-for-Tat, Random(p), Pavlov, and Grudger.

## Scene 2: Long Repeated Games

Run repeated Prisoner's Dilemma matches. Show that one-round incentives do not tell the whole story: long memory, retaliation, forgiveness, and noise change which strategies survive.

## Scene 3: Leaderboard and Payoff Matrix

Display a leaderboard and strategy-vs-strategy payoff matrix. Highlight exploiters, robust cooperators, and strategies that perform well only against weak opponents.

## Scene 4: FPGA Acceleration

Run the same tournament on CPU and FPGA. Show rounds per second, matches per second, and whether transfer overhead is included. If multiple match cores exist, show parallel scaling.

## Scene 5: Evolutionary Tournament

Enable selection and mutation. Weak strategy variants disappear, strong variants reproduce, and probabilistic parameters drift. Show population distribution changing over generations.

## Scene 6: Spatial Civilisation Extension

Move winning or interesting strategies into a 2D civilisation map. Agents interact with neighbours. Cooperation clusters, betrayal waves, collapse, and recovery become visible.

## Scene 7: Multi-Board Extension

If multiple PYNQ boards are available, show each board as an arena shard, civilisation region, or strategy league participant. The host aggregates a global leaderboard or distributed map.

## Live Statistics

Display a compact dashboard:

- Cooperation ratio.
- Mean payoff.
- Strategy distribution.
- Entropy.
- Leaderboard rank.
- Strategy-vs-strategy payoff.
- Robustness or exploitability score.
- Tournament generation number.

The best demo ends with a live parameter change, such as increasing noise, mutation, temptation payoff, or round count, and watching the strategic ecosystem respond.

## Backup Demo

If the full FPGA path is not ready, show:

- Python tournament simulator with strong leaderboard and payoff-matrix visualisation.
- Single FPGA repeated Prisoner's Dilemma match core if available.
- Spatial civilisation as a Python or visual extension.
- A clear roadmap from arena MVP to distributed civilisation.

