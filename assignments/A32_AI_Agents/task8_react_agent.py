import os

from langchain_groq import ChatGroq

from langchain.tools import tool

from langchain.agents import (
    create_react_agent,
    AgentExecutor
)

from langchain import hub

@tool
def calculator(
    expression: str
) -> str:
    """
    Performs math calculations.
    """
    return str(eval(expression))

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

tools = [calculator]

prompt = hub.pull(
    "hwchase17/react"
)

agent = create_react_agent(
    llm,
    tools,
    prompt
)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

result = executor.invoke(
    {
        "input":
        "What is 100 * 25?"
    }
)

print(
    result["output"]
)