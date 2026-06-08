import os

from dotenv import load_dotenv

from langchain_astradb import AstraDBVectorStore

from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = AstraDBVectorStore(
    collection_name="assignment37",
    embedding=embeddings,
    api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
)

print("Connected Successfully")

print(vectorstore)