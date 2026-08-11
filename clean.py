import sqlite3 as sql

conn = sql.connect("database.db")
cur = conn.cursor()

cur.execute("""
   
""")
conn.commit()
conn.close()