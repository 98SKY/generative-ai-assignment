import os

from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = ""

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

response = llm.invoke(
    "What is Generative AI?"
)

print(response.content)