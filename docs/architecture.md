# Architecture

The system is split into host, processing system, and programmable logic. This split keeps the FPGA focused on the repeated local update step while software handles flexibility, interaction, visualisation, and analysis.

## Host / PS / PL Split

Host machine:

- Experiment configuration and launch scripts.
- Web or Python visualisation.
- Long-running data logging.
- CPU reference simulations and benchmark comparison.
- Optional network client for remote control.

Zynq processing system:

- PYNQ overlay loading.
- DMA buffer allocation.
- Register configuration for world size, payoff matrix, mutation probability, and run control.
- TCP/WebSocket bridge to the host frontend.
- Sanity checks and fallback software execution.

Programmable logic:

- Agent update pipeline.
- Neighbour fetch.
- Payoff computation.
- Strategy update and mutation.
- Statistics reduction.
- Frame traversal and double-buffer switching.

## Data Flow

The intended full-system data flow is:

1. Host sends experiment configuration to the PYNQ control layer.
2. Processing system packs the world into compact agent words.
3. DMA transfers a frame or tile into programmable logic.
4. The FPGA streams cells through the update pipeline.
5. Updated cells are written to the next buffer.
6. Statistics are reduced while the frame is processed.
7. The processing system reads summary metrics and selected frame data.
8. The host frontend renders heatmaps and charts.

## Double Buffering

The simulator uses current and next world buffers:

- Read all agents from `world_current`.
- Write all updates to `world_next`.
- Never update a cell in place during the same generation.
- Swap buffers at the frame boundary.

This is important for correctness. Without double buffering, early cells in a frame could influence later cells in the same frame, creating scan-order artefacts.

## DMA Idea

The PYNQ path should eventually use contiguous buffers and DMA:

- `current_frame`: packed agent words sent to PL.
- `next_frame`: packed agent words received from PL.
- `metrics_frame`: optional statistics payload.

For the MVP, a frame can be transferred as a flat row-major byte array. Later versions may use tiles so that large worlds fit within BRAM or stream through line buffers.

## Frontend Visualisation Pipeline

The visualisation layer should support:

- Strategy heatmap.
- Cooperation ratio chart.
- Mean payoff chart.
- Entropy or diversity chart.
- Optional energy/resource field overlay.

Initial implementation can use matplotlib. A web frontend can subscribe to JSON metadata plus binary or base64 frame payloads later.

## Agent Update Pipeline

The planned pipeline stages are:

1. Coordinate/frame traversal.
2. Neighbour fetch from line buffers or BRAM.
3. Strategy action decode.
4. Payoff accumulation across neighbours.
5. Fitness comparison against neighbours.
6. Mutation or random perturbation.
7. Agent word packing.
8. Next-buffer writeback.

The first RTL version can compute one cell per several cycles. A later version can pipeline toward one cell per cycle.

## Statistics Pipeline

Statistics should be reduced in hardware where cheap:

- Count strategies.
- Sum payoff.
- Count cooperative strategies.
- Optionally compute min/max energy.

Expensive derived values such as entropy can be computed in software from counts.

## Tile and Boundary Strategy

The MVP assumes wrap-around edges because it simplifies Python and RTL comparison. If using tiles, each tile needs a halo region containing neighbouring cells. Halo exchange is a natural extension for multi-FPGA or multi-region simulation.

