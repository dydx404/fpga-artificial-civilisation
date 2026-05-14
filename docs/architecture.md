# Architecture

The system is split into host, processing system, and programmable logic. This split keeps the FPGA focused on repeated game computation while software handles flexibility, tournament orchestration, spatial modelling, visualisation, and analysis.

The project now has two connected operating modes:

- Strategy Arena / Strategy Colosseum: repeated-game tournaments between strategies.
- Artificial Civilisation / Spatial Evolution: strategies inhabit agents in a grid world and interact locally.

Strategy Arena is the cleaner MVP because match throughput, ranking, and correctness are easy to benchmark. Spatial Evolution is the extension that makes the demo feel alive.

## Host / PS / PL Split

Host machine:

- Tournament, game, and civilisation configuration.
- Web or Python visualisation.
- Long-running data logging.
- CPU reference simulations and benchmark comparison.
- Optional network client for remote control.
- Multi-board orchestration and result aggregation.

Zynq processing system:

- PYNQ overlay loading.
- DMA buffer allocation.
- Register configuration for payoff matrix, round count, mutation/noise probability, world size, and run control.
- TCP/WebSocket bridge to the host frontend.
- Sanity checks and fallback software execution.

Programmable logic:

- Repeated match pipeline.
- Strategy decision and memory/history lookup.
- Payoff lookup and score accumulation.
- Optional spatial neighbour fetch.
- Strategy update, mutation, and randomness.
- Statistics reduction.
- Tournament scheduling or frame traversal.

## Strategy Arena Data Flow

The intended Strategy Arena data flow is:

1. Host defines games, strategy list, round counts, noise, mutation, and tournament schedule.
2. Processing system packs configuration and strategy parameters for the FPGA.
3. FPGA match cores run repeated games and accumulate scores.
4. Statistics reducers produce cooperation counts, payoff totals, and matchup summaries.
5. Processing system returns compact results to the host.
6. Host aggregates leaderboards, payoff matrices, robustness scores, and evolution updates.
7. Dashboard renders tournament progress and strategy-vs-strategy outcomes.

## Spatial Civilisation Data Flow

The intended spatial data flow is:

1. Host sends experiment configuration to the PYNQ control layer.
2. Processing system packs the world into compact agent words.
3. DMA transfers a frame or tile into programmable logic.
4. The FPGA streams cells through the update pipeline.
5. Updated cells are written to the next buffer.
6. Statistics are reduced while the frame is processed.
7. The processing system reads summary metrics and selected frame data.
8. The host frontend renders heatmaps and charts.

## Strategy Arena Layer

The arena layer defines:

- Game type: Prisoner's Dilemma, Snowdrift, Stag Hunt, Public Goods, or custom matrix.
- Strategy catalogue: always cooperate, always defect, tit-for-tat variants, random(p), Pavlov, Grudger, adaptive, Q-learning, or neural stretch goals.
- Match length and tournament schedule.
- Noise, mutation, and population settings.
- Ranking, exploitability, and robustness metrics.

This layer should remain software-configurable so the FPGA can be a fast engine rather than a rigid experiment.

## FPGA Match Engine

The match engine is the most direct FPGA target:

- Many parallel match cores.
- Each core simulates a long repeated game between two strategies.
- Cores keep compact memory/history state.
- Payoff lookup is table-driven.
- Scores and cooperation counts accumulate locally.
- Result summaries stream back to the processing system.

The first hardware version can be a single repeated Prisoner's Dilemma core. The scalable version replicates cores and shards tournaments across them.

## Evolution Layer

The evolution layer can run in host software or the processing system:

- Weak strategies are eliminated.
- Strong strategies reproduce.
- Probabilistic parameters mutate.
- New strategy variants enter the population.
- Results feed the next tournament generation.

Keeping evolution in software initially reduces hardware risk while still enabling a strong scientific story.

## Double Buffering

The spatial simulator uses current and next world buffers:

- Read all agents from `world_current`.
- Write all updates to `world_next`.
- Never update a cell in place during the same generation.
- Swap buffers at the frame boundary.

This is important for correctness. Without double buffering, early cells in a frame could influence later cells in the same frame, creating scan-order artefacts.

Arena mode uses a different buffering model. It needs match-state buffers, score buffers, and result buffers rather than current/next world frames.

## DMA Idea

The PYNQ path should eventually use contiguous buffers and DMA:

- `current_frame`: packed agent words sent to PL.
- `next_frame`: packed agent words received from PL.
- `metrics_frame`: optional statistics payload.
- `match_config`: packed strategy/game configuration for arena mode.
- `match_results`: compact score and statistics records returned by arena mode.

For the MVP, a frame can be transferred as a flat row-major byte array. Later versions may use tiles so that large worlds fit within BRAM or stream through line buffers.

## Frontend Visualisation Pipeline

The visualisation layer should support:

- Leaderboard.
- Strategy-vs-strategy payoff matrix.
- Payoff heatmap.
- Exploitability / robustness score.
- Population distribution.
- Live tournament replay.
- Strategy heatmap.
- Cooperation ratio chart.
- Mean payoff chart.
- Entropy or diversity chart.
- Optional energy/resource field overlay.

Initial implementation can use matplotlib. A web frontend can subscribe to JSON metadata plus binary or base64 frame payloads later.

## Match Pipeline

The planned Strategy Arena pipeline stages are:

1. Match schedule dispatch.
2. Strategy state and history lookup.
3. Strategy action decision.
4. Noise/random perturbation.
5. Payoff lookup.
6. Score accumulation.
7. Memory/history update.
8. Result/statistics reduction.

## Spatial Agent Update Pipeline

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
- Count wins/losses/draws in arena mode.
- Accumulate strategy-vs-strategy payoff totals.
- Track noise/mutation event counts.
- Optionally compute min/max energy.

Expensive derived values such as entropy can be computed in software from counts.

## Tile and Boundary Strategy

The spatial MVP assumes wrap-around edges because it simplifies Python and RTL comparison. If using tiles, each tile needs a halo region containing neighbouring cells. Halo exchange is a natural extension for multi-board or multi-region simulation.

## Multi-Board Extension

With multiple PYNQ-Z1 boards, the host can distribute work across boards:

- Parallel tournament sharding: each board runs different strategy pairs or noisy variants.
- Spatial civilisation partitioning: each board owns a world region and exchanges border agents over Ethernet.
- Strategy league: each board hosts a strategy family or civilisation and periodically competes with others.

The multi-board path should be summary-first. Boards should stream compact scores, population counts, and border slices before attempting full-frame streaming.
