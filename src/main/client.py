import contextlib
from pynput import keyboard
import pyautogui
import pyperclip
from api.gpt import chat
from helper.help import paste
from src.utils.file_utils import remove_stop_signal, should_stop


keystrokes = []
querying = False

def on_press(key):
    global keystrokes
    global querying
    try:

        if key == keyboard.Key.space:
            keystrokes.append(" ")
        elif key.char != None:
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
        sentence = "".join(keystrokes).strip()

        for _ in range(len(sentence)+4):
            pyautogui.press('backspace')

        stt = "Please wait while I think..."
        pyautogui.typewrite(stt)
        
        try:
            ans = chat(sentence)
        except Exception:
            ans = "I am sorry, There is some internal. Please try again."

        for _ in stt:
            pyautogui.press('backspace')

        keystrokes.clear()
        querying = False
        
        
        # Copy the answer to the clipboard and paste it
        pyperclip.copy(ans)
        paste()
        


def run_client():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while not should_stop():
            listener.join(1)  # Check for the stop signal every 1 second
        remove_stop_signal()

if __name__ == "__main__":
    run_client()