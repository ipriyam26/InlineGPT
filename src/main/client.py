import contextlib
import threading
import time
from pynput import keyboard
import pyautogui


import pyperclip
from ..api.gpt import chat
from ..helper.help import paste, getModifier
from ..utils.file_utils import should_stop


keystrokes = []
querying = False

modifier = getModifier()


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
        if "".join(keystrokes).upper() == "GPT:":
            querying = True
            keystrokes.clear()


def on_release(key):
    global keystrokes
    global querying

    if key == modifier and querying:
        sentence = "".join(keystrokes)

        for _ in range(len(sentence)+4):
            pyautogui.press('backspace')

        stt = "Please wait while I think..."
        pyautogui.write(stt)
        ans = chat(sentence)
        for _ in stt[1:]:
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


def check_clipboard(stop_event):
    prev_content = ""
    while not stop_event.is_set():
        current_content = pyperclip.paste().strip()
        if current_content != prev_content:
            if current_content.startswith("GPT:"):
                pyperclip.copy("Processing request")
                processed_content = chat(current_content)
                pyperclip.copy(processed_content)
                prev_content = current_content
        time.sleep(1)


def run_client():
    stop_event = threading.Event()
    check_thread = threading.Thread(target=check_file, args=(stop_event,))
    clipboard_thread = threading.Thread(
        target=check_clipboard, args=(stop_event,))
    check_thread.start()
    clipboard_thread.start()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as _:
        while not stop_event.is_set():
            stop_event.wait(0.1)  # Wait for the stop_event to be set


if __name__ == "__main__":
    # stop_event = Event()
    run_client()
