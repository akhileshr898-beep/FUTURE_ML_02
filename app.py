import tkinter as tk
import joblib
import sqlite3

from preprocess import clean_text

# Load trained models
category_model = joblib.load("model/category_model.pkl")
priority_model = joblib.load("model/priority_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


def classify():

    # Get ticket from input box
    ticket = entry.get()

    # Clean the text
    cleaned_ticket = clean_text(ticket)

    # Convert to TF-IDF
    X = vectorizer.transform([cleaned_ticket])

    # Predict Category
    category = category_model.predict(X)[0]

    # Predict Priority
    priority = priority_model.predict(X)[0]

    # Connect to SQLite Database
    conn = sqlite3.connect("tickets.db")

    cursor = conn.cursor()

    # Insert prediction into database
    cursor.execute(
        """
        INSERT INTO ticket_history(ticket, category, priority)
        VALUES (?, ?, ?)
        """,
        (ticket, category, priority)
    )

    conn.commit()
    conn.close()

    # Show Result
    result.config(
        text=f"Category: {category}\nPriority: {priority}"
    )


# Create Main Window
root = tk.Tk()

root.title("Support Ticket Classification System")

root.geometry("500x350")

# Heading
heading = tk.Label(
    root,
    text="Support Ticket Classification System",
    font=("Arial", 16, "bold")
)
heading.pack(pady=10)

# Label
label = tk.Label(
    root,
    text="Enter Support Ticket:"
)
label.pack()

# Input Box
entry = tk.Entry(
    root,
    width=50
)
entry.pack(pady=10)

# Predict Button
button = tk.Button(
    root,
    text="Predict",
    command=classify
)
button.pack(pady=10)

# Result Label
result = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)
result.pack(pady=20)

# Run Application
root.mainloop()