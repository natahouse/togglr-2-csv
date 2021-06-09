from PyInquirer import prompt
from pprint import pprint

from .validations import is_required
from lib.credentials import set_api_token

questions = [
    {
        "type": "input",
        "name": "api_token",
        "message": "Type your API Token: (You can get at: https://track.toggl.com/profile)",
        "validate": is_required("API Token is required"),
    },
]


def save_credentials():
    answers = prompt(questions)
    api_token = answers["api_token"]

    set_api_token(api_token)
