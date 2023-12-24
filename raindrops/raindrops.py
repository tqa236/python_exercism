"""Return the sound of raindrops for a given number."""


def convert(number: int) -> str:
    """Return the sound of raindrops for a given number."""
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    drops = "".join(
        [value for key, value in sorted(sounds.items()) if number % key == 0]
    )
    return drops or str(number)
