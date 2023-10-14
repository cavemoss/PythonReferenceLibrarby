import sqlite3
import os
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Clear database (Drop Table)
cursor.execute("Drop Table database")

connection.commit()
