import os


def should_stop():
    return os.path.exists("stop_signal.tmp")


def create_stop_signal():
    with open("stop_signal.tmp", "w") as stop_signal:
        stop_signal.write("stop")


def remove_stop_signal():
    if should_stop():
        os.remove("stop_signal.tmp")
