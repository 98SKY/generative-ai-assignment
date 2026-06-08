import os

from dotenv import load_dotenv

from langchain_astradb import AstraDBVectorStore

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

loader = PyPDFLoader(
    "data/sample.pdf"
)

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(
    documents
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = AstraDBVectorStore(
    collection_name="assignment37",
    embedding=embeddings,
    api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
)

vectorstore.add_documents(
    chunks
)

print("Embeddings Stored Successfully")