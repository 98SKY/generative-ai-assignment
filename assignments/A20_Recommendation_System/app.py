import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)


@st.cache_data
def load_data():
    df = pd.read_csv("movies.csv")
    df["overview"] = df["overview"].fillna("")
    return df


@st.cache_resource
def build_model(df):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=2000
    )

    tfidf_matrix = vectorizer.fit_transform(
        df["overview"]
    )

    return tfidf_matrix


def recommend(movie_name, df, tfidf_matrix, indices):

    idx = indices[movie_name]

    movie_vector = tfidf_matrix[idx]

    similarity_scores = cosine_similarity(
        movie_vector,
        tfidf_matrix
    ).flatten()

    similar_movies = sorted(
        enumerate(similarity_scores),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    movie_indices = [
        movie[0]
        for movie in similar_movies
    ]

    return df["title"].iloc[movie_indices]


# Load Data
df = load_data()

# Build TF-IDF
tfidf_matrix = build_model(df)

# Create Index Mapping
indices = pd.Series(
    df.index,
    index=df["title"]
).drop_duplicates()

# UI
st.title("🎬 Movie Recommendation System")

st.write(
    "Select a movie and get similar recommendations."
)

movie = st.selectbox(
    "Select Movie",
    sorted(df["title"].unique())
)

if st.button("Recommend"):

    recommendations = recommend(
        movie,
        df,
        tfidf_matrix,
        indices
    )

    st.subheader("Recommended Movies")

    for i, rec in enumerate(recommendations, start=1):
        st.write(f"{i}. {rec}")