from transformers import pipeline

print("Loading Model...")

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

response = generator(
    "Explain Retrieval Augmented Generation in simple terms.",
    max_length=100
)

print("\nResponse:")
print(response[0]["generated_text"])