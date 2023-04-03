import sys
import pyautogui
import pyperclip
from pynput import keyboard


def getModifier():
    if sys.platform == "darwin":
        return keyboard.Key.cmd
    else:
        return keyboard.Key.ctrl


def paste():
    # check if the clipboard is empty
    if not pyperclip.paste():
        return

    if sys.platform == "darwin":
        pyautogui.hotkey('command', 'v')
    else:
        pyautogui.hotkey('ctrl', 'v')
