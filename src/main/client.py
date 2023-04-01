import contextlib
from multiprocessing import Event
import threading
import time
from pynput import keyboard
import pyautogui
import pyperclip
from api.gpt import chat
from helper.help import paste
from utils.file_utils import remove_stop_signal, should_stop


keystrokes = []
querying = False


def on_press(key):
    global keystrokes
    global querying
    try:

        if key == keyboard.Key.space:
            keystrokes.append(" ")
        elif key.char is not None:
            keystrokes.append(key.char)
    except AttributeError:
        if key == keyboard.Key.backspace and len(keystrokes) > 0:
            keystrokes.pop()

    if not querying and len(keystrokes) > 4:
        keystrokes.pop(0)

    with contextlib.suppress(Exception):
        if "".join(keystrokes) == "GPT:":
            querying = True
            keystrokes.clear()


def on_release(key):
    global keystrokes
    global querying

    if key == keyboard.Key.cmd and querying:
        sentence = "".join(keystrokes)

        for _ in range(len(sentence)+4):
            pyautogui.press('backspace')

        stt = "Please wait while I think..."
        pyautogui.write(stt)
        ans = chat(sentence)
        for _ in stt:
            pyautogui.press('backspace')

        keystrokes.clear()
        querying = False

        # Copy the answer to the clipboard and paste it
        pyperclip.copy(ans)
        paste()


def check_file(stop_event):
    while not stop_event.is_set():
        if should_stop():
            stop_event.set()
            break
        time.sleep(1)


def run_client():
    stop_event = threading.Event()
    check_thread = threading.Thread(target=check_file, args=(stop_event,))
    check_thread.start()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while not stop_event.is_set():
            stop_event.wait(0.1)  # Wait for the stop_event to be set


if __name__ == "__main__":
    # stop_event = Event()
    run_client()
