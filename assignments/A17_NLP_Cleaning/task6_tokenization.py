import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

df = pd.read_csv("reviews.csv")

for text in df["text"].head(3):

    print("\nOriginal Text:")
    print(text)

    print("\nWord Tokens:")
    print(word_tokenize(text))

    print("\nSentence Tokens:")
    print(sent_tokenize(text))