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
    min_count=1
)

print(
    "\nWords Similar To Product:\n"
)

print(
    model.wv.most_similar(
        "product",
        topn=5
    )
)

print(
    "\nSimilarity Score:\n"
)

print(
    model.wv.similarity(
        "product",
        "service"
    )
)

# Optional analogy
try:

    print(
        model.wv.most_similar(
            positive=["good"],
            negative=["bad"],
            topn=3
        )
    )

except:
    print(
        "Analogy not possible on small dataset."
    )