from langchain_huggingface import HuggingFaceEmbeddings

print("Loading Model...")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "LangChain is used for Generative AI applications."

vector = embedding_model.embed_query(text)

print("\nEmbedding Length:")
print(len(vector))

print("\nFirst 10 Values:")
print(vector[:10])