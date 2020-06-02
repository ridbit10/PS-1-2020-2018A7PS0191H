import sqlite3

conn = sqlite3.connect('test.db')
c=conn.cursor()

nm=('messi',)
c.execute('SELECT * FROM player WHERE name=?',nm)
print(c.fetchone())
#two different ways to print queries
clb=('barca',)
c.execute('SELECT * FROM player WHERE club=?',clb)
print(c.fetchall())
for row in c.execute('SELECT * FROM player WHERE club=?',clb):
    print(row)
#conn.commit()#persistent in nature
conn.close()
