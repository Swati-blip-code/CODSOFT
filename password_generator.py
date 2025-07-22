import tkinter as tk
from tkinter import messagebox
import random
import string

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
        messagebox.showwarning("Oops!", "Please select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Yay!", "Password copied to clipboard! 💖")

# Setup window
root = tk.Tk()
root.title("🌸 Password Generator")
root.geometry("400x420")
root.config(bg="#fff0f5")

# Fonts
TITLE_FONT = ("Comic Sans MS", 18, "bold")
LABEL_FONT = ("Comic Sans MS", 12)
BUTTON_FONT = ("Comic Sans MS", 11, "bold")
ENTRY_FONT = ("Comic Sans MS", 12)

# Title
tk.Label(root, text="✨ My Password Generator ✨", font=TITLE_FONT, bg="#fff0f5", fg="#d81b60").pack(pady=15)

# Password length
tk.Label(root, text="Password Length:", font=LABEL_FONT, bg="#fff0f5").pack()
length_entry = tk.Entry(root, font=ENTRY_FONT, justify="center")
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=var_upper, bg="#fff0f5", font=LABEL_FONT).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=var_lower, bg="#fff0f5", font=LABEL_FONT).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=var_digits, bg="#fff0f5", font=LABEL_FONT).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Symbols (!@#)", variable=var_symbols, bg="#fff0f5", font=LABEL_FONT).pack(anchor="w", padx=40)

# Generate button
tk.Button(root, text="🌟 Generate Password", command=generate_password, bg="#ff69b4", fg="white", font=BUTTON_FONT, padx=10, pady=5).pack(pady=15)

# Output field
password_entry = tk.Entry(root, width=30, font=ENTRY_FONT, justify="center")
password_entry.pack(pady=10)

# Copy button
tk.Button(root, text="📋 Copy to Clipboard", command=copy_password, bg="#da70d6", fg="white", font=BUTTON_FONT, padx=8, pady=3).pack(pady=5)

root.mainloop()
