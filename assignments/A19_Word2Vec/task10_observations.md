# Task 10: Observations & Limitations

## 1. Difference Between CBOW & Skip-Gram

CBOW:
- Faster
- Better on large datasets

Skip-Gram:
- Slower
- Better for rare words

---

## 2. Advantages Over TF-IDF

- Captures semantic meaning
- Dense vectors
- Similar words have similar representations

---

## 3. Limitations of Word2Vec

- Static embeddings
- Same meaning regardless of context
- Requires training data

---

## 4. Why Context Matters?

Word meaning changes depending on surrounding words.

Example:

bank = river bank

bank = financial institution

Word2Vec struggles with this.

Transformers solve this problem using contextual embeddings.