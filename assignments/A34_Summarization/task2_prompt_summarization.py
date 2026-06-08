from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

with open("data/sample_document.txt", "r") as f:
    text = f.read()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["text"],
    template="""
You are an expert summarizer.

Summarize the following text:

{text}
"""
)

chain = prompt | llm

response = chain.invoke({"text": text})

print(response.content)