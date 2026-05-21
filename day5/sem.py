# ================================
# MINI SEMANTIC SEARCH ENGINE
# ================================

# Install required libraries:
# pip install sentence-transformers scikit-learn


# ================================
# IMPORTS
# ================================

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re


# ================================
# DATASET
# ================================

sentences = [
    "Artificial intelligence is transforming healthcare.",
    "Machine learning models learn from data.",
    "Neural networks are inspired by the human brain.",
    "Deep learning is a subset of machine learning.",
    "Python is popular for AI development.",
    "Transformers are used in large language models.",
    "Semantic search understands meaning instead of keywords.",
    "Vector databases store embeddings efficiently.",
    "RAG combines retrieval with text generation.",
    "Embeddings convert text into numerical vectors.",
    "Computer vision enables machines to interpret images.",
    "Natural language processing helps computers understand text.",
    "Recommendation systems personalize user experiences.",
    "Chatbots use NLP to answer user queries.",
    "Open-source models are becoming more powerful.",
    "Fine-tuning improves model performance on specific tasks.",
    "GPU acceleration speeds up deep learning training.",
    "Search engines index and retrieve information.",
    "Cosine similarity measures vector closeness.",
    "AI agents can automate repetitive workflows."
]


# ================================
# LOAD EMBEDDING MODEL
# ================================

print("Loading embedding model...")

model = SentenceTransformer('all-MiniLM-L6-v2')

print("Model loaded successfully!\n")


# ================================
# CREATE EMBEDDINGS
# ================================

print("Generating embeddings for dataset...\n")

embeddings = model.encode(sentences)

print("Embeddings generated successfully!\n")


# ================================
# SEMANTIC SEARCH FUNCTION
# ================================

def semantic_search(query, top_k=3):

    # Convert query into embedding
    query_embedding = model.encode([query])

    # Compute cosine similarity
    similarities = cosine_similarity(query_embedding, embeddings)[0]

    # Get top matching indices
    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []

    for idx in top_indices:
        results.append({
            "sentence": sentences[idx],
            "score": round(float(similarities[idx]), 4)
        })

    return results


# ================================
# KEYWORD SEARCH FUNCTION
# ================================

def keyword_search(query, top_k=3):

    # Remove punctuation + lowercase
    query_words = set(re.findall(r'\w+', query.lower()))

    scores = []

    for sentence in sentences:

        sentence_words = set(re.findall(r'\w+', sentence.lower()))

        # Count overlapping words
        overlap = len(query_words.intersection(sentence_words))

        scores.append(overlap)

    # Sort by overlap score
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for idx in top_indices:
        results.append({
            "sentence": sentences[idx],
            "score": scores[idx]
        })

    return results


# ================================
# TEST QUERIES
# ================================

queries = [
    "How do AI systems understand meaning?",
    "systems that recommend movies",
    "AI for understanding language",
    "models that generate text",
    "speeding up neural network training"
]


# ================================
# RUN SEARCHES
# ================================

for query in queries:

    print("=" * 60)
    print(f"QUERY: {query}")
    print("=" * 60)

    # Semantic Search
    print("\nSEMANTIC SEARCH RESULTS:\n")

    semantic_results = semantic_search(query)

    for i, result in enumerate(semantic_results, start=1):
        print(f"{i}. {result['sentence']}")
        print(f"   Similarity Score: {result['score']}\n")

    # Keyword Search
    print("KEYWORD SEARCH RESULTS:\n")

    keyword_results = keyword_search(query)

    for i, result in enumerate(keyword_results, start=1):
        print(f"{i}. {result['sentence']}")
        print(f"   Keyword Match Score: {result['score']}\n")

    print("\n\n")


# ================================
# OPTIONAL: INTERACTIVE SEARCH
# ================================

while True:

    user_query = input("Enter your search query (or type 'exit'): ")

    if user_query.lower() == "exit":
        print("Exiting search engine...")
        break

    print("\nTop Semantic Search Results:\n")

    results = semantic_search(user_query)

    for i, result in enumerate(results, start=1):
        print(f"{i}. {result['sentence']}")
        print(f"   Similarity Score: {result['score']}\n")