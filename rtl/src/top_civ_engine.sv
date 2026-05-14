`timescale 1ns / 1ps

// Top-level compute-engine outline.
//
// This is not yet a complete PYNQ IP block. It exposes a simple valid-driven
// window interface so the core datapath can be simulated before AXI wrappers,
// DMA, and real neighbour fetch are finished.
module top_civ_engine #(
    parameter int AGENT_WIDTH = 8,
    parameter int N_NEIGHBOURS = 8,
    parameter int PAYOFF_WIDTH = 16
) (
    input  logic clk_i,
    input  logic rst_ni,
    input  logic start_frame_i,
    input  logic valid_i,
    input  logic last_i,
    input  logic [AGENT_WIDTH-1:0] agent_i,
    input  logic [N_NEIGHBOURS*AGENT_WIDTH-1:0] neighbours_i,
    input  logic signed [N_NEIGHBOURS*PAYOFF_WIDTH-1:0] neighbour_payoffs_i,
    input  logic [15:0] mutation_threshold_i,
    output logic valid_o,
    output logic last_o,
    output logic [AGENT_WIDTH-1:0] agent_o,
    output logic stats_done_o,
    output logic [31:0] cooperate_count_o,
    output logic [31:0] defect_count_o,
    output logic [31:0] tft_count_o,
    output logic [31:0] random_count_o,
    output logic signed [47:0] payoff_sum_o
);

    logic [31:0] random_state;
    logic signed [PAYOFF_WIDTH-1:0] payoff;

    mutation_lfsr lfsr_i (
        .clk_i(clk_i),
        .rst_ni(rst_ni),
        .enable_i(valid_i),
        .state_o(random_state)
    );

    agent_update_core #(
        .AGENT_WIDTH(AGENT_WIDTH),
        .N_NEIGHBOURS(N_NEIGHBOURS),
        .PAYOFF_WIDTH(PAYOFF_WIDTH)
    ) agent_update_core_i (
        .clk_i(clk_i),
        .rst_ni(rst_ni),
        .valid_i(valid_i),
        .agent_i(agent_i),
        .neighbours_i(neighbours_i),
        .neighbour_payoffs_i(neighbour_payoffs_i),
        .random_i(random_state),
        .mutation_threshold_i(mutation_threshold_i),
        .valid_o(valid_o),
        .agent_o(agent_o),
        .payoff_o(payoff)
    );

    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            last_o <= 1'b0;
        end else begin
            last_o <= valid_i & last_i;
        end
    end

    stats_reducer #(
        .PAYOFF_WIDTH(PAYOFF_WIDTH)
    ) stats_reducer_i (
        .clk_i(clk_i),
        .rst_ni(rst_ni),
        .start_i(start_frame_i),
        .valid_i(valid_o),
        .last_i(last_o),
        .strategy_i(agent_o[1:0]),
        .payoff_i(payoff),
        .done_o(stats_done_o),
        .cooperate_count_o(cooperate_count_o),
        .defect_count_o(defect_count_o),
        .tft_count_o(tft_count_o),
        .random_count_o(random_count_o),
        .payoff_sum_o(payoff_sum_o)
    );

endmodule

