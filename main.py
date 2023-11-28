from logic_evaluator.logic_evaluator import evaluate
from logic_evaluator.expression import expression

if __name__ == "__main__":
    logical_expression = expression( input(
        "Input a logical expression, the program will decide if the expression is true "
        + "or false: "
    ))
    logical_expression.generate_truth_table()