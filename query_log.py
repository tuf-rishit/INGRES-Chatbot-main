import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS query_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query_text TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("Table created successfully")