from .get_time_entries import TimeEntry
from .date import togglr_date_to_dict


def time_entry_2_nh_entry(time_entry: TimeEntry, tag_to_be_task: str):
    start_date = togglr_date_to_dict(time_entry["start"])
    end_date = togglr_date_to_dict(time_entry["stop"])
    description = time_entry["description"]
    tags = time_entry["tags"]

    nh_entry = {
        "day": f"{start_date['day']}/{start_date['month']}",
        "start": f"{start_date['hours']}:{start_date['minutes']}",
        "end": f"{end_date['hours']}:{end_date['minutes']}",
        "description": description,
        "is_task": True if tag_to_be_task in tags else False,
    }

    return nh_entry
