from typing import List, TypedDict
from urllib import parse
from toggl.TogglPy import Toggl
from .credentials import get_api_token


class TimeEntry(TypedDict):
    id: int
    guid: str
    wid: int
    pid: int
    billable: bool
    start: str
    stop: str
    duration: int
    description: str
    tags: List[str]
    duronly: bool
    at: str
    uid: int


def get_time_entries(start_date, end_date) -> List[TimeEntry]:
    toggl = Toggl()
    api_token = get_api_token()
    toggl.setAPIKey(api_token)

    time_entries_base_url = "https://api.track.toggl.com/api/v8/time_entries"
    time_entries_params = parse.urlencode(
        {"start_date": start_date, "end_date": end_date}
    )

    time_entries_url = f"{time_entries_base_url}?{time_entries_params}"

    return toggl.request(time_entries_url)
