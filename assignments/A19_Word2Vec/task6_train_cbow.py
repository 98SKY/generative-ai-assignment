import pandas as pd
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec

df = pd.read_csv("reviews.csv")

sentences = []

for text in df["text"]:
    sentences.append(
        word_tokenize(
            str(text).lower()
        )
    )

model = Word2Vec(
    sentences,
    vector_size=100,
    window=5,
    min_count=1,
    sg=0
)

print(
    "Vocabulary Size:",
    len(model.wv)
)

print("\nVector for word 'product':\n")

print(
    model.wv["product"]
)