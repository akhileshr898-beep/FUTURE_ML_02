import sqlite3
import tkinter as tk

# Connect to Database
conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

# Count Tickets
cursor.execute("SELECT COUNT(*) FROM ticket_history")
total = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM ticket_history WHERE category='Network'")
network = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM ticket_history WHERE category='Hardware'")
hardware = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM ticket_history WHERE category='Software'")
software = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM ticket_history WHERE category='Email'")
email = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM ticket_history WHERE category='Account'")
account = cursor.fetchone()[0]

conn.close()

# Create Window
root = tk.Tk()

root.title("Ticket Statistics")

root.geometry("500x350")

title = tk.Label(
    root,
    text="Support Ticket Statistics",
    font=("Arial",16,"bold")
)

title.pack(pady=15)

tk.Label(root,text=f"Total Tickets : {total}",font=("Arial",12)).pack(pady=5)

tk.Label(root,text=f"Network Tickets : {network}",font=("Arial",12)).pack()

tk.Label(root,text=f"Hardware Tickets : {hardware}",font=("Arial",12)).pack()

tk.Label(root,text=f"Software Tickets : {software}",font=("Arial",12)).pack()

tk.Label(root,text=f"Email Tickets : {email}",font=("Arial",12)).pack()

tk.Label(root,text=f"Account Tickets : {account}",font=("Arial",12)).pack()

root.mainloop()