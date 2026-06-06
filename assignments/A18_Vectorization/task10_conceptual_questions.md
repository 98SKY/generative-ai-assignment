# Task 10: Conceptual Questions

## 1. Difference between One-Hot Encoding and BoW

One-Hot:
- Indicates only presence/absence
- Ignores frequency

BoW:
- Stores actual word counts
- Captures frequency information

---

## 2. Why N-Grams Increase Dimensionality

Each additional word combination becomes a new feature.

Example:

good
product

becomes

good product

which increases vocabulary size.

---

## 3. When to Prefer TF-IDF Over BoW

TF-IDF is preferred when:

- Common words dominate the dataset
- Important keywords need higher weight
- Text classification tasks

---

## 4. Limitations of Count-Based Vectorization

- Produces sparse matrices
- Ignores semantic meaning
- Ignores word order (except N-Grams)
- High dimensionality