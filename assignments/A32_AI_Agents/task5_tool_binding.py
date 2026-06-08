import os

from langchain_groq import ChatGroq

from langchain.tools import tool

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

@tool
def calculator(
    expression: str
):
    return str(eval(expression))

tools = [calculator]

llm_with_tools = llm.bind_tools(
    tools
)

response = llm_with_tools.invoke(
    "What is 20 * 5?"
)

print(response)