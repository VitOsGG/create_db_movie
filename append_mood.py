from all_movie_off_mood import all_movie_off_modd

mood = ['Любопытство', 'Восторг', 'Радость', 'Гнев', 'Грусть', 'Страх', 'Симпатия', 'Интерес']

all_movie_on_mood = []

for m in all_movie_off_modd:
    for p in m:
        if p == 'приключения' or p == 'детектив' or p == 'биография' or p == 'триллер':
            m.append(mood[0])
            all_movie_on_mood.append(m)
        if p == 'аниме ' or p == 'анимация' or p == 'сказка' or p == 'детский':
            m.append(mood[1])
            all_movie_on_mood.append(m)
        if p == 'мюзикл' or p == 'семейный' or p == 'комедия' or p == 'короткометражный':
            m.append(mood[2])
            all_movie_on_mood.append(m)
        if p == 'криминал' or p == 'боевик' or p == 'военный':
            m.append(mood[3])
            all_movie_on_mood.append(m)
        if p == 'драма':
            m.append(mood[4])
            all_movie_on_mood.append(m)
        if p == 'ужасы' or p == 'мистика':
            m.append(mood[5])
            all_movie_on_mood.append(m)
        if p == 'мелодрама' or p == 'фэнтези' or p == 'фантастика':
            m.append(mood[6])
            all_movie_on_mood.append(m)
        if p == 'спорт' or p == 'исторический' or p == 'документальный' or p == 'вестерн':
            m.append(mood[7])
            all_movie_on_mood.append(m)

print(len(all_movie_on_mood))

print(all_movie_on_mood)