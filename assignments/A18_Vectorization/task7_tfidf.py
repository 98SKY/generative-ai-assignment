import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("reviews.csv")

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(
    df["text"]
)

print("Vocabulary Size:")
print(len(vectorizer.vocabulary_))

print("\nTF-IDF Shape:")
print(X.shape)

print("\nSample Vocabulary:")

print(
    list(
        vectorizer.vocabulary_.keys()
    )[:20]
)