import sqlite3
connection = sqlite3.connect('../database.db')
cursor = connection.cursor()

# Search through the database
cursor.execute("SELECT * FROM database WHERE last_name = 'Ashina'")
print(cursor.fetchall())

cursor.execute("SELECT * FROM database WHERE age > 20")
print(cursor.fetchall())

cursor.execute("SELECT * FROM database WHERE last_name LIKE '%sh%'")
print(cursor.fetchall())

cursor.execute("SELECT * FROM database WHERE first_name LIKE 'G%ro'")
print(cursor.fetchall())

cursor.execute("SELECT * FROM database WHERE email LIKE '%@codemy.com'")
print(cursor.fetchall())


connection.close()
