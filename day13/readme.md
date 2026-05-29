# Understanding Embeddings as Semantic Coordinates

## Introduction

In previous projects, I used TF-IDF to compare the similarity between pieces of text. While TF-IDF works well when documents share common words, it often fails when two sentences have similar meanings but use different vocabulary.

In this project, I explored text embeddings using Google's Gemini Embedding model and compared them with TF-IDF vectors. The goal was to understand how modern AI systems represent meaning and why embeddings are so important for applications like semantic search, recommendation systems, and Retrieval-Augmented Generation (RAG).

## What I Built

For this project, I created a dataset of 20 sentences covering four different topics:

* Sports
* Technology
* Cooking
* Travel

Using these sentences, I:

* Generated embeddings with Gemini Embeddings API
* Calculated cosine similarity scores
* Compared embedding similarities with TF-IDF similarities
* Built a semantic recommendation function
* Clustered sentences using K-Means
* Visualized the clusters using PCA
* Measured embedding generation time

## Why Compare TF-IDF and Embeddings?

TF-IDF represents text based on word frequency. It works by checking how important words are within a document collection.

The problem is that TF-IDF only understands words, not meaning.

For example:

* "Artificial intelligence is transforming industries"
* "Machine learning models learn patterns from data"

These sentences talk about related concepts, but they share very few words. As a result, TF-IDF may consider them only weakly related.

Embeddings approach the problem differently. Instead of focusing on exact words, they convert text into dense numerical vectors that capture semantic meaning. Sentences with similar meanings tend to appear closer together in vector space, even when they use different vocabulary.

## Semantic Recommendation System

One of the most interesting parts of this project was building a simple recommendation system.

Given a query sentence, the system:

1. Generates an embedding for the query.
2. Compares it with embeddings of all sentences in the dataset.
3. Returns the most semantically similar results.

Unlike keyword matching, this approach can retrieve relevant sentences even when there is little or no word overlap.

## Clustering Results

After generating embeddings, I applied K-Means clustering to group similar sentences together.

The resulting clusters mostly aligned with the original topics, which showed that embeddings successfully captured the semantic relationships between sentences.

To better understand the clustering behavior, I reduced the embedding dimensions using PCA and visualized the clusters on a 2D plot.

## Key Takeaways

A few things stood out during this experiment:

* TF-IDF is useful for keyword-based similarity but struggles with paraphrased text.
* Embeddings capture meaning rather than exact wording.
* Cosine similarity becomes much more powerful when applied to embeddings.
* Semantic search is significantly more flexible than traditional keyword search.
* Embeddings naturally group related information together, making them useful for clustering and recommendation tasks.

## Conclusion

This project helped me understand the practical difference between traditional text representations and modern embedding-based approaches.

TF-IDF answers the question:

> "Do these texts use similar words?"

Embeddings answer the question:

> "Do these texts mean similar things?"

That difference is what makes embeddings a core building block of modern AI systems. Whether it's semantic search, document retrieval, recommendation engines, or RAG applications, embeddings provide a much richer representation of language than traditional keyword-based methods.
