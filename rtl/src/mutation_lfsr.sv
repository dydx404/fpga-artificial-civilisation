`timescale 1ns / 1ps

// 32-bit Fibonacci LFSR for mutation decisions and placeholder random actions.
// This is not a cryptographic RNG. It is deterministic and seedable, which is
// useful for repeatable hardware/software comparisons.
module mutation_lfsr #(
    parameter logic [31:0] SEED = 32'h1ACE_B00C
) (
    input  logic        clk_i,
    input  logic        rst_ni,
    input  logic        enable_i,
    output logic [31:0] state_o
);

    logic feedback;

    // Taps for x^32 + x^22 + x^2 + x + 1.
    assign feedback = state_o[31] ^ state_o[21] ^ state_o[1] ^ state_o[0];

    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            state_o <= (SEED == 32'd0) ? 32'd1 : SEED;
        end else if (enable_i) begin
            state_o <= {state_o[30:0], feedback};
            if (state_o == 32'd0) begin
                state_o <= 32'd1;
            end
        end
    end

endmodule

