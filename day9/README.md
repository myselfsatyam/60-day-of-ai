# Teaching AI Semantic Meaning Through Vectors

## Day 9 — AI Foundations

### Focus Area
Vector Representation and Cosine Similarity

---

## Overview

Humans naturally understand that words like **"dog"** and **"puppy"** are related, but computers only understand numbers.  
To enable machines to process language, text must first be converted into numerical vector representations.

This project demonstrates how AI systems measure semantic similarity using:

- TF-IDF Vectorisation
- Cosine Similarity
- NumPy Matrix Operations
- Heatmap Visualisation

The project builds a simple semantic search workflow capable of comparing sentence meanings mathematically.

---

## Objectives

- Understand why plain text cannot be directly compared by machines
- Convert sentences into TF-IDF vectors
- Compute cosine similarity between text vectors
- Build a semantic similarity search function
- Visualise sentence relationships using a heatmap
- Learn why cosine similarity uses vector angles instead of distance

---

## Technologies Used

- Python
- scikit-learn
- NumPy
- matplotlib

---

## Project Structure

```bash
semantic-similarity-demo/
│
├── semantic_similarity.ipynb
├── README.md
└── requirements.txt
```

---

## Dataset

The project uses 10 sentences across 3 different domains:

- Animals
- Technology
- Travel

This helps demonstrate semantic clustering using vector similarity.

---

## Key Concepts

### TF-IDF Vectorisation

TF-IDF converts text into numerical vectors by assigning importance scores to words.

- **TF (Term Frequency)** → How often a word appears
- **IDF (Inverse Document Frequency)** → How unique the word is across documents

This helps reduce the impact of common words while emphasizing meaningful terms.

---

### Cosine Similarity

Cosine similarity measures the angle between two vectors rather than their distance.

The formula:

\[
\cos(\theta)=\frac{A \cdot B}{||A|| \ ||B||}
\]

Where:

- \(A \cdot B\) = Dot product
- \(||A||\) and \(||B||\) = Vector magnitudes
- \(\theta\) = Angle between vectors

### Why Angle Instead of Distance?

Text length can vary significantly.

Example:

- `"dog"`
- `"dog dog dog dog"`

Even though the second sentence is longer, the meaning is nearly identical.

Cosine similarity focuses on direction rather than magnitude, making it ideal for text comparison.

---

## Features

### Sentence Vectorisation
Converts text into TF-IDF vectors using `TfidfVectorizer`.

### Similarity Matrix
Computes pairwise cosine similarity between all sentences.

### Semantic Search Function
Implements:

```python
find_similar(query, corpus, top_k)
```

Returns the most semantically related sentences with similarity scores.

### Heatmap Visualisation
Displays the 10×10 similarity matrix using matplotlib.

---

## Example Queries

### Similar Query

```python
find_similar("A puppy likes playing", sentences)
```

Expected:
- Higher similarity with dog/puppy-related sentences

---

### Dissimilar Query

```python
find_similar("An airplane is flying in the sky", sentences)
```

Expected:
- Higher similarity with travel-related sentences
- Lower similarity with animal-related sentences

---

## Heatmap Output

The heatmap visualises semantic clustering between sentences.

Expected observations:

- Animal sentences cluster together
- Technology sentences show strong similarity
- Travel sentences form a separate cluster
- Unrelated topics have lower similarity scores

---

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Open the notebook:

```bash
jupyter notebook semantic_similarity.ipynb
```

---

## Learning Outcomes

By completing this project, you will understand:

- How AI converts language into vectors
- Why numerical representation is necessary
- How semantic similarity works mathematically
- The importance of cosine similarity in NLP systems
- The foundation behind semantic search and embeddings

---

## Future Improvements

- Use Word2Vec or GloVe embeddings
- Add Sentence Transformers
- Build a mini semantic search engine
- Compare TF-IDF with modern embeddings
- Create an interactive web interface

---

## Author

Satyam Sharma

---

