"""Parse and evaluate simple math word problems."""
from operator import add, mul, sub
from operator import truediv as div


def calculate(question: str) -> None:
    """Parse and evaluate simple math word problems."""
    elements = (
        question.strip("?")
        .replace("plus", "+")
        .replace("minus", "-")
        .replace("divided by", "/")
        .replace("multiplied by", "*")
        .split()
    )
    if (elements[0], elements[1]) != ("What", "is") or len(elements) % 2 == 0:
        raise ValueError("Not a math problem.")
    operator_dict = {"+": add, "-": sub, "/": div, "*": mul}
    if elements[2].lstrip("-").isdigit():
        result = int(elements[2])
    else:
        raise ValueError("No continuous operands")
    for operator, operand in zip(elements[3::2], elements[4::2]):
        try:
            result = operator_dict[operator](result, int(operand))
        except Exception as ex:
            raise ValueError(f"Not a math problem: {ex}")
    return result
