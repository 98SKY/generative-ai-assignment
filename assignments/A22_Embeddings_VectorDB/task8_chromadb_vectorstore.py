from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

docs = [
    "Python programming",
    "Machine Learning",
    "Generative AI",
    "LangChain Framework"
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_texts(
    texts=docs,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

results = vectorstore.similarity_search(
    "Artificial Intelligence",
    k=2
)

print("\nResults:\n")

for doc in results:
    print(doc.page_content)