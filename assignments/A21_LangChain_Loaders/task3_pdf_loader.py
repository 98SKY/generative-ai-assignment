from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/sample.pdf")

documents = loader.load()

print("Total Pages:", len(documents))

print("\nPage Content:")
print(documents[0].page_content[:500])