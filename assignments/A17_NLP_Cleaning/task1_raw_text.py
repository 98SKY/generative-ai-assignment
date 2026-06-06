import pandas as pd

df = pd.read_csv("reviews.csv")

print("First 5 Samples\n")

print(df["text"].head())

print("\nText Lengths\n")

for text in df["text"].head():
    print(len(str(text)))

print("\nCommon Issues:")
print("- Uppercase letters")
print("- Punctuation")
print("- Numbers")
print("- URLs")
print("- Emails")
print("- Emojis")
print("- Extra spaces")