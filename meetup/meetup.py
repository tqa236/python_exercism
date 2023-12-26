"""Return the meeting day given some conditions."""
import datetime
from calendar import monthrange


def next_weekday(day: datetime.date, weekday: int) -> datetime.date:
    """Find the nearest day in the future of a weekday type."""
    days_ahead = weekday - day.weekday()
    if days_ahead < 0:
        days_ahead += 7
    return day + datetime.timedelta(days_ahead)


def meetup(year: int, month: int, which: str, day_of_the_week: str) -> datetime.date:
    """Return the meeting day given some conditions."""
    last_day_of_month = monthrange(year, month)[1]
    days_of_the_week = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }
    start_days = {
        "first": 1,
        "second": 8,
        "third": 15,
        "fourth": 22,
        "fifth": 29,
        "teenth": 13,
        "last": last_day_of_month - 6,
    }
    if start_days[which] > last_day_of_month:
        raise MeetupDayException("That day does not exist.")
    start = datetime.date(year, month, start_days[which])
    chosen_day = next_weekday(start, days_of_the_week[day_of_the_week])
    if chosen_day.month != month:
        raise MeetupDayException("That day does not exist.")
    return chosen_day


class MeetupDayException(Exception):
    """A custom exception."""

    pass
