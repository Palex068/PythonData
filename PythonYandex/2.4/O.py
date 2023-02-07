"""
Числовая змейка 2.0
Воспитательнице вновь нужна программа, которая будет генерировать змейку из чисел. Напишите программу, которая строит числовую змейку требуемого размера.

Формат ввода
В первой строке записано число NN — высота числового прямоугольника.
Во второй строке указано число MM — ширина числового прямоугольника.

Формат вывода
Нужно вывести сформированную числовую змейку требуемого размера.
Чтобы прямоугольник был красивым, каждый его столбец следует сделать одинаковой ширины.

Пример 1
Ввод
2
3
Вывод
1 4 5
2 3 6
Пример 2
Ввод
4
6
Вывод
 1  8  9 16 17 24
 2  7 10 15 18 23
 3  6 11 14 19 22
 4  5 12 13 20 21
"""




def Matrix(h, w):
    matrix = [[0 for x in range(w)] for y in range(h)]
    return matrix


def Print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix) * len(matrix[i]) < 10:
                print("{:1}".format(matrix[i][j]), end=" ")
            elif len(matrix) * len(matrix[i]) >= 10 and len(matrix) * len(matrix[i]) < 100:
                print("{:2}".format(matrix[i][j]), end=" ")
            else:
                print("{:3}".format(matrix[i][j]), end=" ")
        print()


h, w = int(input()), int(input())
matrix = Matrix(h, w)

count = 1
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        if j % 2:
            matrix[- 1 - i][j] = count
        else:
            matrix[i][j] = count
        count += 1

Print_matrix(matrix)
