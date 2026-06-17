import sqlite3

# Connect to database
conn = sqlite3.connect("tickets.db")

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS ticket_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket TEXT,
    category TEXT,
    priority TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")