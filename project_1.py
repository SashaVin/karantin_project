
def film_of_act(actor, dct, lst):
    for j in dct.keys():
        if actor in dct[j]:
            lst.append(j)
    return lst


with open('film.txt', encoding='utf-8') as film:
    lst_film = film.readlines()

name = []
actors = set()
dct_f_act = {}
for i in lst_film:
    a, b = i.split(': ')
    name.append(a)
    z = b.split(', ')
    z[-1] = z[-1][:-4]
    lst_actors = set(z)
    actors = actors.union(lst_actors)
    dct_f_act[a] = lst_actors

q = 0
while q > -1:
    print('1. Работа с фильмами\n2. Работа с актерами')
    q = int(input('Выберите тип работы (1 или 2): '))
    print()
    if q == 1:
        print(name)
        print('1. Определить актерский состав двух фильмов\n2. Определить актеров, игравших в обоих фильмах')
        print('3. Определить актеров, участвующих в съемках первого, но не участвующих в съемках второго')
        print('4. Вернуться в прошлое меню')
        r = int(input('Введите действие (1, 2, 3 или 4): '))
        print()
        if r == 1:
            f1 = input('Введите название первого фильма: ')
            f2 = input('Введите название второго фильма: ')
            print(dct_f_act[f1] | dct_f_act[f2])
        elif r == 2:
            f1 = input('Введите название первого фильма: ')
            f2 = input('Введите название второго фильма: ')
            print(dct_f_act[f1] & dct_f_act[f2])
        elif r == 3:
            f1 = input('Введите название первого фильма: ')
            f2 = input('Введите название второго фильма: ')
            print(dct_f_act[f1] - dct_f_act[f2])

        print()
        v = input('Хотите повторить? (да или нет) ')
        if v == 'да':
            q += 1
        else:
            q = -1
    elif q == 2:
        print(actors)
        print('1. Определить названия фильмов, в которых снимался хотя бы один из актеров')
        print('2. Определить названия фильмов, в которых снимались оба актера')
        print('3. Определить названия фильмов, в которых снимался первый актер, но не участвовал второй')
        print('4. Вернуться в прошлое меню')
        r = int(input('Введите действие (1, 2, 3 или 4): '))
        print()
        if r == 1:
            lst_1 = []
            lst_2 = []
            a1 = input('Введите имя первого актера: ')
            a2 = input('Введите имя второго актера: ')
            a_1 = set(film_of_act(a1, dct_f_act, lst_1))
            a_2 = set(film_of_act(a2, dct_f_act, lst_2))
            print(a_1 | a_2)
        elif r == 2:
            lst_1 = []
            lst_2 = []
            a1 = input('Введите имя первого актера: ')
            a2 = input('Введите имя второго актера: ')
            a_1 = set(film_of_act(a1, dct_f_act, lst_1))
            a_2 = set(film_of_act(a2, dct_f_act, lst_2))
            print(a_1 & a_2)
        elif r == 3:
            lst_1 = []
            lst_2 = []
            a1 = input('Введите имя первого актера: ')
            a2 = input('Введите имя второго актера: ')
            a_1 = set(film_of_act(a1, dct_f_act, lst_1))
            a_2 = set(film_of_act(a2, dct_f_act, lst_2))
            print(a_1 - a_2)

        print()
        v = input('Хотите повторить? (да или нет) ')
        if v == 'да':
            q += 1
        else:
            q = -1
