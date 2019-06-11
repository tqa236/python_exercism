"""Find the score of a dart game."""
import math
from typing import Union


def score(x_coordinate: Union[float, int], y_coordinate: Union[float, int]) -> int:
    """Return the score of a dart game based on the distance."""
    distance = math.sqrt(x_coordinate**2 + y_coordinate**2)
    if distance > 10:
        return 0
    if distance > 5:
        return 1
    if distance > 1:
        return 5
    return 10
