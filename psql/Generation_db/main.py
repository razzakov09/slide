import psycopg2

conn = psycopg2.connect(
    database = 'followers',
    user='Avtandil',
    password='12345',
    host='localhost',
    port=5432
)

cur = conn.cursor()
cur.execute("DELETE FROM narodnii WHERE day_to_expire < 1")
print(cur.fetchall())