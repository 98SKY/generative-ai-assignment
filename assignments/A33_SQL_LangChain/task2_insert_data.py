import sqlite3

conn = sqlite3.connect(
    "company.db"
)

cursor = conn.cursor()

employees = [

    (1,"John","IT",70000),
    (2,"Alice","HR",55000),
    (3,"Bob","Finance",80000),
    (4,"Emma","IT",90000),
    (5,"David","Sales",60000),
    (6,"Sophia","HR",65000),
    (7,"Michael","Finance",85000),
    (8,"James","IT",75000),
    (9,"Olivia","Sales",62000),
    (10,"William","Marketing",58000)
]

cursor.executemany(
    """
    INSERT OR REPLACE INTO employees
    VALUES (?, ?, ?, ?)
    """,
    employees
)

sales = [

    (1,1,5000,"2026-01-01"),
    (2,2,7000,"2026-01-02"),
    (3,3,9000,"2026-01-03"),
    (4,4,6000,"2026-01-04"),
    (5,5,8000,"2026-01-05"),
    (6,6,4000,"2026-01-06"),
    (7,7,3000,"2026-01-07"),
    (8,8,7500,"2026-01-08"),
    (9,9,6500,"2026-01-09"),
    (10,10,5500,"2026-01-10")
]

cursor.executemany(
    """
    INSERT OR REPLACE INTO sales
    VALUES (?, ?, ?, ?)
    """,
    sales
)

conn.commit()

print("Data Inserted")

conn.close()