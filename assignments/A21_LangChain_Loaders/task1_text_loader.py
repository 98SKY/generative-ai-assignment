from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/sample.txt")

documents = loader.load()

print("Documents Loaded:", len(documents))
print("\nContent Preview:")
print(documents[0].page_content[:200])

print("\nMetadata:")
print(documents[0].metadata)