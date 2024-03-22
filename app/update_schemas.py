# this goes through a db
# and generates create table statements
# for each table in the db.

def generate_create_table(db):
    conn = create_connection(db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        cursor.execute(f"SELECT sql FROM sqlite_master WHERE name = '{table[0]}';")
        print(cursor.fetchone()[0])
    conn.close()
    return