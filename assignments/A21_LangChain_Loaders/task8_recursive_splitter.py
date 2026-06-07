from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("data/sample.txt")

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)

print("Total Chunks:", len(chunks))

print("\nSample Chunk:")
print(chunks[0].page_content)