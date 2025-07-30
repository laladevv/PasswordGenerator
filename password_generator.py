import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())

    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.resizable(False, False)

# Widgets
tk.Label(window, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack()
length_entry.insert(0, "12")

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(window, text="Include Uppercase Letters", variable=var_upper).pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Lowercase Letters", variable=var_lower).pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Numbers", variable=var_digits).pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Symbols", variable=var_symbols).pack(anchor="w", padx=20)

tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)

result_entry = tk.Entry(window, font=("Helvetica", 14), justify="center")
result_entry.pack(pady=5)

tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard).pack()

window.mainloop()

#Made by laladevv (ozguxs)
