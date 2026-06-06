import pandas as pd
import re

df = pd.read_csv("movies.csv")

df["overview"] = df["overview"].fillna("")

def clean_text(text):

    text = text.lower()

    text = re.sub(r"[^a-zA-Z ]", "", text)

    text = " ".join(text.split())

    return text

df["clean_text"] = df["overview"].apply(clean_text)

print(
    df[["title", "clean_text"]].head()
)