import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("reviews.csv")

for name, ngram in {

    "Unigram": (1,1),
    "Bigram": (2,2),
    "Trigram": (3,3)

}.items():

    vectorizer = CountVectorizer(
        ngram_range=ngram
    )

    X = vectorizer.fit_transform(
        df["text"]
    )

    print(f"\n{name}")
    print("Vocabulary Size:",
          len(vectorizer.vocabulary_))

    print("Shape:",
          X.shape)