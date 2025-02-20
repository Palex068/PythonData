"""
Числовая змейка
Увы, обыкновенные прямоугольники детям быстро наскучили. 
Теперь воспитательнице требуется новая программа. 
Напишите программу, которая строит числовую змейку требуемого размера.

Формат ввода
В первой строке записано число NN — высота числового прямоугольника.
Во второй строке указано число MM — ширина числового прямоугольника.

Формат вывода
Нужно вывести сформированную числовую змейку требуемого размера.
Чтобы прямоугольник был красивым, каждый его столбец следует 
сделать одинаковой ширины.

Пример 1
Ввод
2
3
Вывод
1 2 3
6 5 4
Пример 2
Ввод
4
6
Вывод
 1  2  3  4  5  6
12 11 10  9  8  7
13 14 15 16 17 18
24 23 22 21 20 19
"""

n, m = int(input()), int(input())

for i in range(1, n + 1):  # счетчик для строк
    if i % 2:
        for j in range(1, m + 1):
            if n * m < 10:
                print("{:1}".format(j + m * (i - 1)), end=" ")
            elif n * m >= 10 and m * n < 100:
                print("{:2}".format(j + m * (i - 1)), end=" ")
            else:
                print("{:3}".format(j + m * (i - 1)), end=" ")
    else:
        for j in range(1, m + 1):
            if n * m < 10:
                print("{:1}".format(m * (i) - j + 1), end=" ")
            elif n * m >= 10 and m * n < 100:
                print("{:2}".format(m * (i) - j + 1), end=" ")
            else:
                print("{:3}".format(m * (i) - j + 1), end=" ")
    print()
