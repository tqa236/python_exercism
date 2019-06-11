"""Return the time of one billion seconds from now."""
from datetime import datetime, timedelta


def add_gigasecond(moment: datetime) -> datetime:
    """Return the time of one billion seconds from now."""
    return moment + timedelta(seconds=10**9)
