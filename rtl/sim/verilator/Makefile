RTL_DIR := ../../src
TB_DIR := ../../tb
TB ?= tb_payoff_unit

SV_SRCS := \
	$(RTL_DIR)/payoff_unit.sv \
	$(RTL_DIR)/mutation_lfsr.sv \
	$(RTL_DIR)/strategy_update_unit.sv \
	$(RTL_DIR)/agent_update_core.sv \
	$(RTL_DIR)/stats_reducer.sv \
	$(RTL_DIR)/top_civ_engine.sv \
	$(TB_DIR)/$(TB).sv

.PHONY: all run clean

all: run

run:
	verilator --binary --timing -Wall $(SV_SRCS) --top-module $(TB)
	./obj_dir/V$(TB)

clean:
	rm -rf obj_dir

