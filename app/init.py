def db_init():
    import psycopg2
    conn = psycopg2.connect(
    database = "main_db", 
    user = "postgres", 
    host = "db",
    password = "a1s2d3f4",
    port = 5432)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: create datacamp_courses table
    cur.execute("""
    CREATE TABLE fst (
        id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        age INTEGER);
    """)


    cur.execute("INSERT INTO fst(name, age) VALUES('AAA', 16)")
    cur.execute("INSERT INTO fst(name, age) VALUES('BBB', 21)")
    cur.execute("INSERT INTO fst(name, age) VALUES ('CCC', 36)")


    # Make the changes to the database persistent
    conn.commit()

    # Close cursor and communication with the database
    cur.close()
    conn.close()

if __name__ == "__main__":
    db_init()