import pandas as pd
import re

df = pd.read_csv("reviews.csv")

def basic_clean(text):

    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    text = re.sub(r"\d+", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text

df["clean_text_basic"] = df["text"].apply(basic_clean)

print(
    df[
        ["text", "clean_text_basic"]
    ].head()
)