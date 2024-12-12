from operator import add, floordiv, mul, sub
from typing import List

OPERATOR_DICT = {"+": add, "-": sub, "/": floordiv, "*": mul}


class StackUnderflowError(Exception):
    pass


def update_stack(stack: List[int], element: str) -> List[int]:
    check_minimum_elements = {
        "dup": 1,
        "swap": 2,
        "drop": 1,
        "over": 2,
        "+": 2,
        "-": 2,
        "*": 2,
        "/": 2,
    }
    if element in check_minimum_elements:
        if len(stack) < check_minimum_elements[element]:
            raise StackUnderflowError("Insufficient number of items in stack")
    if element.isdigit():
        stack.append(int(element))
    elif element == "dup":
        stack.append(stack[-1])
    elif element == "swap":
        stack[-1], stack[-2] = stack[-2], stack[-1]
    elif element == "drop":
        stack.pop()
    elif element == "over":
        stack.append(stack[-2])
    elif element in "+-*/":
        stack = stack[:-2] + [OPERATOR_DICT[element](stack[-2], stack[-1])]
    else:
        raise ValueError("undefined operation")
    return stack


def evaluate(input_data: List[str]) -> None:
    commands = [command.lower().split() for command in input_data]
    stack = []
    user_defined_words = {}
    for command in commands[:-1]:
        if command[1].isdigit():
            raise ValueError("Cannot redefine numbers")
        sub_command = []
        for element in command[2:-1]:
            if element in user_defined_words:
                sub_command = sub_command + user_defined_words[element]
            else:
                sub_command.append(element)
        user_defined_words[command[1]] = sub_command
    for element in commands[-1]:
        if element in user_defined_words:
            for sub_element in user_defined_words[element]:
                stack = update_stack(stack, sub_element)
        else:
            stack = update_stack(stack, element)
    return stack
