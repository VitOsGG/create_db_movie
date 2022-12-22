import sqlite3 as sql
from all_movie_on_mood import all_movie_on_mood

base = sql.connect('movie_db_on_mood.db')
cur = base.cursor()

base.execute(
    'CREATE TABLE IF NOT EXISTS {}(img BLOB, name TEXT, rating NUMERIC(3, 2), country TEXT, genre TEXT, description '
    'TEXT, mood TEXT)'.format(
        'movie_db_on_mood_tab'))
base.commit()


movie_db_on_mood = []
for i in range(1, 995):
    for v in all_movie_on_mood:
        img = open(f"afisha_movie/{i}.jpg", "rb").read()
        v.insert(0, img)
        movie_db_on_mood.append(v)
        all_movie_on_mood.remove(v)
        break

cur.executemany("INSERT INTO movie_db_on_mood_tab(img, name, rating, country, genre, description, mood)  VALUES (?, "
                "?, "
                "?, ?, "
                "?, ?, ?)", movie_db_on_mood)
base.commit()


