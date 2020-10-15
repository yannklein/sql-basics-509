import sqlite3

conn = sqlite3.connect("data/soccer.sqlite")
conn.row_factory = sqlite3.Row
c = conn.cursor()

# c.execute("SELECT * FROM Country")
# rows = c.fetchall()

c.execute("SELECT * FROM Country WHERE Country.id = 17642")
rows = c.fetchone()

print(rows[0]['name'])
print(rows[1]['id'])
