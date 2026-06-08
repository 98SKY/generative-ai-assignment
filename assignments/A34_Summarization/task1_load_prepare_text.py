from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/sample_document.txt")

documents = loader.load()

text = documents[0].page_content

print("Total Characters:", len(text))

print("\nPreview:\n")
print(text[:500])