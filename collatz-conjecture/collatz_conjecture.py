def steps(number: int) -> int:
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        count = count + 1
    return count
