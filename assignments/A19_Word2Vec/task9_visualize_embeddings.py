import pandas as pd

from nltk.tokenize import word_tokenize

from gensim.models import Word2Vec

from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

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
    min_count=1
)

words = list(model.wv.index_to_key)[:20]

vectors = [
    model.wv[word]
    for word in words
]

pca = PCA(n_components=2)

result = pca.fit_transform(vectors)

plt.figure(figsize=(10,6))

for i, word in enumerate(words):

    plt.scatter(
        result[i,0],
        result[i,1]
    )

    plt.annotate(
        word,
        (
            result[i,0],
            result[i,1]
        )
    )

plt.title(
    "Word2Vec Embeddings"
)

plt.show()