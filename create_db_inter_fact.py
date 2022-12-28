import sqlite3 as sql
from inter_fact import list_inter_fact


base = sql.connect('inter_movie_fact.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(fact TEXT)'.format('inter_movie_fact'))

cur.executemany('INSERT INTO inter_movie_fact VALUES(?)', (list_inter_fact))

base.commit()
