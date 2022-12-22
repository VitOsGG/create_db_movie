from all_movie_off_mood import all_movie_off_modd

a = ['Любопытство', 'Восторг', 'Радость', 'Гнев', 'Грусть', 'Страх', 'Симпатия', 'Интерес']

all_movie_on_mood = []

for m in all_movie_off_modd:
    for p in m:
        if p == 'приключения' or p == 'детектив' or p == 'биография' or p == 'триллер':
            m.append(a[0])
            all_movie_on_mood.append(m)
        if p == 'аниме ' or p == 'анимация' or p == 'сказка' or p == 'детский':
            m.append(a[1])
            all_movie_on_mood.append(m)
        if p == 'мюзикл' or p == 'семейный' or p == 'комедия' or p == 'короткометражный':
            m.append(a[2])
            all_movie_on_mood.append(m)
        if p == 'криминал' or p == 'боевик' or p == 'военный':
            m.append(a[3])
            all_movie_on_mood.append(m)
        if p == 'драма':
            m.append(a[4])
            all_movie_on_mood.append(m)
        if p == 'ужасы' or p == 'мистика':
            m.append(a[5])
            all_movie_on_mood.append(m)
        if p == 'мелодрама' or p == 'фэнтези' or p == 'фантастика':
            m.append(a[6])
            all_movie_on_mood.append(m)
        if p == 'спорт' or p == 'исторический' or p == 'документальный' or p == 'вестерн':
            m.append(a[7])
            all_movie_on_mood.append(m)

print(len(all_movie_on_mood))

print(all_movie_on_mood)

