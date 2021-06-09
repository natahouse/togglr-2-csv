import re
from os import path
from pathlib import Path

__TOGGLER_CONFIG_PATH = "~/.togglr"
__ABSOLUTE_TOGGLER_CONFIG_PATH = path.expanduser(__TOGGLER_CONFIG_PATH)

__DEFAULT_CREDENTIALS_FILE_PATH = f"{__ABSOLUTE_TOGGLER_CONFIG_PATH}/credentials"

__CREDENTIALS_KEYS = {"api_token": "API_TOKEN"}


def __check_file_exists():
    return path.exists(__DEFAULT_CREDENTIALS_FILE_PATH)


def __credential_file_to_dict():
    if not __check_file_exists():
        Path(__ABSOLUTE_TOGGLER_CONFIG_PATH).mkdir(parents=True, exist_ok=True)
        open(__DEFAULT_CREDENTIALS_FILE_PATH, "a").close()

    credentials_file = open(__DEFAULT_CREDENTIALS_FILE_PATH, "r")

    credentials = credentials_file.read().replace("\r", "").split("\n")

    credentials_file.close()

    credentials_dict = {}

    for credential in credentials:
        match = re.search("(?P<key>[a-zA-Z_]+)=(?P<value>[a-zA-Z0-9 ]+)", credential)

        if match == None:
            pass
        else:
            key = match.group("key")
            value = match.group("value")

            credentials_dict[key] = value

    return credentials_dict


def __dict_to_credential_file(dict):
    credentials = ""

    for key in dict:
        credentials += f"{key}={dict[key]}\n"

    credentials_file = open(__DEFAULT_CREDENTIALS_FILE_PATH, "w")
    credentials_file.write(credentials)
    credentials_file.close()


def set_api_token(api_token):
    api_token_key = __CREDENTIALS_KEYS["api_token"]

    credentials = __credential_file_to_dict()

    credentials[api_token_key] = api_token

    __dict_to_credential_file(credentials)


def get_api_token():
    credentials = __credential_file_to_dict()

    return credentials[__CREDENTIALS_KEYS["api_token"]]
