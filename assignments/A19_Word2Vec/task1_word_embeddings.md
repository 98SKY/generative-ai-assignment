# Task 1: Understanding Word Embeddings

## 1. What are Word Embeddings?

Word embeddings are dense vector representations of words where similar words have similar vector values.

Example:

king → [0.12, -0.45, 0.88, ...]

queen → [0.10, -0.42, 0.90, ...]

---

## 2. Why One-Hot Encoding and BoW Fail?

- High dimensional vectors
- Sparse representation
- No semantic meaning
- Cannot understand relationships between words

Example:

King and Queen are completely different vectors.

---

## 3. How Word Embeddings Solve This?

- Dense numerical vectors
- Capture semantic relationships
- Similar words are located close together in vector space
- Better NLP performance