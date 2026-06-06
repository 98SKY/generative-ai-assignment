from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "running",
    "playing",
    "studies",
    "better"
]

print("Original Words")

print(words)

print("\nStemmed Words")

print(
    [
        stemmer.stem(word)
        for word in words
    ]
)