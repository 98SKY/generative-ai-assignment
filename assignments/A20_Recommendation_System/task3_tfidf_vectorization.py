import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("movies.csv")

df["overview"] = df["overview"].fillna("")

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000,
    ngram_range=(1,2)
)

tfidf_matrix = vectorizer.fit_transform(
    df["overview"]
)

print(
    "TF-IDF Matrix Shape:"
)

print(
    tfidf_matrix.shape
)