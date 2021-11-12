import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS stores(location TEXT, store_id INTEGER)"""

cursor.execute(command1)

#command2 = """CREATE TABLE IF NOT EXISTS
#purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, 
#FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

#cursor.execute(command2)

cursor.execute("INSERT INTO stores VALUES('yah', 21)")


#cursor.execute("INSERT INTO purchases VALUES (543, 21, 15.49)")

cursor.execute("SELECT * FROM stores")
connection.commit()
results = cursor.fetchall()
print(results)


#cursor.execute('''CREATE TABLE IF NOT EXISTS Media(id INTEGER PRIMARY KEY, title TEXT, type TEXT,  genre TEXT,onchapter INTEGER,  chapters INTEGER,
# status TEXT)''')


#values = [
#{'title':'jack'}, {'type':None, 'genre':'Action', 'onchapter':None, 'chapters':6,'status':'Ongoing'}]
values2 = {'title':'jack', 'type':None, 'genre':'Action', 'onchapter':None, 'chapters':6,'status':'Ongoing'}
#cursor.execute('INSERT INTO Media(title, type, onchapter, chapters, status) VALUES (:title, :type, :onchapter, :chapters, :status)',  values2)


#table = """CREATE TABLE IF NOT EXISTS project(name TEXT, begin_date TEXT, end_date TEXT)""" 
#cursor.execute(table)
#project = ("INSERT INTO project VALUES('Practice', '11-06-2021', '11-05-2021')")
#cursor.execute(project)