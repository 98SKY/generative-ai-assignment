from langchain_community.utilities import (
    SQLDatabase
)

db = SQLDatabase.from_uri(
    "sqlite:///company.db"
)

print(
    db.get_usable_table_names()
)

print("\nSchema:\n")

print(
    db.get_table_info()
)