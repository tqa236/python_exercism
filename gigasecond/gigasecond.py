"""Return the time of one billion seconds from now."""
from datetime import timedelta


def add_gigasecond(moment):
    """Return the time of one billion seconds from now."""
    return moment + timedelta(seconds=10**9)
