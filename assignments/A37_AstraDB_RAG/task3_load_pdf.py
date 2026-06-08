from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader(
    "data/sample.pdf"
)

documents = loader.load()

print("Pages:", len(documents))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(
    documents
)

print("Chunks:", len(chunks))