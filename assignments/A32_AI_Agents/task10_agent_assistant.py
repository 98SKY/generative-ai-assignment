import os

from langchain_groq import ChatGroq

from langchain.tools import tool

@tool
def calculator(
    expression: str
):
    return str(eval(expression))

@tool
def company_policy(
    query: str
):
    return (
        "Employees receive "
        "24 annual leaves."
    )

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

while True:

    q = input("\nAsk: ")

    if q.lower() == "exit":
        break

    if any(
        x in q
        for x in ["+", "-", "*", "/"]
    ):
        try:
            print(
                calculator.invoke(q)
            )
        except:
            print(
                "Invalid expression"
            )

    elif "leave" in q.lower():

        print(
            company_policy.invoke(
                "leave"
            )
        )

    else:

        response = llm.invoke(q)

        print(
            response.content
        )