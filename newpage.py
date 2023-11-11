import sqlite3

connection = sqlite3.connect("abc.db")
cursor = connection.cursor()
cursor.execute("select * from students")
print(cursor.fetchall())
connection.close()