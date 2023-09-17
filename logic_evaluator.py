logical_tokens: list = ["not", "or", "and", "true", "false", "(", ")", "=>", "<=>"]
operators: list = ["and", "or", "=>", "<=>"]
operators_precedence: dict = {"and": 2, "or": 3, "=>": 4, "<=>": 5}
alternative_tokens: dict = {
    "^": "and",
    "&": "and",
    "~": "not",
    "-": "not",
    "v": "or",
    "->": "=>",
    "<->": "<=>",
    "iff": "<=>",
    "w": "true",
    "t": "true",
    "1": "true",
    "0": "false",
    "f": "false",
}


def tokenize(expression: str) -> list:
    """
    ___________________________________________________________________________
    Check if used tokens are legal and return a tokenized list
    ___________________________________________________________________________
    Input: an expression as a String
    Output: The expression as a list of interpretable tokens
    """
    expression = expression.lower()
    token_array: list[str] = []
    expression = expression.replace(" ", "")
    current_token = ""
    for index, i in enumerate(list(expression)):
        current_token += i
        if current_token in logical_tokens and current_token != "":
            token_array.append(current_token)
            current_token = ""
        elif current_token in alternative_tokens and current_token != "":
            if current_token == "t" or current_token == "f":
                if (
                    len(expression) >= index + 4
                    and "true" == expression[index : index + 4]
                ):
                    continue
                elif (
                    len(expression) >= index + 5
                    and "false" == expression[index : index + 5]
                ):
                    continue
            token_array.append(alternative_tokens[current_token])
            current_token = ""

    if len(current_token) > 0:
        raise Exception("Invalid Expression")
    return token_array


def check_if_expression_is_legal(expression_tokenized: list) -> bool:
    """
    ___________________________________________________________________________
    Check if the expression is a legal expression of formal logic by using a PDA
    ___________________________________________________________________________
    Input: a list of tokens
    Output: the boolean value of the correctness of the expression
            (true if legal otherwise false)
    """
    stack = 0
    current_state = 0
    for i in expression_tokenized:
        if i == "(" and current_state in [0, 2]:
            stack += 1
        elif i == "not" and current_state in [0, 2]:
            continue
        elif i in ["true", "false"] and current_state == 0:
            current_state = 1
        elif i in ["true", "false"] and current_state == 2:
            current_state = 1
        elif i in operators and current_state == 1:
            current_state = 2
        elif i == ")" and current_state == 1:
            stack -= 1
        else:
            return False

    return current_state == 1 and stack == 0


def simplify_expression_parts(expression_tokenized: list) -> list:
    """
    ___________________________________________________________________________
    Use equivalent expressions to simplify expression parts
    Example:
        not true <=> false
        not not A <=> A
        ...
    ___________________________________________________________________________
    Input: an tokenized expression
    Output: simplified, but equivalent, expression
    """
    if len(expression_tokenized) <= 1:
        return expression_tokenized

    i = 0
    while i < len(expression_tokenized):
        if len(expression_tokenized) <= 1:
            return expression_tokenized
        if expression_tokenized[i] == "not" and expression_tokenized[i + 1] in [
            "false",
            "true",
        ]:
            temp = expression_tokenized[i + 1]
            del expression_tokenized[i]
            del expression_tokenized[i]
            expression_tokenized.insert(i, temp)
            i += 1
        elif expression_tokenized[i] == "not" and expression_tokenized[i + 1] == "not":
            del expression_tokenized[i]
            del expression_tokenized[i]

        i += 1

    return expression_tokenized


