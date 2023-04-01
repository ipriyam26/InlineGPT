import configparser


def get_api_key():
    config = configparser.ConfigParser()
    config.read("src/config/config.ini")
    return config.get("Credentials", "API_KEY")
