from typing import TypedDict
from .get_time_entries import TimeEntry
from .date import togglr_date_to_dict


class NHEntry(TypedDict):
    day: str
    start: str
    end: str
    description: str
    is_task: bool


NH_ENTRY_HEADER = [
    "day",
    "start",
    "end",
    "description",
    "is_task",
]


def time_entry_2_nh_entry(time_entry: TimeEntry, tag_to_be_task: str) -> NHEntry:
    start_date = togglr_date_to_dict(time_entry["start"])
    end_date = togglr_date_to_dict(time_entry["stop"])
    description = "Sem Descrição"
    if 'description' in time_entry:
        description = time_entry["description"]
    tags = []
    if 'tags' in time_entry:
        tags = time_entry["tags"]

    nh_entry = {
        "day": f"{start_date['day']}/{start_date['month']}",
        "start": f"{start_date['hours']}:{start_date['minutes']}",
        "end": f"{end_date['hours']}:{end_date['minutes']}",
        "description": description,
        "is_task": True if tag_to_be_task in tags else False,
    }

    return nh_entry
