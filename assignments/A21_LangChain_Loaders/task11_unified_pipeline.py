from langchain_community.document_loaders import (
    TextLoader,
    CSVLoader,
    PyPDFLoader,
    WebBaseLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def load_and_split_documents(source, source_type):

    # Load Documents
    if source_type == "txt":
        loader = TextLoader(source)

    elif source_type == "csv":
        loader = CSVLoader(source)

    elif source_type == "pdf":
        loader = PyPDFLoader(source)

    elif source_type == "web":
        loader = WebBaseLoader(source)

    else:
        raise ValueError("Unsupported source type")

    documents = loader.load()

    # Split Documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    return chunks


# TXT
txt_chunks = load_and_split_documents(
    "data/sample.txt",
    "txt"
)

print("TXT Chunks:", len(txt_chunks))


# CSV
csv_chunks = load_and_split_documents(
    "data/sample.csv",
    "csv"
)

print("CSV Chunks:", len(csv_chunks))


# PDF
pdf_chunks = load_and_split_documents(
    "data/sample.pdf",
    "pdf"
)

print("PDF Chunks:", len(pdf_chunks))


# WEBSITE
web_chunks = load_and_split_documents(
    "https://python.langchain.com/docs/introduction/",
    "web"
)

print("WEB Chunks:", len(web_chunks))