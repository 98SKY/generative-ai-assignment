import pandas as pd
import re

df = pd.read_csv("reviews.csv")

def advanced_clean(text):

    text = str(text)

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"www\S+", "", text)

    text = re.sub(
        r"\S+@\S+",
        "",
        text
    )

    text = re.sub(
        r"<.*?>",
        "",
        text
    )

    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    return text.lower().strip()

df["clean_text_advanced"] = (
    df["text"]
    .apply(advanced_clean)
)

print(
    df[
        ["text", "clean_text_advanced"]
    ].head()
)