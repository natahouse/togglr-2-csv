from datetime import datetime, timedelta
from calendar import monthcalendar
import re


def get_local_timezone_offset():
    now = datetime.now().astimezone()

    timezone_offset = now.strftime("%z")
    signal = timezone_offset[0]
    hours = timezone_offset[1:3]
    minutes = timezone_offset[3:5]

    return {
        "signal": signal,
        "hours": hours,
        "minutes": minutes,
    }


def create_togglr_date(date):
    timezone_offset = get_local_timezone_offset()

    timezone_offset_str = (
        f"{timezone_offset['signal']}"
        + f"{timezone_offset['hours']}:"
        + f"{timezone_offset['minutes']}"
    )

    return f"{date}T00:00:00{timezone_offset_str}"


__DATE_REGEX = (
    "(?P<year>\d{4})-"
    + "(?P<month>\d{2})-"
    + "(?P<day>\d{2})T"
    + "(?P<hours>\d{2}):"
    + "(?P<minutes>\d{2}):"
    + "(?P<seconds>\d{2})"
    + "(?P<offset_signal>[+-])"
    + "(?P<offset_hours>\d{2}):"
    + "(?P<offset_minutes>\d{2})"
)


def change_date_to_local_offset(date):
    match = re.search(__DATE_REGEX, date)

    if match == None:
        return date
    else:
        local_off_set = get_local_timezone_offset()
        local_offset_signal = local_off_set["signal"]
        local_offset_hours = local_off_set["hours"]
        local_offset_minutes = local_off_set["minutes"]

        date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")

        local_offset_in_seconds = int(local_offset_hours) * 60 * 60
        local_offset_in_seconds += int(local_offset_minutes) * 60

        if local_offset_signal == "+":
            date_obj += timedelta(seconds=local_offset_in_seconds)
        else:
            date_obj -= timedelta(seconds=local_offset_in_seconds)

        return (
            date_obj.strftime("%Y-%m-%dT%H:%M:%S%z")[:19]
            + f"{local_offset_signal}{local_offset_hours}:{local_offset_minutes}"
        )


def togglr_date_to_dict(date: str):
    date_with_local_offset = change_date_to_local_offset(date)

    match = re.search(__DATE_REGEX, date_with_local_offset)

    if match == None:
        return {
            "year": "0000",
            "month": "00",
            "day": "00",
            "hours": "00",
            "minutes": "00",
            "seconds": "00",
        }
    else:
        return {
            "year": match.group("year"),
            "month": match.group("month"),
            "day": match.group("day"),
            "hours": match.group("hours"),
            "minutes": match.group("minutes"),
            "seconds": match.group("seconds"),
        }


__WEEKDAY_TO_STR = {
    0: "segunda-feira",
    1: "terça-feira",
    2: "quarta-feira",
    3: "quinta-feira",
    4: "sexta-feira",
    5: "sábado",
    6: "domingo",
}


def get_weekday(date: str):
    date_with_local_offset = change_date_to_local_offset(date)

    date_obj = datetime.strptime(date_with_local_offset, "%Y-%m-%dT%H:%M:%S%z")

    return date_obj.weekday()


def get_weekday_str(date: str):
    weekday = get_weekday(date)

    return __WEEKDAY_TO_STR[weekday]


def is_weekend(date: str):
    weekday = get_weekday(date)

    return weekday >= 5


def get_week_of_month(date: datetime):
    day = date.day
    month = date.month
    year = date.year

    return next(
        (
            week_number
            for week_number, days_of_week in enumerate(
                monthcalendar(year, month), start=1
            )
            if day in days_of_week
        ),
        None,
    )


def get_week_of_month_str(date: str):
    date_with_local_offset = change_date_to_local_offset(date)

    date_obj = datetime.strptime(date_with_local_offset, "%Y-%m-%dT%H:%M:%S%z")

    week_of_month = get_week_of_month(date_obj)

    return f"Semana {week_of_month}"
