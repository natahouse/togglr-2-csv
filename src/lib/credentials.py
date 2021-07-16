from .config_file import get_config, save_to_config

__CREDENTIALS_KEYS = {"api_token": "API_TOKEN", "username": "USERNAME"}


def set_api_token(api_token):
    api_token_key = __CREDENTIALS_KEYS["api_token"]

    config = get_config()

    config[api_token_key] = api_token

    save_to_config(config)


def get_api_token():
    config = get_config()

    return config[__CREDENTIALS_KEYS["api_token"]]

def set_username(username):
    username_key = __CREDENTIALS_KEYS["name"]

    config = get_config()

    config[username_key] = username

    save_to_config(config)

def get_username():
    config = get_config()

    return config[__CREDENTIALS_KEYS["username"]]
