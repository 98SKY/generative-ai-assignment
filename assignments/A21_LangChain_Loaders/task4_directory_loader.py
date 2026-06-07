from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    CSVLoader,
    PyPDFLoader
)

documents = []

# Load TXT files
txt_loader = DirectoryLoader(
    "data",
    glob="*.txt",
    loader_cls=TextLoader
)

documents.extend(txt_loader.load())

# Load CSV files
csv_loader = DirectoryLoader(
    "data",
    glob="*.csv",
    loader_cls=CSVLoader
)

documents.extend(csv_loader.load())

# Load PDF files
pdf_loader = DirectoryLoader(
    "data",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

documents.extend(pdf_loader.load())

print("Total Documents:", len(documents))

for doc in documents:
    print("\nMetadata:")
    print(doc.metadata)