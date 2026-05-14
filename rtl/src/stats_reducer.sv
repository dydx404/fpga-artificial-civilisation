`timescale 1ns / 1ps

// Streaming statistics reducer for one frame.
module stats_reducer #(
    parameter int PAYOFF_WIDTH = 16,
    parameter int COUNT_WIDTH = 32,
    parameter int PAYOFF_SUM_WIDTH = 48
) (
    input  logic clk_i,
    input  logic rst_ni,
    input  logic start_i,
    input  logic valid_i,
    input  logic last_i,
    input  logic [1:0] strategy_i,
    input  logic signed [PAYOFF_WIDTH-1:0] payoff_i,
    output logic done_o,
    output logic [COUNT_WIDTH-1:0] cooperate_count_o,
    output logic [COUNT_WIDTH-1:0] defect_count_o,
    output logic [COUNT_WIDTH-1:0] tft_count_o,
    output logic [COUNT_WIDTH-1:0] random_count_o,
    output logic signed [PAYOFF_SUM_WIDTH-1:0] payoff_sum_o
);

    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            done_o <= 1'b0;
            cooperate_count_o <= '0;
            defect_count_o <= '0;
            tft_count_o <= '0;
            random_count_o <= '0;
            payoff_sum_o <= '0;
        end else if (start_i) begin
            done_o <= 1'b0;
            cooperate_count_o <= '0;
            defect_count_o <= '0;
            tft_count_o <= '0;
            random_count_o <= '0;
            payoff_sum_o <= '0;
        end else begin
            done_o <= 1'b0;
            if (valid_i) begin
                unique case (strategy_i)
                    2'd0: cooperate_count_o <= cooperate_count_o + 1'b1;
                    2'd1: defect_count_o <= defect_count_o + 1'b1;
                    2'd2: tft_count_o <= tft_count_o + 1'b1;
                    2'd3: random_count_o <= random_count_o + 1'b1;
                    default: ;
                endcase
                payoff_sum_o <= payoff_sum_o + {{(PAYOFF_SUM_WIDTH-PAYOFF_WIDTH){payoff_i[PAYOFF_WIDTH-1]}}, payoff_i};
                done_o <= last_i;
            end
        end
    end

endmodule

