from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

words = [
    "running",
    "playing",
    "studies",
    "better"
]

for word in words:

    print("\nWord:", word)

    print(
        "Stem:",
        stemmer.stem(word)
    )

    print(
        "Lemma:",
        lemmatizer.lemmatize(word)
    )