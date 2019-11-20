from typing import List


class StackUnderflowError(Exception):
    pass


def evaluate(input_data: List[str]) -> None:
    commands = [command.lower().split() for command in input_data]
    stack = []
    for command in commands:
        for element in command:
            if element.isdigit():
                stack.append(int(element))
            if element == "dup":
                if not stack:
                    raise StackUnderflowError("Not enough value for this operator")
                stack.append(stack[-1])
            if element == "swap":
                if len(stack) < 2:
                    raise StackUnderflowError("Not enough value for this operator")
                stack[-1], stack[-2] = stack[-2], stack[-1]
    return stack
    # return [int(element) for element in input_data[0].split()]
