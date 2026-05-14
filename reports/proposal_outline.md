# Proposal Outline

## Title

FPGA Artificial Civilisation Engine: Hardware-Accelerated Simulation of Emergent Cooperation

## Motivation

Explain why evolutionary game theory and cellular automata are useful for studying cooperation, collapse, and collective behaviour. Motivate FPGA acceleration through massive local parallelism.

## Objectives

- Build a Python reference simulator.
- Design an FPGA update pipeline for local agent interactions.
- Visualise strategy evolution and statistics.
- Benchmark CPU and FPGA throughput.
- Demonstrate at least one emergent behaviour story.

## Method

Describe the 2D grid, agent state, Prisoner's Dilemma payoff, mutation, strategy copying, and double buffering.

## Hardware Plan

Describe neighbour fetch, payoff computation, mutation LFSR, writeback, and statistics reduction.

## Evaluation

Correctness against Python on small worlds. Throughput comparison on larger worlds. Qualitative demo of emergent behaviour.

## Risks

Neighbour fetch, DMA, scope creep, visualisation time, and correctness mismatch.

