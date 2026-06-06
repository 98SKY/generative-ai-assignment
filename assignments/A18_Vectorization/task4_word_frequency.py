import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("reviews.csv")

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(df["text"])

word_counts = X.sum(axis=0).A1

words = vectorizer.get_feature_names_out()

freq_df = pd.DataFrame({
    "word": words,
    "count": word_counts
})

freq_df = freq_df.sort_values(
    by="count",
    ascending=False
)

print("Top 10 Frequent Words:\n")
print(freq_df.head(10))

print("\nLeast Frequent Words:\n")
print(freq_df.tail(10))