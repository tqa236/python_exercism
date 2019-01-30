year_seconds = 31557600

year_map = {
    'earth': 1,
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132,
}


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds


def on_planet(r):
    def inner(self):
        return round(self.seconds / year_seconds / r, 2)
    return inner


for k, v in year_map.items():
    setattr(SpaceAge, "on_{}".format(k), on_planet(v))
