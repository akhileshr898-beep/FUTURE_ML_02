import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from preprocess import clean_text

# Load dataset
data = pd.read_csv("dataset/tickets.csv")

# Clean text
data["CleanTicket"] = data["Ticket"].apply(clean_text)

# Convert to TF-IDF
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data["CleanTicket"])

# Category model
category_model = MultinomialNB()
category_model.fit(X, data["Category"])

# Priority model
priority_model = MultinomialNB()
priority_model.fit(X, data["Priority"])

# Save models
joblib.dump(category_model, "model/category_model.pkl")
joblib.dump(priority_model, "model/priority_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Training Completed Successfully!")