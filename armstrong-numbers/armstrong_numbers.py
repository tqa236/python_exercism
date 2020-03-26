def is_armstrong_number(number: int) -> bool:
    return sum([int(d) ** len(str(number)) for d in str(number)]) == number
