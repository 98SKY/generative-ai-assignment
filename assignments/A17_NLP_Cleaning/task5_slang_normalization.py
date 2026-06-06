import re

slang_dict = {
    "gr8": "great",
    "u": "you",
    "omg": "oh my god"
}

text = "OMG this phone is gr8 and soooo good"

# slang replacement
for slang, actual in slang_dict.items():
    text = text.lower().replace(
        slang,
        actual
    )

# repeated characters
text = re.sub(
    r"(.)\1{2,}",
    r"\1",
    text
)

print(text)