import time

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

start = time.time()

skipgram_model = Word2Vec(
    sentences,
    vector_size=100,
    window=5,
    min_count=1,
    sg=1
)

end = time.time()

print(
    "Training Time:",
    end - start
)

print(
    "\nMost Similar Words To 'product':\n"
)

print(
    skipgram_model.wv.most_similar(
        "product"
    )
)