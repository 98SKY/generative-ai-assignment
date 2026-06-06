import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("reviews.csv")

vectorizer = CountVectorizer(
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(
    df["text"]
)

print("Vocabulary Size:")
print(len(vectorizer.vocabulary_))

print("\nSample Features:")

features = vectorizer.get_feature_names_out()

print(features[:50])