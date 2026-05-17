# Comparison With Other Project Ideas

This document compares three candidate project directions using practical criteria for a 35-day second-year EEE/FPGA group project.

| Project Idea | Strengths | Risks | FPGA Fit |
| --- | --- | --- | --- |
| EM field visualiser using sensors | Physically grounded, visually strong, intuitive demo | Sensor calibration, sparse reconstruction, noisy measurements, unclear role for FPGA beyond acquisition | Moderate: FPGA can sample/filter/stream data, but the compute acceleration story may be weak |
| CFD / equation solver | Technically impressive, strong numerical computing angle | High numerical/debugging risk, boundary conditions and stability are hard, may be too ambitious | Strong in principle, but likely too complex for the time limit |
| Spatial game dynamics simulator | Clear local parallelism, strong visualisation, modular scope, mathematical depth without heavy numerics | Less physically grounded, must avoid overclaiming social meaning | Strong: local synchronous updates, payoff lookup, replicated pipelines, double buffering, clear CPU/FPGA benchmark |

## Recommendation

The spatial game dynamics simulator is the most balanced option for this team if scope is controlled. It has a clear MVP, a credible FPGA datapath, visually understandable outputs, and enough mathematical content for a strong report.

The main discipline required is framing: present it as local strategic interaction and evolutionary dynamics, not as a realistic society simulator.
