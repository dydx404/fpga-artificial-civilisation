`timescale 1ns / 1ps

// Double-buffered world memory scaffold.
//
// This module is simulation-friendly and intentionally simple. A production
// PYNQ design may replace it with AXI BRAM controllers, DMA-accessible buffers,
// or a tiled streaming memory system.
module world_buffer #(
    parameter int ADDR_WIDTH = 16,
    parameter int AGENT_WIDTH = 8,
    parameter int DEPTH = 65536
) (
    input  logic clk_i,
    input  logic rst_ni,
    input  logic swap_i,

    input  logic load_we_i,
    input  logic [ADDR_WIDTH-1:0] load_addr_i,
    input  logic [AGENT_WIDTH-1:0] load_agent_i,

    input  logic [ADDR_WIDTH-1:0] current_addr_i,
    output logic [AGENT_WIDTH-1:0] current_agent_o,

    input  logic next_we_i,
    input  logic [ADDR_WIDTH-1:0] next_addr_i,
    input  logic [AGENT_WIDTH-1:0] next_agent_i
);

    logic active_buffer_q;
    logic [AGENT_WIDTH-1:0] mem_a [0:DEPTH-1];
    logic [AGENT_WIDTH-1:0] mem_b [0:DEPTH-1];

    assign current_agent_o = active_buffer_q ? mem_b[current_addr_i] : mem_a[current_addr_i];

    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            active_buffer_q <= 1'b0;
        end else begin
            if (swap_i) begin
                active_buffer_q <= ~active_buffer_q;
            end

            if (load_we_i) begin
                if (active_buffer_q) begin
                    mem_b[load_addr_i] <= load_agent_i;
                end else begin
                    mem_a[load_addr_i] <= load_agent_i;
                end
            end

            if (next_we_i) begin
                if (active_buffer_q) begin
                    mem_a[next_addr_i] <= next_agent_i;
                end else begin
                    mem_b[next_addr_i] <= next_agent_i;
                end
            end
        end
    end

endmodule

