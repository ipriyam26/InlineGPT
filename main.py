from pynput import keyboard
import pyautogui

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
        sentence = "".join(keystrokes).strip()
        # convert all spaces to single space and remove all spaces at the end
        sentence = re.sub(' +', ' ', sentence)
        words = len(sentence.split(" "))
        for _ in range(words+2):
            pyautogui.hotkey('option', 'backspace')
        stt = "Please wait while I think..."
        pyautogui.write(stt)
        ans = chat(sentence)
        for _ in stt.split(" ")+["GPT:"]:
            pyautogui.hotkey('option', 'backspace')
        keystrokes.clear()
        querying = False
        pyautogui.typewrite(ans)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
