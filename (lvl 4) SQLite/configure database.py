import sqlite3

# Create the database Connection
connection = sqlite3.connect('database.db')  # sqlite3.connect('../database.db'); sqlite3.connect(':memory:')

# Crete a Cursor
cursor = connection.cursor()

# Create a Table
cursor.execute("""CREATE TABLE database (
    first_name text, 
    last_name text, 
    age integer,
    email text
)""")  # Datatypes: null, integer, real, text, blob


# Commit the change
connection.commit()

# Close the connection
connection.close()
