from random import random
from math import floor


def get_coord():
    '''принимает на ввод 2 числа координат(по осям х у), разделенные пробелом, или слово "мина" и 2 числа
    возвращает coordi & coordj соответственно, а так же mine = True, если было введено слово "мина" и False иначе'''
    a = input('Проверим в координатах: ').split()
    if len(a) == 3 and a[0] == 'мина':
        mine = True
        coordi, coordj = int(a[1])-1, int(a[2])-1
    elif len(a) == 2:
        mine = False
        coordi, coordj = int(a[0])-1, int(a[1])-1
    else:
        raise ValueError
    return mine, coordi, coordj


def rep_game():
    """получает на ввод 3 числа: n-число строк, m-число столбцов, k-число мин, разделенные пробелом, генерирует поле с минами
    и запускает функцию запроса координат для открытия ячеек поля"""
    while True:
        try:
            n, m, k = (int(i) for i in input('Размер и кол-во мин: ').split())
            break
        except:
            print('Данные введены неверно, попробуй еще раз')
    basic = [[0 for j in range(m)] for i in range(n)]
    bas = [['#' for j in range(m)] for i in range(n)]
    mines, coordi, coordj = 0, 0, 0
    for i in range(k):
        while True:
            row, col = floor(random() * n), floor(random() * m)
            if basic[row][col] == 0:
                basic[row][col] = -1
                break
    for i in range(n):
        for j in range(m):
            if basic[i][j] == 0:
                for di in range(-1,2):
                    for dj in range(-1,2):
                        ai = i + di
                        aj = j + dj
                        if 0 <= ai < n and 0 <= aj < m and basic[ai][aj] == -1:
                            basic[i][j] += 1
    win = True
    while k != 0 and win:
        while True:
            try:
                mine, coordi, coordj = get_coord()
                break
            except:
                print('ошибка ввода координат, попробуем еще раз: ')
        if mine:
            bas[coordi][coordj] = 'X'
            mines += 1
            if basic[coordi][coordj] == -1:
                k -= 1
        else:
            if basic[coordi][coordj] != -1:
                bas[coordi][coordj] = basic[coordi][coordj]
            else: 
                win = False
                print(('упс... тут была мина, вы проиграли. Сыграем еще? (да/нет)'))
                bas[coordi][coordj] = '*'
        for i in bas:
            for j in i:
                print(j, end = ' ')
            print()
    if win:
        print('Поздравляю, вы победили, все мины закрыты! ')
        print('Вам потребовалось закрыть ' + str(mines) + ' ячейки(ек), чтобы закрыть все ' + str(k) + " мин")

if __name__ == '__main__':
    go = input('Сыграем? да/нет ')
    if go == 'да':
        print('Введи число строк, столбцов и мин ')
        rep_game()
    else:
        break