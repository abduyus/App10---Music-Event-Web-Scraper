import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor =  connection.cursor()

# Query data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
row = cursor.fetchall()
print(row)


cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
row2 = cursor.fetchall()
print(row2)

# Inserting new rows
new_rows = [('Cats', 'Cats City', '2088.10.15')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()