# create_db_movie
![Python](https://img.shields.io/badge/Python-3.11.0-yellow) ![aiogram](https://img.shields.io/badge/sqlite3-blue)

Данный проект был реализован для создания баз данных для использования их в telegram-боте.
___

Ссылка на проект telegram-боте и парсер информации о фильмах:
* [Проект telegram-бота по подбору фильмов](https://github.com/VitOsGG/search_movie_telegram_bot)
* [Парсер фильмов для базы данных](https://github.com/VitOsGG/parser_movie)

___

**Структура проекта:**
* Папка venv

  Стандартная папка с виртуальный окружением. В данном проекте использовалась только стандартная библиотека sqlite3
    
* Папка afisha_movies

  Папка с афишами фильмов полученными после парсинга сайта с фильмами
  
* Папка afisha_movie_test

  Папка с афишами фильмов для тестовой базы данных
  
* Файлы в корневой папке:

  * create_db_test_movie.py - файл создания тестовой базы данных фильмов, необходимой для создания и настройки бота
  
  * create_db_inter_fact.py - файл создания базы данных интересных фактов, необходимой для одной из функциональных ветвей бота
    
  * inter_fact.py - файл с списком интересных фактов для БД
  
  * create_db_movie.py - файл создания основной базы данных фильмов для работы готового проекта бота
   
  * all_movie_off_mood.py - файл с списком фильмов и информации о каждом фильме без добавления параметра "эмоция"
  
  * all_movie_on_mood.py - файл с списком фильмов и информации о каждом фильме после добавления параметра "эмоция"
  
  * append_mood.py- файл с функцией добавления параметра "эмоция" для каждого фильма в зависимости от жанра
  
  * inter_movie_fact.db - полученная база данных инетесных фактов
  
  * movie_db_on_mood.db - полученная база данных фильмов
  
  * movie_db_test.db - полученная тестовая база данных фильмов
  
  * .gitattributes - служебный файл (создается при использование Git LFS, потому что Git Hub не принимает файлы более 100 Мб, а БД фильмво весит больше)
  
 * Реализация 
  
  -Файл create_db_inter_fact.py. Создание БД с интересные фактами:
  
```python
import sqlite3 as sql
from inter_fact import list_inter_fact


base = sql.connect('inter_movie_fact.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(fact TEXT)'.format('inter_movie_fact'))

cur.executemany('INSERT INTO inter_movie_fact_2 VALUES(?)', (list_inter_fact))

base.commit()
```
Список с интересными фактами - list_inter_fact находится в файле inter_fact.py


-Файл create_db_test_movie.py. Создание тестовой БД с фактами:


```python
base = sql.connect('movie_db_test.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(img BLOB, name PRIMARY KEY, rating NUMERIC(3, 2), country TEXT, '
             'genre TEXT, '
             'description TEXT, emotion TEXT)'.format('movie_db_test'))

cur.execute('INSERT INTO movie_db_test VALUES (?, ?, ?, ?, ?, ?, ?)', (
    open('afisha_movie_test/1.jpg', 'rb').read(), 'Однажды в Голливуде', 7.6, 'США', 'драма',
    'Можно ли переписать историю? Самый ностальгический фильм Тарантино — с Шэрон Тейт, Брюсом Ли и Чарли Мэнсоном',
    'Любопытсво'))
base.commit()
```

Аналогично в БД записано еще 17 фильмов

-Файл create_db_movie.py. Создание основной БД с фильмами:

Создание БД

```python
base = sql.connect('movie_db_on_mood.db')
cur = base.cursor()

base.execute(
    'CREATE TABLE IF NOT EXISTS {}(img BLOB, name TEXT, rating NUMERIC(3, 2), country TEXT, genre TEXT, description '
    'TEXT, mood TEXT)'.format(
        'movie_db_on_mood_tab'))
base.commit()
```

Конвертирование афиш в байтовый код и добавления кода к списку с информацией о фильмах
  
```python
movie_db_on_mood = []
for i in range(1, 995):
    for v in all_movie_on_mood:
        img = open(f"afisha_movie/{i}.jpg", "rb").read()
        v.insert(0, img)
        movie_db_on_mood.append(v)
        all_movie_on_mood.remove(v)
        break
```

Создание таблицы с фильмами в БД
  
```python
cur.executemany("INSERT INTO movie_db_on_mood_tab(img, name, rating, country, genre, description, mood)  VALUES (?, "
                "?, "
                "?, ?, "
                "?, ?, ?)", movie_db_on_mood)
base.commit()
```
