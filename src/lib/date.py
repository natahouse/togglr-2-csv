from datetime import datetime


def create_togglr_date(date):
    now = datetime.now().astimezone()

    timezone_offset = now.strftime("%z")
    signal = timezone_offset[0]
    hour = timezone_offset[1:3]
    minutes = timezone_offset[3:5]

    signal = "+" if signal == "-" else "-"

    timezone_offset = f"{signal}{hour}:{minutes}"

    return f"{date}T00:00:00{timezone_offset}"
