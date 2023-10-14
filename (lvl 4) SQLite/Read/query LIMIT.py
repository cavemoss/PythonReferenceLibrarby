import sqlite3
connection = sqlite3.connect('../database.db')
cursor = connection.cursor()

# Query the database LIMIT
cursor.execute("SELECT rowid, * FROM database LIMIT 3")
for item in cursor.fetchall():
    print(item)


connection.close()
