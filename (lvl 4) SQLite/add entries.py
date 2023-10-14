import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Add an Entry to the database
cursor.execute("INSERT INTO database VALUES ('Alexandr', 'Shushakov', 19, 'alexshu1812@gmail.com')")
cursor.execute("INSERT INTO database VALUES ('Genichiro', 'Ashina', 21, 'glory@ashina.com')")

# Add Multiple Entries to the database
many_entries = [('Wes', 'Brown', 26, 'wes@codemy.com'),
                ('Steph', 'Kuewa', 20, 'steph@kuewa.com'),
                ('Mary', 'Brown', 28, 'mary@codemy.com'),
                ('Dan', 'Pas', 69, 'dan@pas.com')]
cursor.executemany("INSERT INTO database VALUES (?,?,?,?)", many_entries)


connection.commit()
connection.close()
