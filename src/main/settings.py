import configparser

def read_setting(section, key, default_value=None):
    config = configparser.ConfigParser()
    config.read("config.ini")
    try:
        value = config.get(section, key)
    except (configparser.NoSectionError, configparser.NoOptionError):
        value = default_value
    return value

def save_setting(section, key, value):
    config = configparser.ConfigParser()
    config.read("config.ini")
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, key, value)
    with open("config.ini", "w") as configfile:
        config.write(configfile)

def get_api_key():
    return read_setting("Credentials", "API_KEY")

def get_custom_trigger():
    return read_setting("Settings", "CUSTOM_TRIGGER", "GPT:")

def save_api_key(api_key):
    save_setting("Credentials", "API_KEY", api_key)

def save_custom_trigger(custom_trigger):
    save_setting("Settings", "CUSTOM_TRIGGER", custom_trigger)