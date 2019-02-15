"""Find the kind of a triangle."""


def is_triangle(sides):
    """Check if the sides satisfied the triangle inequility."""
    return min(sides) > 0 and sum(sides) > 2 * max(sides)


def is_equilateral(sides):
    """Check if the triangle is equilateral."""
    return is_triangle(sides) and min(sides) == max(sides)


def is_isosceles(sides):
    """Check if the triangle is isosceles."""
    return is_triangle(sides) and not is_scalene(sides)


def is_scalene(sides):
    """Check if the triangle is scalene."""
    return is_triangle(sides) and (len(set(sides)) == 3)
