`timescale 1ns / 1ps

// Combinational payoff unit for a two-action game.
//
// Strategy encoding:
//   2'd0 cooperate
//   2'd1 defect
//   2'd2 tit-for-tat placeholder, treated as cooperate until memory exists
//   2'd3 random placeholder, random bit selects defect when high
module payoff_unit #(
    parameter int PAYOFF_WIDTH = 16,
    parameter logic signed [PAYOFF_WIDTH-1:0] R_PAYOFF = 16'sd3,
    parameter logic signed [PAYOFF_WIDTH-1:0] S_PAYOFF = 16'sd0,
    parameter logic signed [PAYOFF_WIDTH-1:0] T_PAYOFF = 16'sd5,
    parameter logic signed [PAYOFF_WIDTH-1:0] P_PAYOFF = 16'sd1
) (
    input  logic [1:0] strategy_a_i,
    input  logic [1:0] strategy_b_i,
    input  logic       random_a_i,
    input  logic       random_b_i,
    output logic signed [PAYOFF_WIDTH-1:0] payoff_a_o
);

    localparam logic [1:0] STRATEGY_COOPERATE = 2'd0;
    localparam logic [1:0] STRATEGY_DEFECT    = 2'd1;
    localparam logic [1:0] STRATEGY_TFT       = 2'd2;
    localparam logic [1:0] STRATEGY_RANDOM    = 2'd3;

    logic action_a_defects;
    logic action_b_defects;

    always_comb begin
        unique case (strategy_a_i)
            STRATEGY_COOPERATE: action_a_defects = 1'b0;
            STRATEGY_DEFECT:    action_a_defects = 1'b1;
            STRATEGY_TFT:       action_a_defects = 1'b0;       // TODO: use neighbour memory.
            STRATEGY_RANDOM:    action_a_defects = random_a_i;
            default:            action_a_defects = 1'b1;
        endcase

        unique case (strategy_b_i)
            STRATEGY_COOPERATE: action_b_defects = 1'b0;
            STRATEGY_DEFECT:    action_b_defects = 1'b1;
            STRATEGY_TFT:       action_b_defects = 1'b0;       // TODO: use neighbour memory.
            STRATEGY_RANDOM:    action_b_defects = random_b_i;
            default:            action_b_defects = 1'b1;
        endcase

        if (!action_a_defects && !action_b_defects) begin
            payoff_a_o = R_PAYOFF;
        end else if (!action_a_defects && action_b_defects) begin
            payoff_a_o = S_PAYOFF;
        end else if (action_a_defects && !action_b_defects) begin
            payoff_a_o = T_PAYOFF;
        end else begin
            payoff_a_o = P_PAYOFF;
        end
    end

endmodule

