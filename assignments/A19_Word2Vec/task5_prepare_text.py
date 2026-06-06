import pandas as pd
from nltk.tokenize import word_tokenize

df = pd.read_csv("reviews.csv")

sentences = []

for text in df["text"]:

    tokens = word_tokenize(
        str(text).lower()
    )

    sentences.append(tokens)

print("First 5 Tokenized Sentences:\n")

for s in sentences[:5]:
    print(s)