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

indices = pd.Series(
    df.index,
    index=df["title"]
).drop_duplicates()


def recommend(movie_name, top_n=5):

    idx = indices[movie_name]

    scores = list(
        enumerate(
            similarity_matrix[idx]
        )
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    scores = scores[1:top_n+1]

    movie_indices = [
        i[0]
        for i in scores
    ]

    return df["title"].iloc[
        movie_indices
    ]


print(
    recommend("Avatar")
)

print(
    recommend("Batman Begins")
)

print(
    recommend("Titanic")
)