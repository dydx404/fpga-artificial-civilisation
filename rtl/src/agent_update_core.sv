`timescale 1ns / 1ps

// Cell-local update wrapper.
//
// TODO pipeline stages:
//   1. Register centre and neighbour words.
//   2. Compute payoff against all neighbours.
//   3. Select best neighbour strategy from accumulated payoff plane.
//   4. Apply mutation.
//   5. Pack next agent word and emit statistics.
module agent_update_core #(
    parameter int AGENT_WIDTH = 8,
    parameter int N_NEIGHBOURS = 8,
    parameter int PAYOFF_WIDTH = 16,
    parameter logic signed [PAYOFF_WIDTH-1:0] R_PAYOFF = 16'sd3,
    parameter logic signed [PAYOFF_WIDTH-1:0] S_PAYOFF = 16'sd0,
    parameter logic signed [PAYOFF_WIDTH-1:0] T_PAYOFF = 16'sd5,
    parameter logic signed [PAYOFF_WIDTH-1:0] P_PAYOFF = 16'sd1
) (
    input  logic clk_i,
    input  logic rst_ni,
    input  logic valid_i,
    input  logic [AGENT_WIDTH-1:0] agent_i,
    input  logic [N_NEIGHBOURS*AGENT_WIDTH-1:0] neighbours_i,
    input  logic signed [N_NEIGHBOURS*PAYOFF_WIDTH-1:0] neighbour_payoffs_i,
    input  logic [31:0] random_i,
    input  logic [15:0] mutation_threshold_i,
    output logic valid_o,
    output logic [AGENT_WIDTH-1:0] agent_o,
    output logic signed [PAYOFF_WIDTH-1:0] payoff_o
);

    localparam int STRATEGY_BITS = 2;

    logic [STRATEGY_BITS-1:0] self_strategy;
    logic [N_NEIGHBOURS*STRATEGY_BITS-1:0] neighbour_strategies;
    logic signed [PAYOFF_WIDTH-1:0] interaction_payoff [N_NEIGHBOURS];
    logic signed [PAYOFF_WIDTH-1:0] payoff_sum;
    logic [STRATEGY_BITS-1:0] next_strategy;

    assign self_strategy = agent_i[1:0];

    genvar n;
    generate
        for (n = 0; n < N_NEIGHBOURS; n = n + 1) begin : gen_payoff_units
            assign neighbour_strategies[n*STRATEGY_BITS +: STRATEGY_BITS] =
                neighbours_i[n*AGENT_WIDTH +: STRATEGY_BITS];

            payoff_unit #(
                .PAYOFF_WIDTH(PAYOFF_WIDTH),
                .R_PAYOFF(R_PAYOFF),
                .S_PAYOFF(S_PAYOFF),
                .T_PAYOFF(T_PAYOFF),
                .P_PAYOFF(P_PAYOFF)
            ) payoff_unit_i (
                .strategy_a_i(self_strategy),
                .strategy_b_i(neighbours_i[n*AGENT_WIDTH +: STRATEGY_BITS]),
                .random_a_i(random_i[n]),
                .random_b_i(random_i[n+8]),
                .payoff_a_o(interaction_payoff[n])
            );
        end
    endgenerate

    integer idx;
    always_comb begin
        payoff_sum = '0;
        for (idx = 0; idx < N_NEIGHBOURS; idx = idx + 1) begin
            payoff_sum = payoff_sum + interaction_payoff[idx];
        end
    end

    strategy_update_unit #(
        .N_NEIGHBOURS(N_NEIGHBOURS),
        .STRATEGY_BITS(STRATEGY_BITS),
        .PAYOFF_WIDTH(PAYOFF_WIDTH)
    ) strategy_update_unit_i (
        .self_strategy_i(self_strategy),
        .self_payoff_i(payoff_sum),
        .neighbour_strategies_i(neighbour_strategies),
        .neighbour_payoffs_i(neighbour_payoffs_i),
        .random_i(random_i),
        .mutation_threshold_i(mutation_threshold_i),
        .strategy_o(next_strategy)
    );

    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            valid_o <= 1'b0;
            agent_o <= '0;
            payoff_o <= '0;
        end else begin
            valid_o <= valid_i;
            payoff_o <= payoff_sum;
            // Preserve non-strategy bits until energy/age update is implemented.
            agent_o <= {agent_i[AGENT_WIDTH-1:STRATEGY_BITS], next_strategy};
        end
    end

endmodule

