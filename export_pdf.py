import sqlite3

from reportlab.platypus import SimpleDocTemplate, Table

conn = sqlite3.connect("tickets.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM ticket_history")

rows = cursor.fetchall()

data = [["ID", "Ticket", "Category", "Priority"]]

for row in rows:
    data.append(list(row))

pdf = SimpleDocTemplate("TicketHistory.pdf")

table = Table(data)

pdf.build([table])

conn.close()

print("PDF Created Successfully!")