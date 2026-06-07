from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

documents = [
    "Python is used in Data Science",
    "Machine Learning requires data",
    "LangChain helps create RAG systems",
    "Generative AI uses embeddings"
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_texts(
    documents,
    embedding=embedding_model
)

query = "What is used in RAG?"

results = vectorstore.similarity_search(
    query,
    k=3
)

print("\nQuery:")
print(query)

print("\nResults:\n")

for doc in results:
    print(doc.page_content)