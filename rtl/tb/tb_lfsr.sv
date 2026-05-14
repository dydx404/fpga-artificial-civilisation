`timescale 1ns / 1ps

module tb_lfsr;

    logic clk;
    logic rst_n;
    logic enable;
    logic [31:0] state;
    logic [31:0] first_state;

    mutation_lfsr dut (
        .clk_i(clk),
        .rst_ni(rst_n),
        .enable_i(enable),
        .state_o(state)
    );

    always #5 clk = ~clk;

    initial begin
        clk = 1'b0;
        rst_n = 1'b0;
        enable = 1'b0;
        #20;
        rst_n = 1'b1;
        #10;
        first_state = state;
        enable = 1'b1;
        #50;
        if (state == first_state) begin
            $fatal(1, "LFSR did not advance");
        end
        if (state == 32'd0) begin
            $fatal(1, "LFSR entered zero state");
        end
        $display("tb_lfsr passed");
        $finish;
    end

endmodule

