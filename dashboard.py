import tkinter as tk
from tkinter import font
import subprocess

# -------------------------
# Functions
# -------------------------
def new_ticket():
    subprocess.Popen(["python", "app.py"])

def history():
    subprocess.Popen(["python", "history.py"])

def statistics():
    subprocess.Popen(["python", "statistics.py"])

def exit_app():
    root.destroy()

# -------------------------
# Window
# -------------------------
root = tk.Tk()

root.title("Support Ticket Management System")
root.geometry("1000x600")
root.configure(bg="#f5f5f5")

# -------------------------
# Sidebar
# -------------------------
sidebar = tk.Frame(root, bg="#2C3E50", width=220)
sidebar.pack(side="left", fill="y")

title = tk.Label(
    sidebar,
    text="HELP DESK",
    bg="#2C3E50",
    fg="white",
    font=("Arial", 20, "bold")
)
title.pack(pady=30)

btn1 = tk.Button(
    sidebar,
    text="📝 New Ticket",
    font=("Arial",12),
    bg="#34495E",
    fg="white",
    width=20,
    command=new_ticket
)
btn1.pack(pady=10)

btn2 = tk.Button(
    sidebar,
    text="📂 Ticket History",
    font=("Arial",12),
    bg="#34495E",
    fg="white",
    width=20,
    command=history
)
btn2.pack(pady=10)

btn3 = tk.Button(
    sidebar,
    text="📊 Statistics",
    font=("Arial",12),
    bg="#34495E",
    fg="white",
    width=20,
    command=statistics
)
btn3.pack(pady=10)

btn4 = tk.Button(
    sidebar,
    text="🚪 Exit",
    font=("Arial",12),
    bg="#E74C3C",
    fg="white",
    width=20,
    command=exit_app
)
btn4.pack(side="bottom", pady=20)

# -------------------------
# Main Area
# -------------------------
main = tk.Frame(root, bg="#f5f5f5")
main.pack(fill="both", expand=True)

heading = tk.Label(
    main,
    text="Support Ticket Management Dashboard",
    font=("Arial",22,"bold"),
    bg="#f5f5f5",
    fg="#2C3E50"
)

heading.pack(pady=30)

card1 = tk.LabelFrame(
    main,
    text="Welcome",
    font=("Arial",12,"bold"),
    padx=20,
    pady=20
)

card1.pack(pady=20)

msg = tk.Label(
    card1,
    text="Manage and classify support tickets using AI.",
    font=("Arial",13)
)

msg.pack()

root.mainloop()