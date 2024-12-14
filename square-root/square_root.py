def square_root(n):
    if n == 0 or n == 1:
        return n

    x = n // 2
    while True:
        next_x = (x + n // x) // 2
        if next_x >= x:
            return x
        x = next_x
