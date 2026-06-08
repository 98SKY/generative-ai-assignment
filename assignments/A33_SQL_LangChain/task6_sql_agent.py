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

response = agent.invoke(
    {
        "input":
        "Who has highest salary?"
    }
)

print(response)