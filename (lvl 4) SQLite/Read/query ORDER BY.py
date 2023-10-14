import sqlite3
connection = sqlite3.connect('../database.db')
cursor = connection.cursor()

# Query the database ORDER BY
cursor.execute("SELECT rowid, * FROM database ORDER BY last_name DESC")  # ASC; DESC
for item in cursor.fetchall():
    print(item)


connection.close()
