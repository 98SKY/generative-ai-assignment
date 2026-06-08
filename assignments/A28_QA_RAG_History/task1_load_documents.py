from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/sample.txt")

documents = loader.load()

print("Total Documents:", len(documents))

print("\nSample Content:\n")
print(documents[0].page_content[:500])