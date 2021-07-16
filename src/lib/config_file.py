import re
from os import path
from pathlib import Path

__TOGGLER_CONFIG_PATH = "~/.togglr"
__ABSOLUTE_TOGGLER_CONFIG_PATH = path.expanduser(__TOGGLER_CONFIG_PATH)

__DEFAULT_CONFIG_FILE_PATH = f"{__ABSOLUTE_TOGGLER_CONFIG_PATH}/credentials"

def __check_file_exists():
    return path.exists(__DEFAULT_CONFIG_FILE_PATH)


def config_file_to_dict():
    if not __check_file_exists():
        Path(__ABSOLUTE_TOGGLER_CONFIG_PATH).mkdir(parents=True, exist_ok=True)
        open(__DEFAULT_CONFIG_FILE_PATH, "a").close()

    config_file = open(__DEFAULT_CONFIG_FILE_PATH, "r")

    configs = config_file.read().replace("\r", "").split("\n")

    config_file.close()

    config_dict = {}

    for config in configs:
        match = re.search("(?P<key>[a-zA-Z_]+)=(?P<value>[a-zA-Z0-9 ]+)", config)

        if match == None:
            pass
        else:
            key = match.group("key")
            value = match.group("value")

            config_dict[key] = value

    return config_dict


def dict_to_config_file(dict):
    config = ""

    for key in dict:
        config += f"{key}={dict[key]}\n"

    config_file = open(__DEFAULT_CONFIG_FILE_PATH, "w")
    config_file.write(config)
    config_file.close()
