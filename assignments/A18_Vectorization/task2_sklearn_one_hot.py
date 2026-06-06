import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("reviews.csv")

sentences = df["text"].head(5)

vectorizer = CountVectorizer(binary=True)

X = vectorizer.fit_transform(sentences)

print("Vocabulary:\n")
print(vectorizer.vocabulary_)

print("\nEncoded Matrix:\n")
print(X.toarray())