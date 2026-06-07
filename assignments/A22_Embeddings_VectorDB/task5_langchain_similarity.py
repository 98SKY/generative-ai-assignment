from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

docs = [
    "Python is a programming language",
    "Machine learning uses data",
    "LangChain helps build AI applications",
    "Deep learning is a subset of ML"
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_texts(
    texts=docs,
    embedding=embedding_model
)

results = vectorstore.similarity_search(
    "Artificial Intelligence",
    k=3
)

for doc in results:
    print(doc.page_content)