import pandas as pd

df = pd.read_csv("reviews.csv")

sentences = df["text"].head(5).tolist()

# Build vocabulary
vocabulary = sorted(
    set(
        word.lower()
        for sentence in sentences
        for word in sentence.split()
    )
)

print("Vocabulary:\n")
print(vocabulary)

print("\nOne-Hot Encoded Vectors:\n")

for sentence in sentences:

    vector = []

    words = sentence.lower().split()

    for vocab_word in vocabulary:

        if vocab_word in words:
            vector.append(1)
        else:
            vector.append(0)

    print(vector)