import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")

df["overview"] = df["overview"].fillna("")

vectorizer = TfidfVectorizer(
    stop_words="english"
)

tfidf_matrix = vectorizer.fit_transform(
    df["overview"]
)

similarity_matrix = cosine_similarity(
    tfidf_matrix
)

print(
    "Similarity Matrix Shape:"
)

print(
    similarity_matrix.shape
)