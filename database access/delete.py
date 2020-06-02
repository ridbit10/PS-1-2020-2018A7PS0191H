import sqlite3

conn = sqlite3.connect('test.db')
c=conn.cursor()

clb=('psg',)
c.execute('DELETE FROM player WHERE club=?',clb)
c.execute('SELECT * FROM player')
print(c.fetchall())
conn.commit()
conn.close()
