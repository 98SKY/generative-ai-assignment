from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader("data/sample.txt")

documents = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_documents(documents)

print("Total Chunks:", len(chunks))

print("\nSample Chunk:")
print(chunks[0].page_content)