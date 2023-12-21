def AND(first_argument: bool, second_argument: bool) -> bool:
    """
    ___________________________________________________________________________
    The implementation of the "and" operator
    ___________________________________________________________________________
    Input: two boolean values A and B
    Output: A and B
    """
    return first_argument and second_argument


def OR(first_argument: bool, second_argument: bool) -> bool:
    """
    ___________________________________________________________________________
    The implementation of the "or" operator
    ___________________________________________________________________________
    Input: two boolean values A and B
    Output: A or B
    """
    return first_argument or second_argument


def IMP(first_argument: bool, second_argument: bool) -> bool:
    """
    ___________________________________________________________________________
    The implementation of the "if ... then ..." operator
    ___________________________________________________________________________
    Input: two boolean values A and B
    Output: if A then B
    """
    return first_argument == second_argument or second_argument


def SYNEQ(first_argument: bool, second_argument: bool) -> bool:
    """
    ___________________________________________________________________________
    The implementation of the "if and only if" operator
    ___________________________________________________________________________
    Input: two boolean values A and B
    Output: A iff B
    """
    return first_argument == second_argument

def XOR(first_argument: bool, second_argument: bool) -> bool:
    """
        ___________________________________________________________________________
        The implementation of the "exclusive or" operator
        ___________________________________________________________________________
        Input: two boolean values A and B
        Output: not (A iff B)
        """
    return not (SYNEQ(first_argument, second_argument))
