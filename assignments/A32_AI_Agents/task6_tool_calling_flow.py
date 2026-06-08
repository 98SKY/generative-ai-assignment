import os

from langchain_groq import ChatGroq
from langchain.tools import tool

# -----------------------------
# LLM
# -----------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# -----------------------------
# TOOLS
# -----------------------------

@tool
def calculator(expression: str) -> str:
    """
    Perform mathematical calculations.
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


@tool
def company_policy_lookup(query: str) -> str:
    """
    Returns company policy information.
    """

    policies = {
        "leave":
        "Employees get 24 paid leaves annually.",

        "wfh":
        "Employees can work from home 3 days per week.",

        "dress code":
        "Smart casual dress code is required."
    }

    return policies.get(
        query.lower(),
        "Policy not found."
    )

# -----------------------------
# TOOL CALL FLOW
# -----------------------------

def process_query(query):

    print("\n======================")
    print("USER QUERY:")
    print(query)

    # Tool Selection

    if any(op in query for op in ["+", "-", "*", "/"]):

        print("\nTOOL SELECTED:")
        print("Calculator")

        result = calculator.invoke(query)

        print("\nTOOL OUTPUT:")
        print(result)

        print("\nFINAL ANSWER:")
        print(result)

    elif "leave" in query.lower():

        print("\nTOOL SELECTED:")
        print("Company Policy Lookup")

        result = company_policy_lookup.invoke(
            "leave"
        )

        print("\nTOOL OUTPUT:")
        print(result)

        print("\nFINAL ANSWER:")
        print(result)

    else:

        print("\nTOOL SELECTED:")
        print("LLM")

        response = llm.invoke(query)

        print("\nFINAL ANSWER:")
        print(response.content)


# -----------------------------
# TEST CASES
# -----------------------------

queries = [

    "25 * 8",

    "What is the leave policy?",

    "What is Generative AI?"
]

for q in queries:

    process_query(q)