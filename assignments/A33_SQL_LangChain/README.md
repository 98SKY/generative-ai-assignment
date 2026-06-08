# Assignment 33: Chat with SQL Database using LangChain

## Objective

Build a Chat-with-SQL application using LangChain and SQL Agents.

The application should:

- Store company data in SQLite
- Connect using SQLAlchemy
- Create a LangChain SQLDatabase object
- Build an SQL Agent
- Answer natural language questions
- Connect to MySQL Workbench database

---

## Technologies Used

- Python
- SQLite
- MySQL Workbench
- SQLAlchemy
- LangChain
- Groq/OpenAI/Ollama

---

## Project Structure

```text
A33_Chat_With_SQL/

├── company.db
├── task1_create_sqlite_db.py
├── task2_insert_sample_data.py
├── task3_sqlalchemy_engine.py
├── task4_langchain_sqldb.py
├── task5_sql_toolkit.py
├── task6_sql_agent.py
├── task7_chat_with_sql.py
├── task8_ambiguous_queries.py
├── mysql_connection.py
├── observations.md
```


---

# observations.md

```md
# Observations & Insights

## 1. Why SQL Agents are better than manual SQL generation

SQL Agents automatically understand user questions and generate SQL queries dynamically. Business users do not need SQL knowledge.

---

## 2. Difference between SQL Agent and RAG

### SQL Agent

- Works on structured data
- Generates SQL queries
- Retrieves exact records

### RAG

- Works on unstructured documents
- Retrieves text chunks
- Generates answers using retrieved context

---

## 3. Risks of unrestricted SQL access

- Data leakage
- Accidental table deletion
- Unauthorized updates
- Security vulnerabilities

Proper permissions and read-only access should be used.

---

## 4. Advantages of SQL Agents

- Natural language interface
- Dynamic query generation
- Faster analytics
- Business-friendly access to databases

---

## 5. Challenges

- Complex joins
- Ambiguous user questions
- Large database schemas
- Query optimization
