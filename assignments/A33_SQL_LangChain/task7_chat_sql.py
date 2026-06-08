import os

from langchain_groq import ChatGroq

from langchain_community.utilities import (
    SQLDatabase
)

from langchain_community.agent_toolkits import (
    create_sql_agent
)

db = SQLDatabase.from_uri(
    "sqlite:///company.db"
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)

questions = [

    "How many employees are there in each department?",

    "Who has highest salary?",

    "What is total sales amount?",

    "Average salary by department?"
]

for q in questions:

    print("\n================")
    print(q)

    result = agent.invoke(
        {"input": q}
    )

    print(
        result["output"]
    )