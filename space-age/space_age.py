"""Find the ages of the planets in the Solar system."""
from typing import Callable, Union

YEAR_SECONDS = 31557600

YEAR_MAP = {
    "earth": 1,
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
}


class SpaceAge(object):
    def __init__(self, seconds: Union[float, int]) -> None:
        self.seconds = seconds


def on_planet(r: Union[float, int]) -> Callable:
    def inner(self):
        return round(self.seconds / YEAR_SECONDS / r, 2)

    return inner


for k, v in YEAR_MAP.items():
    setattr(SpaceAge, "on_{}".format(k), on_planet(v))
