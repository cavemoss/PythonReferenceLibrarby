import sqlite3
connection = sqlite3.connect('../database.db')
cursor = connection.cursor()

# Query the data along with the Primary Key
cursor.execute("SELECT rowid, * FROM database")
for item in cursor.fetchall():
    print(item)


connection.close()
