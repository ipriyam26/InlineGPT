import configparser


def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config.get("Credentials", "API_KEY")
