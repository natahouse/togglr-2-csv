from typing import TypedDict

from lib.credentials import get_username
from .get_time_entries import TimeEntry
from .date import get_week_of_month, is_weekend, togglr_date_to_dict, get_weekday


class NHEntry(TypedDict):
    day: str
    start: str
    end: str
    description: str
    is_task: bool


NH_ENTRY_HEADER = [
    "day",
    "weekday",
    "is_weekend",
    "weekday",
    "responsible",
    "is_task",
    "start",
    "end",
    "description",
]


def time_entry_2_nh_entry(time_entry: TimeEntry, tag_to_be_task: str) -> NHEntry:
    start_date = togglr_date_to_dict(time_entry["start"])
    end_date = togglr_date_to_dict(time_entry["stop"])
    description = "Sem Descrição"
    if "description" in time_entry:
        description = time_entry["description"]
    tags = []
    if "tags" in time_entry:
        tags = time_entry["tags"]
    weekend = (
        "Fim de semana" if is_weekend(time_entry["start"]) == True else "Dia de semana"
    )
    responsible = get_username()

    nh_entry = {
        "day": f"{start_date['day']}/{start_date['month']}",
        "weekday": get_weekday(time_entry["start"]),
        "is_weekend": weekend,
        "week_of_month": get_week_of_month(time_entry["start"]),
        "responsible": responsible,
        "is_task": "Tarefa" if tag_to_be_task in tags else "Justificativa",
        "start": f"{start_date['hours']}:{start_date['minutes']}",
        "end": f"{end_date['hours']}:{end_date['minutes']}",
        "description": description,
    }

    return nh_entry
