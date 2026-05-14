`timescale 1ns / 1ps

// Selects the strategy of the highest-payoff neighbour, then optionally mutates.
// The unit assumes neighbour payoffs are already accumulated for the same
// generation. A full accelerator may need a two-pass design or a stored payoff
// plane to provide these values.
module strategy_update_unit #(
    parameter int N_NEIGHBOURS = 8,
    parameter int STRATEGY_BITS = 2,
    parameter int PAYOFF_WIDTH = 16
) (
    input  logic [STRATEGY_BITS-1:0] self_strategy_i,
    input  logic signed [PAYOFF_WIDTH-1:0] self_payoff_i,
    input  logic [N_NEIGHBOURS*STRATEGY_BITS-1:0] neighbour_strategies_i,
    input  logic signed [N_NEIGHBOURS*PAYOFF_WIDTH-1:0] neighbour_payoffs_i,
    input  logic [31:0] random_i,
    input  logic [15:0] mutation_threshold_i,
    output logic [STRATEGY_BITS-1:0] strategy_o
);

    integer idx;
    logic signed [PAYOFF_WIDTH-1:0] best_payoff;
    logic signed [PAYOFF_WIDTH-1:0] candidate_payoff;
    logic [STRATEGY_BITS-1:0] best_strategy;
    logic [STRATEGY_BITS-1:0] candidate_strategy;

    always_comb begin
        best_payoff = self_payoff_i;
        best_strategy = self_strategy_i;

        for (idx = 0; idx < N_NEIGHBOURS; idx = idx + 1) begin
            candidate_payoff = $signed(neighbour_payoffs_i[idx*PAYOFF_WIDTH +: PAYOFF_WIDTH]);
            candidate_strategy = neighbour_strategies_i[idx*STRATEGY_BITS +: STRATEGY_BITS];
            if (candidate_payoff > best_payoff) begin
                best_payoff = candidate_payoff;
                best_strategy = candidate_strategy;
            end
        end

        if (random_i[15:0] < mutation_threshold_i) begin
            strategy_o = random_i[17:16];
        end else begin
            strategy_o = best_strategy;
        end
    end

endmodule

