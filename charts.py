import sqlite3
import matplotlib.pyplot as plt

# Connect database
conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

cursor.execute("""
SELECT category, COUNT(*)
FROM ticket_history
GROUP BY category
""")

data = cursor.fetchall()
print(data)
conn.close()

if len(data) == 0:
    print("No ticket data found.")
    exit()

categories = []
counts = []

for category, count in data:
    categories.append(category)
    counts.append(count)

# Pie Chart
plt.figure(figsize=(6,6))
plt.pie(
    counts,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Ticket Distribution by Category")
plt.axis("equal")
plt.show()

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(categories, counts)
plt.title("Ticket Count by Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()