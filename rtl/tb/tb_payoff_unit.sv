`timescale 1ns / 1ps

module tb_payoff_unit;

    logic [1:0] strategy_a;
    logic [1:0] strategy_b;
    logic random_a;
    logic random_b;
    logic signed [15:0] payoff_a;

    payoff_unit dut (
        .strategy_a_i(strategy_a),
        .strategy_b_i(strategy_b),
        .random_a_i(random_a),
        .random_b_i(random_b),
        .payoff_a_o(payoff_a)
    );

    task automatic expect_payoff(input logic [1:0] a, input logic [1:0] b, input int expected);
        begin
            strategy_a = a;
            strategy_b = b;
            random_a = 1'b0;
            random_b = 1'b0;
            #1;
            if (payoff_a !== expected[15:0]) begin
                $fatal(1, "payoff mismatch: a=%0d b=%0d got=%0d expected=%0d", a, b, payoff_a, expected);
            end
        end
    endtask

    initial begin
        expect_payoff(2'd0, 2'd0, 3);
        expect_payoff(2'd0, 2'd1, 0);
        expect_payoff(2'd1, 2'd0, 5);
        expect_payoff(2'd1, 2'd1, 1);
        $display("tb_payoff_unit passed");
        $finish;
    end

endmodule

