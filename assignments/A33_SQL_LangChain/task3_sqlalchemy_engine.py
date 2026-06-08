from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///company.db"
)

with engine.connect() as conn:

    result = conn.exec_driver_sql(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """
    )

    print("\nTables:")

    for row in result:

        print(row[0])