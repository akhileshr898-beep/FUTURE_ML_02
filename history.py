import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ----------------------------
# Load Data
# ----------------------------
def load_data():

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ticket_history")

    rows = cursor.fetchall()

    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()


# ----------------------------
# Search Ticket
# ----------------------------
def search_ticket():

    keyword = search_entry.get()

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM ticket_history
        WHERE ticket LIKE ?
        OR category LIKE ?
        OR priority LIKE ?
        """,
        (
            "%" + keyword + "%",
            "%" + keyword + "%",
            "%" + keyword + "%"
        )
    )

    rows = cursor.fetchall()

    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()


# ----------------------------
# Delete Ticket
# ----------------------------
def delete_ticket():

    selected = tree.focus()

    if selected == "":
        messagebox.showwarning(
            "Warning",
            "Please select a ticket."
        )
        return

    values = tree.item(selected, "values")

    ticket_id = values[0]

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM ticket_history WHERE id=?",
        (ticket_id,)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Success",
        "Ticket deleted successfully!"
    )

    load_data()


# ----------------------------
# Update Ticket
# ----------------------------
def update_ticket():

    selected = tree.focus()

    if selected == "":
        messagebox.showwarning(
            "Warning",
            "Please select a ticket."
        )
        return

    values = tree.item(selected, "values")

    ticket_id = values[0]

    edit = tk.Toplevel(root)

    edit.title("Update Ticket")

    edit.geometry("350x250")

    tk.Label(edit, text="Category").pack(pady=5)

    category_entry = tk.Entry(edit, width=30)
    category_entry.insert(0, values[2])
    category_entry.pack()

    tk.Label(edit, text="Priority").pack(pady=5)

    priority_entry = tk.Entry(edit, width=30)
    priority_entry.insert(0, values[3])
    priority_entry.pack()

    def save_changes():

        conn = sqlite3.connect("tickets.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE ticket_history
            SET category=?, priority=?
            WHERE id=?
            """,
            (
                category_entry.get(),
                priority_entry.get(),
                ticket_id
            )
        )

        conn.commit()
        conn.close()

        edit.destroy()

        load_data()

        messagebox.showinfo(
            "Success",
            "Ticket updated successfully!"
        )

    tk.Button(
        edit,
        text="Save Changes",
        bg="green",
        fg="white",
        command=save_changes
    ).pack(pady=20)


# ----------------------------
# Main Window
# ----------------------------

root = tk.Tk()

root.title("Support Ticket History")

root.geometry("950x550")

title = tk.Label(
    root,
    text="Support Ticket History",
    font=("Arial",18,"bold")
)

title.pack(pady=10)

# Search Frame
search_frame = tk.Frame(root)

search_frame.pack(pady=5)

search_entry = tk.Entry(
    search_frame,
    width=40
)

search_entry.pack(side=tk.LEFT, padx=5)

search_btn = tk.Button(
    search_frame,
    text="Search",
    command=search_ticket
)

search_btn.pack(side=tk.LEFT)

refresh_btn = tk.Button(
    search_frame,
    text="Refresh",
    command=load_data
)

refresh_btn.pack(side=tk.LEFT, padx=5)

# Table
tree = ttk.Treeview(
    root,
    columns=("ID", "Ticket", "Category", "Priority"),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Ticket", text="Ticket")
tree.heading("Category", text="Category")
tree.heading("Priority", text="Priority")

tree.column("ID", width=50)
tree.column("Ticket", width=500)
tree.column("Category", width=150)
tree.column("Priority", width=100)

tree.pack(fill="both", expand=True, pady=10)

# Buttons
button_frame = tk.Frame(root)

button_frame.pack(pady=10)

update_btn = tk.Button(
    button_frame,
    text="Update Selected",
    bg="green",
    fg="white",
    width=20,
    command=update_ticket
)

update_btn.pack(side=tk.LEFT, padx=10)

delete_btn = tk.Button(
    button_frame,
    text="Delete Selected",
    bg="red",
    fg="white",
    width=20,
    command=delete_ticket
)

delete_btn.pack(side=tk.LEFT, padx=10)

# Load all records
load_data()

root.mainloop()