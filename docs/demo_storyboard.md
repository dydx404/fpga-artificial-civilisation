# Demo Storyboard

The final demo should tell a clear story: simple local incentives can produce dramatic social-scale behaviour, and the FPGA makes it possible to explore larger worlds interactively.

## Scene 1: Random Society

Start with a random grid of cooperators and defectors. Show a heatmap where colours represent strategies. Explain that every cell is an agent making repeated local decisions.

## Scene 2: Defectors Dominate

Run fixed Prisoner's Dilemma with no mutation. Defectors exploit nearby cooperators and spread. The cooperation ratio drops. This establishes the baseline social dilemma.

## Scene 3: Local Copying and Mutation

Enable mutation and best-neighbour copying. The society becomes less uniform. Small pockets of alternative strategies appear. Some die out; some seed larger structures.

## Scene 4: Cooperation Clusters

Show that cooperators can survive in clusters because they reward each other locally. Highlight the difference between individual incentive and spatial group structure.

## Scene 5: Resource Scarcity

Enable a resource or energy pressure mode. Agents in crowded or low-resource regions lose energy. The map shows collapse in stressed areas and recovery where cooperative clusters stabilise.

## Scene 6: CPU vs FPGA

Run the same rule on CPU and FPGA. Show cells updated per second and frame rate. Be explicit about whether the benchmark includes DMA transfer.

## Scene 7: Live Statistics

Display:

- Cooperation ratio.
- Mean payoff.
- Strategy distribution.
- Entropy.
- Generation number.

The best demo ends with a live parameter change, such as increasing mutation or temptation, and watching the society respond.

## Backup Demo

If the full FPGA path is not ready, show:

- Python simulation with strong visualisation.
- FPGA cellular automata or fixed Prisoner's Dilemma proof.
- A clear roadmap connecting the two.

