import logic_evaluator.logic_evaluator as le
from logic_evaluator.variable import variable
from itertools import product

class expression:
    def __init__(self, expression):
        self.expression = expression
        self.expression_tokenized = le.tokenize(self.expression)
        self.includes_variables = False
        self.number_of_variables = 0
        self.is_legal_expression = le.check_if_expression_is_legal(self.expression_tokenized)
        self.variables = []
        for i in self.expression_tokenized:
            if isinstance(i, variable):
                self.includes_variables = True
                is_duplicate = False
                for j in self.variables:
                    if j.name == i.name:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    self.variables.append(variable(i.name))
                    self.number_of_variables += 1
    def evaluate(self):
        if not self.is_legal_expression or self.includes_variables:
            return None
        return le.evaluate_expression_in_RPN(le.shunting_yard(le.simplify_expression_parts(self.expression_tokenized)))

    def simplified_equation(self):
        return le.simplify_expression_parts(self.expression_tokenized)

    def evaluate_with_values(self, values: list):
        if len(values) != self.number_of_variables:
            raise Exception("Variables")

        for j, token in enumerate(values):
            if token not in ["true", "false"] and le.alternative_tokens.get(token) not in ["true", "false"]:
                raise Exception("Incorrect Value for: " + token)
            if le.alternative_tokens.get(token) in ["true", "false"]:
                values[j] = le.alternative_tokens.get(token)
        copy_of_expression = self.expression_tokenized.copy()
        for i, var in enumerate(self.variables):
            for j, token in enumerate(copy_of_expression):
                if isinstance(token, variable) and token.name == var.name:
                    copy_of_expression[j] = values[i]
        return le.evaluate_expression_in_RPN(le.shunting_yard(le.simplify_expression_parts(copy_of_expression)))

    def generate_truth_table(self):
        max_lenght = len("false")
        for i in self.variables:
            if len(i.name) > max_lenght:
                max_lenght = len(i)
        if len(self.expression) > max_lenght:
            max_lenght = len(self.expression)
        for i in self.variables:
            print(i.name, end=" " * (max_lenght-len(i.name)) + " | ")
        print(self.expression)
        print("-" * (self.number_of_variables + 1) * (max_lenght + 3))
        for combo in list(product(["false", "true"], repeat=self.number_of_variables)):
            for i in combo:
                print(i, end= " " * (max_lenght-len(i)) + " | ")
            print(self.evaluate_with_values(combo))

