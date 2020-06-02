import sqlite3

conn = sqlite3.connect('test.db')
c=conn.cursor()

c.execute('''CREATE TABLE player
             (name text, club text, jersey no real, value real)''')

c.execute("INSERT INTO player VALUES('messi','barca',10,1000)")
conn.commit()#persistent in nature
conn.close()
