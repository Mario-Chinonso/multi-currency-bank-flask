import sqlite3 as sql
import random
conn = sql.connect('database.db')

cur = conn.cursor()

def generate_account_number(conn: sql.Connection) -> str:
    """Generates a unique 10-digit random account number.

    Ensures the number starts with a non-zero digit and doesn't already exist
    in the database.
    """
    cur = conn.cursor()
    while True:
        # Generates a random integer between 1000000000 and 9999999999
        acc_num = str(random.randint(1000000000, 9999999999))

        # Check if this account number already exists
        cur.execute(
            "SELECT 1 FROM Account_Number WHERE Number = ?", (acc_num,)
        )
        if not cur.fetchone():
            return acc_num

cur.execute("""
   INSERT INTO Account_Number(UserID, Number)
   VALUES (?, ?)
""", (19, generate_account_number(conn)))
conn.commit()
conn.close()