"""Find the kind of a triangle."""


from typing import List, Union


def is_triangle(sides: Union[List[float], List[int]]) -> bool:
    """Check if the sides satisfied the triangle inequility."""
    return min(sides) > 0 and sum(sides) > 2 * max(sides)


def is_equilateral(sides: Union[List[float], List[int]]) -> bool:
    """Check if the triangle is equilateral."""
    return is_triangle(sides) and min(sides) == max(sides)


def is_isosceles(sides: Union[List[float], List[int]]) -> bool:
    """Check if the triangle is isosceles."""
    return is_triangle(sides) and not is_scalene(sides)


def is_scalene(sides: Union[List[float], List[int]]) -> bool:
    """Check if the triangle is scalene."""
    return is_triangle(sides) and (len(set(sides)) == 3)
