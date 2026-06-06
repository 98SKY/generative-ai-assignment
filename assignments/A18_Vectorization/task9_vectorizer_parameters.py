import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("reviews.csv")

configs = [

    {"max_features":10},

    {"max_features":20},

    {"min_df":2},

    {"max_df":0.8}

]

for config in configs:

    vectorizer = CountVectorizer(
        **config
    )

    X = vectorizer.fit_transform(
        df["text"]
    )

    print("\nConfig:", config)

    print(
        "Vocabulary Size:",
        len(vectorizer.vocabulary_)
    )