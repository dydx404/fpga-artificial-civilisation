# Demo Storyboard

The demo should show simple local rules producing visible spatial dynamics, then show where the FPGA accelerates the update loop.

## Scene 1: Initial Grid

Show a grid with a random mix of strategies. Explain that each cell is a simple finite-state agent.

## Scene 2: Local Repeated Game

Show or explain the local update: each cell plays Prisoner's Dilemma with neighbours, accumulates payoff, and compares local performance.

## Scene 3: Spatial Evolution

Run the simulation. Show cooperation clusters, defector spread, boundary movement, or oscillations.

## Scene 4: Metrics

Display:

- cooperation ratio,
- strategy distribution,
- mean payoff,
- payoff heatmap,
- generation number.

## Scene 5: FPGA Acceleration

Run the same deterministic rule on CPU and FPGA. Show cells updated per second, game rounds per second, and full-loop timing including transfer overhead.

## Scene 6: Controlled Extension

If stable, enable mutation/noise or add another strategy. Show how the pattern changes.

## Backup Demo

If full FPGA grid integration is incomplete:

- Show Python visualisation.
- Show RTL payoff/update core tests.
- Show a single hardware update or simulated hardware-compatible pipeline.
- Explain the achieved fallback tier.
