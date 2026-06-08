from langchain.tools import tool

@tool
def company_policy_lookup(
    query: str
) -> str:
    """
    Returns company policy information.
    """

    policies = {

        "leave":
        "Employees get 24 paid leaves annually.",

        "work from home":
        "WFH allowed 3 days per week.",

        "dress code":
        "Smart casual attire."
    }

    return policies.get(
        query.lower(),
        "Policy not found."
    )

print(
    company_policy_lookup.invoke(
        "leave"
    )
)