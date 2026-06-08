from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    "data/sample.pdf"
)

pages = loader.load()

print("Total Pages:", len(pages))

print("\nSample Content:\n")

print(
    pages[0].page_content[:500]
)