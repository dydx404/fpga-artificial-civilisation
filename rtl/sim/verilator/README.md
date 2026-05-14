# Verilator Simulation

This folder contains a starter Makefile for compiling small SystemVerilog testbenches with Verilator.

The RTL is still a scaffold, so treat these simulations as smoke tests and module-level checks rather than full-system verification.

## Example

```bash
make TB=tb_payoff_unit
make TB=tb_lfsr
make TB=tb_agent_update_core
```

You may need to adjust include paths or add a C++ harness depending on the local Verilator version.

