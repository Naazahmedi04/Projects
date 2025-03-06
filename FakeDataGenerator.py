import tkinter as tk
from tkinter import messagebox, filedialog
import json
from faker import Faker
import pyperclip

fake = Faker()

def generate_fake_data():
    """Generate fake name, email, and address"""
    name_var.set(fake.name())
    email_var.set(fake.email())
    address_var.set(fake.address().replace("\n", ", "))

def generate_fun_name():
    """Generate a fun random name"""
    fun_names = ["Captain Thunder", "Sir Giggles", "Dr. Whiz", "Miss Zany", "Professor Quirk"]
    name_var.set(fake.random_element(fun_names))

def copy_to_clipboard(text):
    """Copy text to clipboard and show message"""
    pyperclip.copy(text)
    messagebox.showinfo("Copied!", "Copied to clipboard")

def export_to_json():
    """Save generated data as JSON file"""
    data = {
        "name": name_var.get(),
        "email": email_var.get(),
        "address": address_var.get()
    }
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Success", "Data saved successfully!")

def apply_theme(theme):
    """Change the background and text colors based on theme"""
    colors = {"Tech Blue": ("#0A1931", "red"), "Paper Theme": ("#F5DEB3", "black")}
    bg_color, fg_color = colors[theme]
    root.configure(bg=bg_color)
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Button, tk.Label)):
            widget.configure(bg=bg_color, fg=fg_color, highlightbackground=bg_color, font=("Arial", 12, "bold"))
            widget.configure(activeforeground=fg_color, activebackground=bg_color)
            widget.configure(relief="solid", bd=2)
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)


root = tk.Tk()
root.title("Fake Data Generator")
root.geometry("600x600")


name_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()

tk.Label(root, text="Fake Name:").pack()
tk.Entry(root, textvariable=name_var, width=40).pack()
tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(name_var.get())).pack()

tk.Label(root, text="Fake Email:").pack()
tk.Entry(root, textvariable=email_var, width=40).pack()
tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(email_var.get())).pack()

tk.Label(root, text="Fake Address:").pack()
tk.Entry(root, textvariable=address_var, width=40).pack()
tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(address_var.get())).pack()

tk.Button(root, text="Generate Data", command=generate_fake_data).pack(pady=5)
tk.Button(root, text="Surprise Me!", command=generate_fun_name).pack(pady=5)
tk.Button(root, text="Save as JSON", command=export_to_json).pack()

tk.Label(root, text="Choose Theme:").pack()
tk.Button(root, text="Tech Blue", command=lambda: apply_theme("Tech Blue")).pack()
tk.Button(root, text="Paper Theme", command=lambda: apply_theme("Paper Theme")).pack()

root.mainloop()