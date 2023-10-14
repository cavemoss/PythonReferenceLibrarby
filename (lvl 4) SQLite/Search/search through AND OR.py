import sqlite3
connection = sqlite3.connect('../database.db')
cursor = connection.cursor()

# Search through the database AND OR
cursor.execute("SELECT rowid, * FROM database WHERE last_name LIKE 'Br%' AND rowid = 3")
print(cursor.fetchall())

cursor.execute("SELECT * FROM database WHERE last_name LIKE '%sh%' OR age < 20")
print(cursor.fetchall())


connection.close()
