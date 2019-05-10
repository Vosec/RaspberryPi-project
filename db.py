import sqlite3
#skript pro vytvoreni DB
conn = sqlite3.connect('measurements.db')
c = conn.cursor()

c.execute('''CREATE TABLE measurements
                (date time, type text, data real)''')

conn.commit()
conn.close()