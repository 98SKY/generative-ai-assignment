from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "What is Retrieval Augmented Generation?"

vector = embeddings.embed_query(text)

print("Embedding Length:", len(vector))

print("\nFirst 10 Values:")
print(vector[:10])