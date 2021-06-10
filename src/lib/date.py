from datetime import datetime
import re


def create_togglr_date(date):
    now = datetime.now().astimezone()

    timezone_offset = now.strftime("%z")
    signal = timezone_offset[0]
    hours = timezone_offset[1:3]
    minutes = timezone_offset[3:5]

    signal = "+" if signal == "-" else "-"

    timezone_offset = f"{signal}{hours}:{minutes}"

    return f"{date}T00:00:00{timezone_offset}"


def togglr_date_to_dict(date: str):
    match = re.search(
        "(?P<year>\d{4})-"
        + "(?P<month>\d{2})-"
        + "(?P<day>\d{2})T"
        + "(?P<hours>\d{2}):"
        + "(?P<minutes>\d{2}):"
        + "(?P<seconds>\d{2})",
        date,
    )

    if match == None:
        return {
            "year": 0000,
            "month": 00,
            "day": 00,
            "hours": 00,
            "minutes": 00,
            "seconds": 00,
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
