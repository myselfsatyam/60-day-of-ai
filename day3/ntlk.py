# ============================================
# DAY 3 — TEXT IS DATA
# Turning Words into Numbers using NLP
# ============================================

# -----------------------------
# 1. Install Required Libraries
# -----------------------------
# Run this only once in Jupyter/Colab

##!pip install nltk scikit-learn pandas

# -----------------------------
# 2. Import Libraries
# -----------------------------

import nltk
import string
import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# -----------------------------
# 3. Create Sample Dataset
# -----------------------------

texts = [
    "Artificial Intelligence is transforming the world.",
    "Natural Language Processing helps machines understand text.",
    "Machine learning models require clean and structured data.",
    "Chatbots use NLP techniques to communicate with users.",
    "Preprocessing text improves machine learning accuracy."
]

# Convert into DataFrame
df = pd.DataFrame({
    "Original_Text": texts
})

print("========== ORIGINAL DATASET ==========\n")
print(df)

# -----------------------------
# 4. Tokenization Example
# -----------------------------

sample_text = texts[0]

tokens = word_tokenize(sample_text)

print("\n========== TOKENIZATION ==========\n")

print("Original Text:\n")
print(sample_text)

print("\nTokens:\n")
print(tokens)

# -----------------------------
s
# -----------------------------

stop_words = set(stopwords.words('english'))

clean_tokens = [
    word.lower()
    for word in tokens
    if word.lower() not in stop_words
    and word not in string.punctuation
]

print("\n========== AFTER CLEANING ==========\n")

print("Clean Tokens:\n")
print(clean_tokens)

# -----------------------------
# 6. Create Preprocessing Function
# -----------------------------

def preprocess_text(text):

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords & punctuation
    clean_tokens = [
        word.lower()
        for word in tokens
        if word.lower() not in stop_words
        and word not in string.punctuation
    ]

    # Join tokens back into sentence
    processed_text = " ".join(clean_tokens)

    return processed_text

# -----------------------------
# 7. Apply Preprocessing
# -----------------------------

df["Processed_Text"] = df["Original_Text"].apply(preprocess_text)

print("\n========== PREPROCESSED DATASET ==========\n")
print(df)

# -----------------------------
# 8. Convert Text into Bag-of-Words
# -----------------------------

vectorizer = CountVectorizer()

bow_matrix = vectorizer.fit_transform(df["Processed_Text"])

# Convert matrix into DataFrame
bow_df = pd.DataFrame(
    bow_matrix.toarray(),
    columns=vectorizer.get_feature_names_out()
)

print("\n========== BAG OF WORDS REPRESENTATION ==========\n")
print(bow_df)

# -----------------------------
# 9. Vocabulary
# -----------------------------

print("\n========== VOCABULARY ==========\n")
print(vectorizer.get_feature_names_out())

# -----------------------------
# 10. Save Preprocessed Dataset
# -----------------------------

df.to_csv("preprocessed_text_dataset.csv", index=False)

print("\n========== FILE SAVED ==========")
print("Preprocessed dataset saved as 'preprocessed_text_dataset.csv'")

# -----------------------------
# 11. Final Summary
# -----------------------------

print("\n========== SUMMARY ==========\n")

print("1. Original text loaded")
print("2. Text tokenized")
print("3. Stop words removed")
print("4. Punctuation removed")
print("5. Text converted to lowercase")
print("6. Bag-of-Words representation created")
print("7. Dataset saved for ML input")