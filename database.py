import sqlite3

def get_connection():
    conn = sqlite3.connect("ingres.db")
    conn.row_factory = sqlite3.Row
    return conn

def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result