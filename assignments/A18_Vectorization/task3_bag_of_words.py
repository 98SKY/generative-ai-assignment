import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("reviews.csv")

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(df["text"])

print("Vocabulary Size:")
print(len(vectorizer.vocabulary_))

print("\nBoW Matrix Shape:")
print(X.shape)

print("\nSample Feature Vector:")
print(X.toarray()[0])