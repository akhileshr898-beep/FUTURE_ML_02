import sqlite3
from openpyxl import Workbook

conn = sqlite3.connect("tickets.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM ticket_history")

rows = cursor.fetchall()

wb = Workbook()

ws = wb.active

ws.append(["ID", "Ticket", "Category", "Priority"])

for row in rows:
    ws.append(row)

wb.save("TicketHistory.xlsx")

conn.close()

print("Excel File Created Successfully!")