from operator import add, mul, sub
from operator import truediv as div


def answer(question: str) -> None:
    elements = (
        question.strip("?")
        .replace("plus", "+")
        .replace("minus", "-")
        .replace("divided by", "/")
        .replace("multiplied by", "*")
        .split()
    )
    if (elements[0], elements[1]) != ("What", "is"):
        raise ValueError("unknown operation")
    operator_dict = {"+": add, "-": sub, "/": div, "*": mul}
    elements = elements[2:]
    try:
        elements = [
            element if element in operator_dict else int(element)
            for element in elements
        ]
    except ValueError:
        raise ValueError("unknown operation")
    if (
        len(elements) % 2 == 0
        or not all(isinstance(element, int) for element in elements[::2])
        or not all(element in operator_dict for element in elements[1::2])
    ):
        raise ValueError("syntax error")
    result = int(elements[0])
    for operator, operand in zip(elements[1::2], elements[2::2]):
        result = operator_dict[operator](result, int(operand))
    return result
