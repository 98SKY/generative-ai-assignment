from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

docs = [
    "AI is transforming business",
    "Machine learning uses data",
    "Deep learning is part of machine learning",
    "Generative AI creates content",
    "LangChain helps build AI applications"
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_texts(
    docs,
    embedding_model
)

print("\nSimilarity Search")

similarity_retriever = vectorstore.as_retriever(
    search_type="similarity"
)

results = similarity_retriever.invoke(
    "AI"
)

for doc in results:
    print(doc.page_content)

print("\nMMR Search")

mmr_retriever = vectorstore.as_retriever(
    search_type="mmr"
)

results = mmr_retriever.invoke(
    "AI"
)

for doc in results:
    print(doc.page_content)