def shunting_yard(expression: list) -> list:
    """
    ___________________________________________________________________________
    shunting yard algorithm from Dijkstra to get the expression into the easier
    evaluatable postfix notation (for example: true and true => true true and)
    ___________________________________________________________________________
    Input: an tokenized expression
    Output: the expression in postfix notation
    """
    output_queue = []
    operator_stack = []

    for i in expression:
        if i in ["true", "false"]:
            output_queue.append(i)

        elif i == "not":
            operator_stack.append(i)

        elif i in operators:
            while (
                len(operator_stack) > 0
                and operator_stack[-1] in operators
                and operators_precedence[i] >= operators_precedence[operator_stack[-1]]
            ):
                output_queue.append(operator_stack[-1])
                del operator_stack[-1]
            operator_stack.append(i)

        elif i == "(":
            operator_stack.append(i)

        elif i == ")":
            while len(operator_stack) > 0 and operator_stack[-1] != "(":
                output_queue.append(operator_stack[-1])
                del operator_stack[-1]

            if len(operator_stack) == 0:
                raise Exception("Invalid Expression")

            del operator_stack[-1]

    while len(operator_stack) > 1:
        if operator_stack[len(operator_stack) - 1] != "(":
            output_queue.append(operator_stack[-1])
            del operator_stack[-1]
        else:
            raise Exception("Invalid Expression")

    if len(operator_stack) == 1:
        output_queue.append(operator_stack[0])

    return output_queue


def AND(first_argument: bool, second_argument: bool) -> bool:
    """
    ___________________________________________________________________________
    The implementation of the and operator
    ___________________________________________________________________________
    Input: two boolean values A and B
    Output: A and B
    """
    return first_argument and second_argument


def OR(first_argument: bool, second_argument: bool) -> bool:
    """
    ___________________________________________________________________________
    The implementation of the or operator
    ___________________________________________________________________________
    Input: two boolean values A and B
    Output: A or B
    """
    return first_argument or second_argument


def IMP(first_argument: bool, second_argument: bool) -> bool:
    """
    ___________________________________________________________________________
    The implementation of the if ... then ... operator
    ___________________________________________________________________________
    Input: two boolean values A and B
    Output: if A then B
    """
    return first_argument == second_argument or second_argument


def SYNEQ(first_argument: bool, second_argument: bool) -> bool:
    """
    ___________________________________________________________________________
    The implementation of the if and only if operator
    ___________________________________________________________________________
    Input: two boolean values A and B
    Output: A iff B
    """

    return first_argument == second_argument


def evaluate_expression_in_RPN(expression_in_RPN: list) -> bool:
    """
    ___________________________________________________________________________
    A stack based evaluator for the postfix notation.
    ___________________________________________________________________________
    Input: an tokenized expression in the postfix notation
    Output: the evaluated truth value of the expression
    """
    if len(expression_in_RPN) < 1:
        raise Exception("Invalid Expression")
    solution_stack = [True] if expression_in_RPN[0] == "true" else [False]
    for i in expression_in_RPN[1:]:
        if i in ["false", "true"]:
            solution_stack.append(True if i == "true" else False)
        elif i in operators:
            temp1 = solution_stack[-1]
            del solution_stack[-1]
            temp2 = solution_stack[-1]
            del solution_stack[-1]
            if i == "and":
                solution_stack.append(AND(temp1, temp2))
            elif i == "or":
                solution_stack.append(OR(temp1, temp2))
            elif i == "=>":
                solution_stack.append(IMP(temp2, temp1))
            elif i == "<=>":
                solution_stack.append(SYNEQ(temp1, temp2))
        elif i == "not":
            solution_stack[-1] = not solution_stack[-1]

    if len(solution_stack) != 1:
        raise Exception("Invalid expression")
    return solution_stack[0]


def evaluate(expression: str) -> bool:
    """
    ___________________________________________________________________________
    Evaluates an expression of formal logic to the truth value of the expression
    ___________________________________________________________________________
    Input: an expression as a String
    Output: the truth value
    """
    tokenized_expression = tokenize(expression)

    if not check_if_expression_is_legal(tokenized_expression):
        raise Exception("Invalid expression")
    else:
        return evaluate_expression_in_RPN(
            shunting_yard(simplify_expression_parts(tokenized_expression))
        )


if __name__ == "__main__":
    logical_expression: str = input(
        "Input a logical expression, the program will decide if the expression is true "
        + "or false: "
    )
    print(f"provided expression is {evaluate(logical_expression)}")
