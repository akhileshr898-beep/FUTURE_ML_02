import tkinter as tk
from tkinter import messagebox
import subprocess

# -----------------------------
# Login Function
# -----------------------------
def login():

    username = txt_username.get().strip()
    password = txt_password.get().strip()

    if username == "admin" and password == "admin123":

        messagebox.showinfo(
            "Login",
            "Login Successful!"
        )

        root.destroy()

        subprocess.Popen(["python", "dashboard.py"])

    else:

        messagebox.showerror(
            "Login Failed",
            "Invalid Username or Password"
        )


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Support Ticket Management System")

root.geometry("600x400")

root.configure(bg="#F4F6F9")

# -----------------------------
# Heading
# -----------------------------
heading = tk.Label(
    root,
    text="Support Ticket Management System",
    font=("Arial", 20, "bold"),
    bg="#F4F6F9",
    fg="#1F4E79"
)

heading.pack(pady=20)

# -----------------------------
# Login Frame
# -----------------------------
frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="ridge"
)

frame.pack(pady=20, padx=40)

# Username
tk.Label(
    frame,
    text="Username",
    bg="white",
    font=("Arial", 12)
).pack(pady=8)

txt_username = tk.Entry(
    frame,
    width=30,
    font=("Arial", 12)
)

txt_username.pack()

# Password
tk.Label(
    frame,
    text="Password",
    bg="white",
    font=("Arial", 12)
).pack(pady=8)

txt_password = tk.Entry(
    frame,
    show="*",
    width=30,
    font=("Arial", 12)
)

txt_password.pack()

# Login Button
login_btn = tk.Button(
    frame,
    text="LOGIN",
    bg="#2563EB",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18,
    command=login
)

login_btn.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="AI-Based Support Ticket Classification System",
    bg="#F4F6F9",
    fg="gray",
    font=("Arial", 10)
)

footer.pack(side="bottom", pady=10)

root.mainloop()