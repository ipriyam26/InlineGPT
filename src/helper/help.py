import sys
import pyautogui
import pyperclip


def paste():
    # check if the clipboard is empty
    if not pyperclip.paste() :
        return
    
    if sys.platform == "darwin":
        pyautogui.hotkey('command', 'v')
    else:
        pyautogui.hotkey('ctrl', 'v')