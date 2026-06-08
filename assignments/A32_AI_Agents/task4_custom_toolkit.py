from datetime import datetime

from langchain.tools import tool

@tool
def policy_lookup(
    query: str
):
    return "Leave policy available."

@tool
def employee_db(
    emp_id: str
):
    return f"Employee {emp_id} Active"

@tool
def current_time(
    text: str
):
    return str(
        datetime.now()
    )

toolkit = [
    policy_lookup,
    employee_db,
    current_time
]

for t in toolkit:
    print(t.name)