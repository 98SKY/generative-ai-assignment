import sqlite3

conn = sqlite3.connect(
    "company.db"
)

cursor = conn.cursor()

# Employees Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (

    id INTEGER PRIMARY KEY,

    name TEXT,

    department TEXT,

    salary INTEGER
)
""")

# Sales Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (

    sale_id INTEGER PRIMARY KEY,

    employee_id INTEGER,

    amount INTEGER,

    sale_date TEXT
)
""")

conn.commit()

print(
    "Database Created Successfully"
)

conn.close()