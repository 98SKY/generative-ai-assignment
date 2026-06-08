from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

with open("data/sample_document.txt", "r") as f:
    text = f.read()

llm = ChatGroq(model="llama-3.1-8b-instant")

short_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Summarize in 5 lines.

{text}
"""
)

bullet_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Summarize as bullet points.

{text}
"""
)

print("SHORT SUMMARY")
print((short_prompt | llm).invoke({"text": text}).content)

print("\nBULLET SUMMARY")
print((bullet_prompt | llm).invoke({"text": text}).content)