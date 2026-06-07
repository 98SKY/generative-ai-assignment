from langchain_openai import OpenAIEmbeddings

# Requires OpenAI API Key

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

text = "LangChain is used for Generative AI applications."

vector = embeddings.embed_query(text)

print("Embedding Length:", len(vector))
print(vector[:10])