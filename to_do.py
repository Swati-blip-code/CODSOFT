import tkinter as tk
from tkinter import messagebox, font

# --- Add Task ---
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# --- Delete Task ---
def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected[0])
    except:
        messagebox.showwarning("Select Error", "Please select a task to delete.")

# --- Mark as Done ---
def mark_done():
    try:
        selected = task_listbox.curselection()
        task = task_listbox.get(selected[0])
        task_listbox.delete(selected[0])
        task_listbox.insert(tk.END, "✔️ " + task)
    except:
        messagebox.showwarning("Select Error", "Please select a task to mark as done.")

# --- GUI Setup ---
root = tk.Tk()
root.title("🐰 To-Do List")
root.geometry("400x500")
root.config(bg="#FFFAF0")

# --- Fonts and Styling ---
cute_font = font.Font(family="Comic Sans MS", size=12)
title_label = tk.Label(root, text="📝 My To-Do List", font=("Comic Sans MS", 18, "bold"), bg="#FFFAF0", fg="#EFA4EF")
title_label.pack(pady=10)

# --- Task Entry ---
task_entry = tk.Entry(root, font=cute_font, width=25, bd=3)
task_entry.pack(pady=10)

# --- Buttons ---
button_frame = tk.Frame(root.config(bg="#FFF0F5"))
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", font=cute_font, bg="#FFB6C1", width=10, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(button_frame, text="Delete", font=cute_font, bg="#FFB6C1", width=10, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

done_btn = tk.Button(button_frame, text="Mark Done", font=cute_font, bg="#FFB6C1", width=10, command=mark_done)
done_btn.grid(row=0, column=2, padx=5)

# --- Listbox for Tasks ---
task_listbox = tk.Listbox(root, font=cute_font, width=30, height=12, bd=3, fg="#555")
task_listbox.pack(pady=20)

# --- Start App ---
root.mainloop()
