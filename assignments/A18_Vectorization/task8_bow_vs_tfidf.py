import pandas as pd

from sklearn.feature_extraction.text import (
    CountVectorizer,
    TfidfVectorizer
)

df = pd.read_csv("reviews.csv")

# BoW

bow = CountVectorizer()

bow_matrix = bow.fit_transform(
    df["text"]
)

# TF-IDF

tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(
    df["text"]
)

bow_words = bow.get_feature_names_out()

tfidf_scores = tfidf_matrix.sum(
    axis=0
).A1

tfidf_df = pd.DataFrame({

    "word": bow_words,
    "tfidf_score": tfidf_scores

})

tfidf_df = tfidf_df.sort_values(
    by="tfidf_score",
    ascending=False
)

print("Top TF-IDF Words:\n")

print(
    tfidf_df.head(10)
)

print("\nLowest TF-IDF Words:\n")

print(
    tfidf_df.tail(10)
)