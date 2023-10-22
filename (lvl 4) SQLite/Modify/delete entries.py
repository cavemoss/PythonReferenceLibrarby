import sqlite3
connection = sqlite3.connect('../database.db')
cursor = connection.cursor()

# Delete a record (Drop record form the Table)
cursor.execute("DELETE FROM database WHERE rowid = 6")
connection.commit()

cursor.execute("SELECT rowid, * FROM database")
for item in cursor.fetchall():
    print(item)


connection.close()
