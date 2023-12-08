import psycopg2

try:
    # Update port to the correct one (default is usually 5432)
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456789", port=5432)
    
    cur = conn.cursor()

    # Create table query with corrected syntax
    cur.execute("""CREATE TABLE IF NOT EXISTS person (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
    );""")

    cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
    (1, 'Mike', 30, 'm'),
    (2, 'Lisa', 30, 'f'),
    (3, 'John', 54, 'm'),
    (4, 'Bob', 80, 'm'),
    (5, 'Julie', 30, 'f');
""")

    cur.execute("""SELECT * FROM person WHERE name = 'Bob';""")

    print(cur.fetchone())

    cur.execute("""SELECT * FROM person WHERE age < 50;""")

    for row in cur.fetchall():
        print(row)

    sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""", ("J", 50))

    print(sql)

    cur.execute(sql)

    print(cur.fetchall())

    conn.commit()


except psycopg2.Error as e:
    print("Error:", e)

finally:
    # Close cursor and connection in the finally block
    if cur:
        cur.close()
    if conn:
        conn.close()
