`timescale 1ns / 1ps

module tb_agent_update_core;

    localparam int AGENT_WIDTH = 8;
    localparam int N_NEIGHBOURS = 8;
    localparam int PAYOFF_WIDTH = 16;

    logic clk;
    logic rst_n;
    logic valid_i;
    logic [AGENT_WIDTH-1:0] agent_i;
    logic [N_NEIGHBOURS*AGENT_WIDTH-1:0] neighbours_i;
    logic signed [N_NEIGHBOURS*PAYOFF_WIDTH-1:0] neighbour_payoffs_i;
    logic [31:0] random_i;
    logic [15:0] mutation_threshold_i;
    logic valid_o;
    logic [AGENT_WIDTH-1:0] agent_o;
    logic signed [PAYOFF_WIDTH-1:0] payoff_o;

    agent_update_core dut (
        .clk_i(clk),
        .rst_ni(rst_n),
        .valid_i(valid_i),
        .agent_i(agent_i),
        .neighbours_i(neighbours_i),
        .neighbour_payoffs_i(neighbour_payoffs_i),
        .random_i(random_i),
        .mutation_threshold_i(mutation_threshold_i),
        .valid_o(valid_o),
        .agent_o(agent_o),
        .payoff_o(payoff_o)
    );

    always #5 clk = ~clk;

    initial begin
        clk = 1'b0;
        rst_n = 1'b0;
        valid_i = 1'b0;
        agent_i = 8'd0;          // cooperate
        neighbours_i = '0;       // all cooperate
        neighbour_payoffs_i = '0;
        random_i = 32'd0;
        mutation_threshold_i = 16'd0;

        #20;
        rst_n = 1'b1;
        #10;
        valid_i = 1'b1;
        #10;
        valid_i = 1'b0;
        #10;

        if (!valid_o) begin
            $fatal(1, "expected valid output");
        end
        if (payoff_o !== 16'sd24) begin
            $fatal(1, "expected all-cooperator Moore payoff 24, got %0d", payoff_o);
        end

        $display("tb_agent_update_core passed");
        $finish;
    end

endmodule

