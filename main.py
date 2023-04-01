import time
from pynput import keyboard
import pyautogui,pyperclip

import openai
import os
import dotenv
import re

dotenv.load_dotenv()


def chat(message):
    openai.api_key = os.getenv("API_KEY")
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Be precise and to the point."},
    ]

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    return chat_completion.choices[0].message.content


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

    # check if keystrokes is equal to "GPT:"
    try:
        if "".join(keystrokes) == "GPT:":
            # set querying to true
            querying = True
            keystrokes.clear()
    except Exception:
        print(keystrokes)


def on_release(key):
    global keystrokes
    global querying

    if key == keyboard.Key.cmd and querying:
        # Reset keystrokes list
        sentence = "".join(keystrokes)

        for _ in range(len(sentence)+4):
            pyautogui.press('backspace')

        stt = "Please wait while I think..."

        pyautogui.typewrite(stt, interval=0)
        try:
            ans = chat(sentence)
        except Exception:
            ans = "I am sorry, There is some internal. Please try again."

        for _ in range(len(stt)):
            pyautogui.press('backspace')

        keystrokes.clear()
        querying = False
        pyperclip.copy(ans)
        pyautogui.hotkey('command', 'v')
        # pyautogui.typewrite(ans, interval=0)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
