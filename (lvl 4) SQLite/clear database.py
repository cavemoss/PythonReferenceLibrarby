import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Clear table off entries
cursor.execute("DELETE FROM database")

# Delete table (Drop Table)
cursor.execute("DROP TABLE database")

connection.commit()
connection.close()
