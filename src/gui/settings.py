import sys
import os
import subprocess
import threading
from tkinter import messagebox
import tkinter as tk


from ..main.settings import get_api_key, save_api_key
from ..main.settings import get_custom_trigger, save_custom_trigger
from ..utils.file_utils import create_stop_signal, remove_stop_signal
from ..gui.utils import create_labeled_input
from ..main.client import run_client

# client_thread = threading.Thread(target=run_client, daemon=True)


def save_settings():
    api_key = api_key_entry.get()
    custom_trigger = custom_trigger_entry.get()

    save_api_key(api_key)
    save_custom_trigger(custom_trigger)
    messagebox.showinfo("Success", "Settings saved successfully.")


def stop_script():
    create_stop_signal()
    messagebox.showinfo("Success", "The script will stop shortly.")


def start_script():
    global client_thread
    if not client_thread.is_alive():
        client_thread = threading.Thread(target=run_client, daemon=True)
        client_thread.start()
        messagebox.showinfo("Success", "The script has started.")


# client_thread = None
# stop_event = multiprocessing.Event()

client_process = None


def toggle_script():
    global client_process
    if client_process is None or client_process.poll() is not None:
        run_client_path = os.path.join(os.path.dirname(
            os.path.abspath(sys.argv[0])), "run_client")
        if sys.platform == "win32":
            client_process = subprocess.Popen([f"{run_client_path}.exe"])
        else:
            client_process = subprocess.Popen([f"{run_client_path}"])
        messagebox.showinfo("Success", "The script has started.")
        start_stop_button.config(text="Stop Script", command=toggle_script)
    else:
        create_stop_signal()
        client_process.wait()
        remove_stop_signal()
        messagebox.showinfo("Success", "The script has stopped.")
        start_stop_button.config(text="Start Script", command=toggle_script)


root = tk.Tk()
root.title("GPT-3 Inline Client Settings")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

api_key_entry = create_labeled_input(
    frame, "API Key:", 0, padx=(0, 10), pady=(0, 10))
api_key_entry.insert(0, get_api_key())

custom_trigger_entry = create_labeled_input(
    frame, "Custom Trigger:", 1, padx=(0, 10), pady=(0, 10))
custom_trigger_entry.insert(0, get_custom_trigger())

save_button = tk.Button(frame, text="Save Settings", command=save_settings)
save_button.grid(row=2, columnspan=2, pady=(10, 5))

start_stop_button = tk.Button(
    frame, text="Start Script", command=toggle_script)
start_stop_button.grid(row=4, columnspan=2, pady=(5, 10))
