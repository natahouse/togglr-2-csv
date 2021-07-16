from .config_file import config_file_to_dict, dict_to_config_file

__CREDENTIALS_KEYS = {"api_token": "API_TOKEN"}


def set_api_token(api_token):
    api_token_key = __CREDENTIALS_KEYS["api_token"]

    credentials = config_file_to_dict()

    credentials[api_token_key] = api_token

    dict_to_config_file(credentials)


def get_api_token():
    credentials = config_file_to_dict()

    return credentials[__CREDENTIALS_KEYS["api_token"]]
