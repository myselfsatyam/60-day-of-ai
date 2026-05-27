# Document Retrieval System using TF-IDF

## Day 11 — Information Retrieval

This project focuses on building a simple document retrieval system using TF-IDF vectorization and cosine similarity. The goal is to understand how AI systems retrieve relevant information before generating responses.

The system takes a user query, compares it with a collection of documents, and returns the most relevant matches based on similarity scores.

---

# Project Overview

In this project, I created a small knowledge base containing documents related to Artificial Intelligence and Machine Learning.

The workflow includes:

* Preprocessing text data
* Converting documents into TF-IDF vectors
* Comparing queries using cosine similarity
* Retrieving top matching documents
* Handling irrelevant queries with a relevance threshold
* Analysing retrieval failures

---

# Step-by-Step Workflow

## 1. Creating the Knowledge Base

I first created a list of documents that act as the system’s knowledge source.

Example:

```python
documents = [
    "Machine learning allows computers to learn patterns from data.",
    "Deep learning uses neural networks with multiple hidden layers.",
    "Natural language processing helps machines understand language."
]
```

---

## 2. Text Preprocessing

Before vectorization, the text is cleaned by:

* converting to lowercase
* removing punctuation
* removing unnecessary symbols

This helps make the text more consistent.

---

## 3. TF-IDF Vectorization

Since machines cannot directly understand text, the documents are converted into numerical vectors using TF-IDF.

TF-IDF gives importance to words that are useful in a document while reducing the weight of very common words.

```python
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)
```

---

## 4. Query Vectorization

When a user enters a query, the query is transformed into a vector using the same TF-IDF vocabulary.

Example:

```python
query_vector = vectorizer.transform([query])
```

---

## 5. Calculating Similarity

Cosine similarity is used to compare the query vector with all document vectors.

```python
similarities = cosine_similarity(query_vector, tfidf_matrix)
```

Higher similarity scores indicate more relevant documents.

---

## 6. Retrieving Top Results

The documents are ranked based on similarity scores, and the top matches are returned.


# Retrieval Failures

Some queries did not perform well because TF-IDF depends heavily on exact word matching.

Example:

Query:

```python
"word representations"
```

Relevant concept:

```python
"embeddings"
```

The system failed because the words were different even though the meanings were related.

---

# Limitation of TF-IDF

TF-IDF works well for keyword matching, but it does not understand semantic meaning.

Because of this, synonym-based queries often fail. This limitation explains why modern AI systems use embeddings instead of only keyword-based retrieval.

Embeddings help capture meaning and relationships between words, making retrieval systems much more effective.

---

# Technologies Used

* Python
* NumPy
* scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

---

# Key Learnings

Through this project, I learned:

* how retrieval systems work
* how TF-IDF represents text numerically
* how cosine similarity ranks documents
* why keyword-based retrieval has limitations
* why embeddings are important in modern AI systems

---

# Conclusion

This project provided a practical introduction to information retrieval systems. Although TF-IDF retrieval is simple, it forms the foundation for more advanced systems such as semantic search and Retrieval-Augmented Generation (RAG).
