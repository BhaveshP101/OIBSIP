import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4.")
        return

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")

# Password length
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
length_var = tk.IntVar(value=12)
tk.Entry(root, textvariable=length_var).grid(row=0, column=1, padx=5, pady=5)

# Checkboxes for complexity
uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=1, column=0, columnspan=2, padx=5, pady=5)

digits_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

symbols_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Generate and copy buttons
tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2, pady=10)
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
