import psycopg2
from init import db_init

#db_init()

conn = psycopg2.connect(
    database = "main_db", 
    user = "postgres", 
    host = 'db',
    password = "a1s2d3f4",
    port = 5432)


cur = conn.cursor()
cur.execute('SELECT * FROM fst;')
rows = cur.fetchall()

conn.commit()
conn.close()

for row in rows:
    print("\t", row)

#print("hello world")