import sqlite3

# Create the Database Connection
connection = sqlite3.connect('database.db')  # sqlite3.connect('../database.db'); sqlite3.connect(':memory:')

# Crete a Cursor
cursor = connection.cursor()

# Create a Table (there could be multiple Tables within a Database)
cursor.execute("""CREATE TABLE IF NOT EXISTS database (  
    first_name TEXT, 
    last_name TEXT, 
    age INTEGER,
    email TEXT
)""")  # Datatypes: NULL, INTEGER, REAL, TEXT, BLOB


# Commit the change
connection.commit()

# Close the connection
connection.close()
