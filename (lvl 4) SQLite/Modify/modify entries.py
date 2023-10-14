import sqlite3
connection = sqlite3.connect('../database.db')
cursor = connection.cursor()

# Modify the records
cursor.execute("""UPDATE database 
        SET last_name = 'Bastard' WHERE first_name LIKE 'G%ro'
""")
cursor.execute("""UPDATE database 
        SET last_name = 'Ashina' WHERE rowid = 2
""")
connection.commit()

cursor.execute("SELECT rowid, * FROM database")
for item in cursor.fetchall():
    print(item)


connection.close()
