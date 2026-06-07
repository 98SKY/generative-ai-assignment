import os

from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

response = llm.invoke(
    "What is Generative AI?"
)

print(response.content)