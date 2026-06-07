from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("data/sample.csv")

documents = loader.load()

print("Rows Loaded:", len(documents))

print("\nSample Row:")
print(documents[0].page_content)