import os


def should_stop():
    return os.path.exists("src/config/stop_signal.tmp")


def create_stop_signal():
    with open("src/config/stop_signal.tmp", "w") as stop_signal:
        stop_signal.write("stop")


def remove_stop_signal():
    if should_stop():
        os.remove("src/config/stop_signal.tmp")
