from .config_file import get_config, save_to_config

__CREDENTIALS_KEYS = {"api_token": "API_TOKEN"}


def set_api_token(api_token):
    api_token_key = __CREDENTIALS_KEYS["api_token"]

    credentials = get_config()

    credentials[api_token_key] = api_token

    save_to_config(credentials)


def get_api_token():
    credentials = get_config()

    return credentials[__CREDENTIALS_KEYS["api_token"]]
