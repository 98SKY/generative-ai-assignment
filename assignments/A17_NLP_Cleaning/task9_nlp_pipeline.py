import pandas as pd
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

df = pd.read_csv("reviews.csv")

stop_words = set(
    stopwords.words("english")
)

lemmatizer = WordNetLemmatizer()

def nlp_preprocess(text):

    text = str(text).lower()

    text = re.sub(
        r"http\S+",
        "",
        text
    )

    text = re.sub(
        r"\S+@\S+",
        "",
        text
    )

    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    tokens = word_tokenize(text)

    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(tokens)

df["final_clean_text"] = (
    df["text"]
    .apply(nlp_preprocess)
)

print(
    df[
        ["text", "final_clean_text"]
    ].head()
)