# Frontend

The frontend layer turns simulation frames and metrics into something readable during demos.

Start simple:

1. Use `python_viewer/live_viewer.py` for local Python simulation.
2. Use `web_viewer` once a stable frame protocol exists.
3. Add live PYNQ/TCP data only after the simulation and DMA paths are reliable.

## Visual Design Goals

- Strategy heatmap is the main view.
- Statistics should be visible without hiding the map.
- CPU versus FPGA comparisons should be explicit.
- Demo controls should focus on mutation, payoff, and reset.

