import os

from groq import Groq

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

loader = TextLoader("data/sample.txt")

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

retriever = vectorstore.as_retriever()

question = "What is RAG?"

docs = retriever.invoke(question)

context = "\n".join(
    [doc.page_content for doc in docs]
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content":
            f"""
            Context:
            {context}

            Question:
            {question}
            """
        }
    ]
)

print(response.choices[0].message.content)