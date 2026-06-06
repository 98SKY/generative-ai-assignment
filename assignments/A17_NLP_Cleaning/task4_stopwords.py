import pandas as pd
from nltk.corpus import stopwords

df = pd.read_csv("reviews.csv")

stop_words = set(
    stopwords.words("english")
)

def remove_stopwords(text):

    words = text.split()

    words = [
        word
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

df["text_no_stopwords"] = (
    df["text"]
    .str.lower()
    .apply(remove_stopwords)
)

print(
    df[
        ["text", "text_no_stopwords"]
    ].head()
)