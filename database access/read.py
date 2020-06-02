import sqlite3

conn = sqlite3.connect('test.db')
c=conn.cursor()

c.execute('SELECT * FROM player')
query=c.fetchall()
for row in query:
    name=row[0]
    value=row[3]
    print("{} value is {}".format(row[0],row[3]))
conn.commit()
conn.close()
