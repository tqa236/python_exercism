"""Return the sound of raindrops for a given number."""


def raindrops(number):
    """Return the sound of raindrops for a given number."""
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    drops = "".join([sounds[i] for i in [3, 5, 7] if number % i == 0])
    return drops if drops else str(number)
