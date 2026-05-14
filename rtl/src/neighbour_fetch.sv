`timescale 1ns / 1ps

// Placeholder neighbour fetch stage.
//
// A real implementation will use BRAM reads, line buffers, or tile buffers with
// halo cells. This scaffold passes the centre cell through and outputs zeroed
// neighbours so downstream modules can be wired and simulated early.
module neighbour_fetch #(
    parameter int AGENT_WIDTH = 8,
    parameter int N_NEIGHBOURS = 8
) (
    input  logic clk_i,
    input  logic rst_ni,
    input  logic valid_i,
    input  logic [AGENT_WIDTH-1:0] stream_agent_i,
    output logic valid_o,
    output logic [AGENT_WIDTH-1:0] centre_agent_o,
    output logic [N_NEIGHBOURS*AGENT_WIDTH-1:0] neighbours_o
);

    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            valid_o <= 1'b0;
            centre_agent_o <= '0;
            neighbours_o <= '0;
        end else begin
            valid_o <= valid_i;
            centre_agent_o <= stream_agent_i;
            neighbours_o <= '0; // TODO: replace with real Moore-neighbour window.
        end
    end

endmodule

