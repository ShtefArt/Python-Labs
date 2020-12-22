import sqlite3

conn = sqlite3.connect('patients.db')
cursor = conn.cursor()

cursor.execute("""SELECT * FROM patients
                  ORDER BY height DESC
              """)

print("The highest patient: ", cursor.fetchone())

cursor.execute("""SELECT sum(weight) as sum FROM patients
                  ORDER BY height
              """)

print("Total weight: ", cursor.fetchone()[0])
