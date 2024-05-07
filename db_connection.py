import sqlite3

def execute_sql(intent, table):
    # Connect to your database
    conn = sqlite3.connect('C:/sqlite/chinook/chinook.db')
    cursor = conn.cursor()

    # Example: executing a SELECT query
    if intent == "SELECT":
        try:
            cursor.execute(f"SELECT * FROM {table}")
            results = cursor.fetchall()
            return str(results)  # Returning results as a string for simplicity
            
        except Exception as e:
            # return str(e)  # Return the error message if something goes wrong
            return f"SELECT * FROM {table}"

    return "No intent found"
