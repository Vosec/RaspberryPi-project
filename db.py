import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''CREATE TABLE measurements
                (date time, type text, data real)''')



c.execute("INSERT INTO measurements VALUES ('2019-02-08 10:15:14', 'prutok', 11)")
c.execute("INSERT INTO measurements VALUES ('2019-02-05 10:15:14', 'prutok', 50.05)")
c.execute("INSERT INTO measurements VALUES ('2019-02-03 10:15:14', 'tlak', 40.05)")
c.execute("INSERT INTO measurements VALUES ('2019-02-08 10:15:14', 'tlak', 18)")



conn.commit()
conn.close()