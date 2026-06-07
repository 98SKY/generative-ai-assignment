from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

documents = [
    "Artificial Intelligence is transforming industries.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks.",
    "LangChain helps build RAG systems."
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_texts(
    texts=documents,
    embedding=embedding_model
)

retriever = vectorstore.as_retriever()

results = retriever.invoke(
    "What is AI?"
)

for doc in results:
    print(doc.page_content)