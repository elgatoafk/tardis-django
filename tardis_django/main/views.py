from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import TimeForm
from datetime import datetime, timedelta
from dateutil import parser, tz
# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

# from tardis_django.main.processing import difference_calculator, convert, format_input, format_results, ConversionError
@csrf_exempt
def main(request):
    if request.method == 'POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            time_zone = form.cleaned_data['time_zone']
            contents = form.cleaned_data['contents']
            try:
                entered_date = convert(contents, time_zone)
                result = difference_calculator(entered_date)
                entered_date = format_input(entered_date)
                result = format_results(
            result, "{d} days, {h} hours, {m} minutes and {s} seconds passed"
        )
                return render(request, 'main.html', {'entered_date': entered_date}, {'result': result}, {'result_zone' : "Results shown for "
            + request.form["time-zone"]
            + " time zone."})
            except ConversionError as e:
                error_message = str(e)
                form.add_error(None, error_message)
            return render(request, 'result.html', {'entered_date': entered_date})
    else:
        form = TimeForm()
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    




class ConversionError(Exception):
    def __init__(self):
        self.message = "Incorrect input, please check"
        super().__init__(self.message)


def convert(time_input: str, zone: str) -> datetime:
    """convert Converts a string representation of time to a datetime object with the specified timezone.

    :param time_input: The string representation of time to convert.
    :type time_input: str
    :param zone: The timezone to apply to the converted datetime object.
    :type zone: str
    :return: The converted datetime object with the specified timezone
    :rtype: datetime
    """

    time_input = parser.parse(time_input)
    return time_input.replace(tzinfo=tz.gettz(zone))


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


def format_results(delta: timedelta, pattern: str) -> str:
    """format_results Formats the given time difference using the specified pattern.

    :param delta: The time difference to format.
    :type delta: timedelta
    :param pattern: The pattern to use for formatting the time difference.
    The pattern can include placeholders for days, hours, minutes, and seconds.
    :type pattern: str
    :return: The formatted time difference.
    :rtype: str
    """
    d = {"d": delta.days}
    d["h"], rem = divmod(delta.seconds, 3600)
    d["m"], d["s"] = divmod(rem, 60)
    return pattern.format(**d)


def format_input(time_input: datetime) -> str:
    """format_input Formats the given datetime object into a specific string representation.

    :param time_input: The datetime object to format.
    :type time_input: datetime
    :return: The formatted string representation of the datetime object.
    :rtype: str
    """
    return time_input.strftime("%H:%M:%S %d %B %Y (%A)")

    