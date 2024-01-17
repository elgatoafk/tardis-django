def convert(time_input: str, zone: str):
    from dateutil import parser, tz

    try:
        time_input = parser.parse(time_input)
        return time_input.replace(tzinfo=tz.gettz(zone))

    except:
        return None

def difference_calculator(user_time):
    from datetime import datetime
    from dateutil import tz

    if user_time is not None:
        diff = datetime.now(tz=tz.gettz("Europe/London")) - user_time
        return diff
    else:
        return "Incorrect input, please check"

def format_input(time_input):
    return time_input.strftime("%H:%M:%S %d %B %Y (%A)")
