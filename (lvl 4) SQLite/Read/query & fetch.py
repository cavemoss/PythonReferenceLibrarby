import sqlite3
connection = sqlite3.connect('../database.db')
cursor = connection.cursor()

# Query the database
cursor.execute("SELECT * FROM database")

# Fetch data
items = cursor.fetchall()  # cursor.fetchone()[1]; cursor.fetchmany(3)
print(type(items), items, end='\n\n')

# Print out formatted data
for item in items:
    print(item[0] + ' ' + item[1] + ' ' + str(item[2]) + ' | ' + item[3])
print('')

# Print out data along with the Primary Key
cursor.execute("SELECT rowid, * FROM database")
for item in cursor.fetchall():
    print(item)

connection.close()
