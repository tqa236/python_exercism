"""Find the kind of a triangle."""


from typing import List, Union


def triangle(sides: Union[List[float], List[int]]) -> bool:
    """Check if the sides satisfied the triangle inequility."""
    return min(sides) > 0 and sum(sides) > 2 * max(sides)


def equilateral(sides: Union[List[float], List[int]]) -> bool:
    """Check if the triangle is equilateral."""
    return triangle(sides) and min(sides) == max(sides)


def isosceles(sides: Union[List[float], List[int]]) -> bool:
    """Check if the triangle is isosceles."""
    return triangle(sides) and not scalene(sides)


def scalene(sides: Union[List[float], List[int]]) -> bool:
    """Check if the triangle is scalene."""
    return triangle(sides) and (len(set(sides)) == 3)
