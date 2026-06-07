from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    "https://python.langchain.com/docs/introduction/"
)

documents = loader.load()

print(documents[0].page_content[:500])