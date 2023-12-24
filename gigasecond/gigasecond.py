from datetime import datetime, timedelta


def add(moment: datetime) -> datetime:
    """Return the time of one billion seconds from now."""
    return moment + timedelta(seconds=10**9)
