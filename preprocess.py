import nltk
import string

from nltk.corpus import stopwords

# Download stopwords (only the first time)
nltk.download("stopwords")

# Load English stop words
stop_words = set(stopwords.words("english"))

# Function to clean text
def clean_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = "".join(
        ch for ch in text
        if ch not in string.punctuation
    )

    # Split into words
    words = text.split()

    # Remove stop words
    words = [
        word for word in words
        if word not in stop_words
    ]

    # Join back into a sentence
    return " ".join(words)


# Test the function
sample = "Internet is not working properly!!"

print(clean_text(sample))