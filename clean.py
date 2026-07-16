import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def clean_text(text):
    """Cleans raw text for Naive Bayes preprocessing by removing punctuation,

    special characters, numbers, and excess whitespaces.
    """
    # 1. Convert the text to lowercase so 'Apple' and 'apple' are treated the same
    text = text.lower()

    # 2. Use regex to replace everything that is NOT a letter or a space with nothing
    # [^a-zA-Z\s] means: "Match anything that is NOT a lowercase letter, uppercase letter, or whitespace"
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # 3. Remove extra whitespaces/tabs/newlines and trim the edges
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ==========================================
# Example Usage in a Naive Bayes Pipeline
# ==========================================

# 1. Raw Data
raw_data = {
    "text": [
        "Wow!!! I absolutely loved this movie, it was fantastic!",
        "Don't waste your money... worst experience ever.",
        "It was okay, nothing special, just an average film.",
        "Brilliant acting and a great plot! Highly recommended.",
    ],
    "sentiment": [
        1,
        0,
        0,
        1,
    ],  # 1 = Positive, 0 = Negative
}

df = pd.DataFrame(raw_data)

# 2. Apply the cleaning function to the DataFrame
df["cleaned_text"] = df["text"].apply(clean_text)

print("--- Cleaned Data ---")
print(df[["text", "cleaned_text"]])

# 3. Vectorize the cleaned text (Convert text to numbers)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["cleaned_text"])
y = df["sentiment"]

# 4. Train the Naive Bayes Classifier
model = MultinomialNB()
model.fit(X, y)

# 5. Test it on a new raw string
test_phrase = "Seriously, this was spectacular!!"
cleaned_test = clean_text(test_phrase)
vectorized_test = vectorizer.transform([cleaned_test])

prediction = model.predict(vectorized_test)
print(f"\nPrediction for '{test_phrase}': {prediction[0]}")