"""Return the time of one billion seconds from now."""
from datetime import timedelta


from datetime import datetime
def add_gigasecond(moment: datetime) -> datetime:
    """Return the time of one billion seconds from now."""
    return moment + timedelta(seconds=10**9)
