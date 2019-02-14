def is_triangle(sides):
    return min(sides) > 0 and sum(sides) > 2 * max(sides)


def is_equilateral(sides):
    return is_triangle(sides) and min(sides) == max(sides)


def is_isosceles(sides):
    return is_triangle(sides) and not is_scalene(sides)


def is_scalene(sides):
    return is_triangle(sides) and (len(set(sides)) == 3)
