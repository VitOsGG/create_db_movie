import sqlite3 as sql
from fact import b


base = sql.connect('inter_movie_fact_2.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(fact TEXT)'.format('inter_movie_fact_2'))

cur.executemany('INSERT INTO inter_movie_fact_2 VALUES(?)', (b))

base.commit()
