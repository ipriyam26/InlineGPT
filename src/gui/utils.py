import tkinter as tk

def create_labeled_input(parent, label_text, row, entry_width=50, padx=(0, 0), pady=(0, 0)):
    label = tk.Label(parent, text=label_text)
    label.grid(row=row, column=0, padx=padx, pady=pady, sticky="e")

    entry = tk.Entry(parent, width=entry_width)
    entry.grid(row=row, column=1, pady=pady)

    return entry