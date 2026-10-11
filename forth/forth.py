from operator import add, floordiv, mul, sub
from typing import Dict, List

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
    if (
        element in check_minimum_elements
        and len(stack) < check_minimum_elements[element]
    ):
        raise StackUnderflowError("Insufficient number of items in stack")

    if element.lstrip("-").isdigit() and element != "-":
        stack.append(int(element))
        return stack

    if element == "dup":
        stack.append(stack[-1])
    elif element == "swap":
        stack[-1], stack[-2] = stack[-2], stack[-1]
    elif element == "drop":
        stack.pop()
    elif element == "over":
        stack.append(stack[-2])
    elif element in "+-*/":
        if element == "/" and stack[-1] == 0:
            raise ZeroDivisionError("divide by zero")
        stack = stack[:-2] + [OPERATOR_DICT[element](stack[-2], stack[-1])]
    else:
        raise ValueError("undefined operation")
    return stack


def _is_int_token(token: str) -> bool:
    return token.lstrip("-").isdigit() and token != "-"


def _execute_token(
    stack: List[int], token: str, words: Dict[str, List[str]]
) -> List[int]:
    if token in words:
        for subtoken in words[token]:
            stack = _execute_token(stack, subtoken, words)
        return stack
    if _is_int_token(token):
        stack.append(int(token))
        return stack
    if token in {"dup", "swap", "drop", "over", "+", "-", "*", "/"}:
        return update_stack(stack, token)
    raise ValueError("undefined operation")


def evaluate(input_data: List[str]) -> List[int]:
    stack: List[int] = []
    words: Dict[str, List[str]] = {}

    for command in input_data:
        tokens = command.lower().split()
        if not tokens:
            continue
        if tokens[0] == ":":
            if len(tokens) < 4 or tokens[-1] != ";":
                raise ValueError("illegal operation")
            name = tokens[1]
            if _is_int_token(name):
                raise ValueError("illegal operation")
            body = []
            previous_definition = words.get(name, [])
            for token in tokens[2:-1]:
                if token in words and token != name:
                    body.extend(words[token])
                elif token == name and previous_definition:
                    body.extend(previous_definition)
                else:
                    body.append(token)
            words[name] = body
            continue

        for token in tokens:
            stack = _execute_token(stack, token, words)
    return stack
