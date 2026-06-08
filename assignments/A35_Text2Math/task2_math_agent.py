import os

from langchain_groq import ChatGroq

from langchain.agents import initialize_agent
from langchain.agents import AgentType

from langchain.tools import Tool

# ---------------------------
# LLM
# ---------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# ---------------------------
# Calculator Tool
# ---------------------------

def calculator(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

math_tool = Tool(
    name="Calculator",
    func=calculator,
    description="""
Useful for solving mathematical expressions.
Input should be a valid math expression.
Example:
25*4
100/5
"""
)

# ---------------------------
# Agent
# ---------------------------

agent = initialize_agent(
    tools=[math_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# ---------------------------
# Test Cases
# ---------------------------

questions = [
    "What is 15 percent of 800?",
    "A shop gives 20 percent discount on 1500 rupees. What is final price?",
    "What is 45 multiplied by 78?",
    "Solve 25 + 35 * 2"
]

for q in questions:
    print("\nQUESTION:")
    print(q)

    result = agent.invoke(q)

    print("\nANSWER:")
    print(result["output"])