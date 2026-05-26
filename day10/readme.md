                RAW INPUT QUERY
                        │
                        ▼
          ┌────────────────────────┐
          │ Preprocessing Module   │
          │ - Lowercasing          │
          │ - Cleaning             │
          │ - Tokenization         │
          │ - Stopword Removal     │
          └────────────────────────┘
                        │
                        ▼
          ┌────────────────────────┐
          │ Vectorizer Module      │
          │ - TF-IDF Vectorization │
          │ - Query Transformation │
          └────────────────────────┘
                        │
                        ▼
          ┌────────────────────────┐
          │ Similarity Engine      │
          │ - Cosine Similarity    │
          └────────────────────────┘
                        │
                        ▼
          ┌────────────────────────┐
          │ Ranked Output Results  │
          │ - Similarity Scores    │
          │ - Sorted Documents     │
          └────────────────────────┘