import sqlite3
from datetime import datetime

conn = sqlite3.connect('patients.db')
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE patients
#                   (name text, lastname text, birthday int,
#                   address text, height int, weight int)
#                """)

name = input("name: ")
lastname = input("lastname")
birthday = datetime.strptime(input("birthday: "), '%d.%m.%Y').date()
address = input("address: ")
height = input("height: ")
weight = input("weight: ")

cursor.execute('INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?)',
    (name, lastname, birthday, address, height, weight))

conn.commit()