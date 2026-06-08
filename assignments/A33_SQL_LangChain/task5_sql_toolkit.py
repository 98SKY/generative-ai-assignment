import os

from langchain_groq import ChatGroq

from langchain_community.utilities import (
    SQLDatabase
)

from langchain_community.agent_toolkits import (
    SQLDatabaseToolkit
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

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=llm
)

tools = toolkit.get_tools()

for tool in tools:

    print(tool.name)