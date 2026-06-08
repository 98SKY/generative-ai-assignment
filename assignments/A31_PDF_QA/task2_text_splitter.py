from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

loader = PyPDFLoader(
    "data/sample.pdf"
)

pages = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(
    pages
)

print(
    "Total Chunks:",
    len(chunks)
)

print(
    chunks[0].page_content[:300]
)