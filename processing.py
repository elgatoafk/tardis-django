from datetime import datetime, timedelta
from dateutil import parser, tz


def convert(time_input: str, zone: str) -> datetime | None:
    """convert Converts a string representation of time to a datetime object with the specified timezone.

    :param time_input: The string representation of time to convert.
    :type time_input: str
    :param zone: The timezone to apply to the converted datetime object.
    :type zone: str
    :return: The converted datetime object with the specified timezone, or None if the conversion fails.
    :rtype: datetime | None
    """
    try:
        time_input = parser.parse(time_input)
        return time_input.replace(tzinfo=tz.gettz(zone))

    except ValueError:
        return None


def difference_calculator(user_time: datetime) -> timedelta | str:
    """difference_calculator Calculates the difference between the current time and the given user time.

    :param user_time: The user-provided time to calculate the difference from.
    :type user_time: datetime
    :return: The time difference between the current time and the user time.
    :rtype: timedelta
    """
    if user_time is None:
        return "Incorrect input, please check"
    if user_time > datetime.now(tz=tz.gettz("Europe/London")):
        # make an additional alert that the date is in future
        return user_time - datetime.now(tz=tz.gettz("Europe/London"))
    return datetime.now(tz=tz.gettz("Europe/London")) - user_time
