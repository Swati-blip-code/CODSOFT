import tkinter as tk
from tkinter import messagebox
import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts():
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and phone are required!")
        return

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts()
    refresh_contact_list()
    clear_fields()
    messagebox.showinfo("Success", f"Contact '{name}' added!")

def refresh_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in sorted(contacts):
        contact_listbox.insert(tk.END, f"{name} - {contacts[name]['Phone']}")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contact():
    query = search_entry.get().strip().lower()
    contact_listbox.delete(0, tk.END)
    for name, details in contacts.items():
        if query in name.lower() or query in details["Phone"]:
            contact_listbox.insert(tk.END, f"{name} - {details['Phone']}")

def on_select(event):
    if not contact_listbox.curselection():
        return
    selected = contact_listbox.get(contact_listbox.curselection())
    name = selected.split(" - ")[0]
    details = contacts[name]

    name_entry.delete(0, tk.END)
    name_entry.insert(0, name)

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, details["Phone"])

    email_entry.delete(0, tk.END)
    email_entry.insert(0, details["Email"])

    address_entry.delete(0, tk.END)
    address_entry.insert(0, details["Address"])

def update_contact():
    name = name_entry.get().strip()
    if name not in contacts:
        messagebox.showwarning("Not Found", "Contact not found.")
        return
    contacts[name]["Phone"] = phone_entry.get().strip()
    contacts[name]["Email"] = email_entry.get().strip()
    contacts[name]["Address"] = address_entry.get().strip()
    save_contacts()
    refresh_contact_list()
    messagebox.showinfo("Updated", f"Contact '{name}' updated!")

def delete_contact():
    name = name_entry.get().strip()
    if name in contacts:
        del contacts[name]
        save_contacts()
        refresh_contact_list()
        clear_fields()
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

root = tk.Tk()
root.title("Contact Book - Starry Night 🌌")
root.configure(bg="#0a0f3d")

contacts = load_contacts()

frame = tk.Frame(root, bg="#0a0f3d")
frame.pack(pady=10)

label_fg = "#c9d1ff"
entry_bg = "#1a1f4a"
entry_fg = "#ffffff"

tk.Label(frame, text="Name:", bg="#0a0f3d", fg=label_fg).grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, width=30, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Phone:", bg="#0a0f3d", fg=label_fg).grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(frame, width=30, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
phone_entry.grid(row=1, column=1)

tk.Label(frame, text="Email:", bg="#0a0f3d", fg=label_fg).grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(frame, width=30, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
email_entry.grid(row=2, column=1)

tk.Label(frame, text="Address:", bg="#0a0f3d", fg=label_fg).grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(frame, width=30, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
address_entry.grid(row=3, column=1)

btn_frame = tk.Frame(root, bg="#0a0f3d")
btn_frame.pack()

tk.Button(btn_frame, text="Add", command=add_contact, bg="#2f3a91", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=update_contact, bg="#2f3a91", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_contact, bg="#2f3a91", fg="white").grid(row=0, column=2, padx=5)

search_frame = tk.Frame(root, bg="#0a0f3d")
search_frame.pack(pady=5)

tk.Label(search_frame, text="Search:", bg="#0a0f3d", fg=label_fg).pack(side="left")
search_entry = tk.Entry(search_frame, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
search_entry.pack(side="left", padx=5)
tk.Button(search_frame, text="Find", command=search_contact, bg="#2f3a91", fg="white").pack(side="left")

contact_listbox = tk.Listbox(root, width=50, bg="#101540", fg="white", selectbackground="#2f3a91")
contact_listbox.pack(pady=10)
contact_listbox.bind("<<ListboxSelect>>", on_select)

refresh_contact_list()
root.mainloop()