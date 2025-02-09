"""
Каждый n-ый элемент
На вход программе подается строка текста, содержащая символы и число nn. Из данной строки формируется список. Напишите программу, которая разделяет список на вложенные подсписки так, что nn последовательных элементов принадлежат разным подспискам.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Графическая иллюстрация для 11 теста:
"""
# S = input().split()
# n = int(input())

# result = []
# for i in range(n):
#     result.append(list(S[i::n]))
# print(result)

"""
Максимальный в области 2
Напишите программу, которая выводит максимальный 
элемент в заштрихованной области квадратной матрицы.

ниже дополнительной диагонали

"""
# N = int(input())
# matrix = list(list(map(int, input().split())) for _ in range(N))
# result = []

# for i in range(N):
#     for j in range(N):
#         if i >= N - 1 - j:
#             result.append(matrix[i][j])
# print(max(result))


"""
Напишите программу, которая транспонирует квадратную матрицу.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и 
столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести транспонированную матрицу.

Примечание 1. Транспонированная матрица — матрица, полученная из 
исходной матрицы заменой строк на столбцы.

Примечание 2. Задачу можно решить без использования вспомогательного списка.
"""
# N = int(input())
# matrix = list(list(map(int, input().split())) for _ in range(N))
# result = result = [list('0' * N) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         result[j][i] = matrix[i][j]

# for row in result:
#     print(*(f'{e:<3}' for e in row), sep='')

"""
Снежинка
На вход программе подается нечетное натуральное число n. 
Напишите программу, которая создает матрицу размером n x n 
заполнив её символами . . 
Затем заполните символами * среднюю строку и столбец матрицы, 
главную и побочную диагональ матрицы. Выведите полученную матрицу на экран, 
разделяя элементы пробелами.

Формат входных данных
На вход программе подается нечетное натуральное число n, (n ≥ 3)
 — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.
"""

# N = int(input())

# result = [list('.' * N) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         if i == j or i == (N - 1 - j) or (j == N // 2) or (i == N // 2): 
#             result[j][i] = '*'

# for row in result:
#     print(*(f'{e:<2}' for e in row), sep='')

"""
Симметричная матрица
Напишите программу проверки симметричности квадратной 
матрицы относительно побочной диагонали.

Формат входных данных
На вход программе подаётся натуральное число n — количество
 строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.
"""

# def is_symmetrical(matrix):
#     N = len(matrix)
#     for i in range(N):
#         for j in range(N):
#             if matrix[i][j] != matrix[N - j - 1][N - i - 1]:
#                 return False
#     return True


# matrix = list(list(map(int, input().split())) for _ in range(int(input())))

# print("YES" if is_symmetrical(matrix) else "NO")

"""
 Латинский квадрат 🌶️
Латинским квадратом порядка n называется квадратная матрица 
размером n x n, каждая строка и каждый столбец которой содержат все числа от 1 до n. 
Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.
"""
# from itertools import chain
# N = int(input())
# matrix = list(list(map(int, input().split())) for _ in range(N))
# result = []

# for i in range(N):
#     result.append(sum(matrix[i]))
#     column_sum = 0
#     for j in range(N):
#         column_sum += matrix[j][i]
#     result.append(column_sum)

# print("YES" if (len(set(result)) == 1 and list(set(result))[0] != 0 
#                 and sorted(list(chain(*matrix))) == list(range(1, N + 1))) else "NO")

"""
Ходы ферзя
На шахматной доске 8 x 8 стоит ферзь. 
Отметьте положение ферзя на доске и все клетки, которые бьет ферзь. 
Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, 
отметьте символами *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты ферзя на шахматной доске в шахматной нотации 
(то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), 
затем номер строки (цифра от 1 до 8, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
"""

# result = [list('.' * 8) for _ in range(8)]
# inp = input()
# iN = 8 - int(inp[1])
# jN = 'a b c d e f g h'.split().index(inp[0])

# for i in range(8):
#     for j in range(8):
#         if (i == iN or j == jN
#             or (jN + iN == i + j) 
#             or  jN - iN == j - i):
#             result[i][j] = '*'
# result[iN][jN] = 'Q'
# for row in result:
#     print(*(f'{e:<2}' for e in row), sep='')

"""
Диагонали параллельные главной
На вход программе подается натуральное число n. 
Напишите программу, которая создает матрицу размером n x n и 
заполняет её по следующему правилу:

    на главной диагонали на месте каждого элемента должно стоять число 0;
    на двух диагоналях, прилегающих к главной, число 1;
    на следующих двух диагоналях число 2, и т.д.
Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.
"""

# N = int(input())
# result = [list('0' * N) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         result[i][j] = abs(i - j)
# for row in result:
#     print(*(f'{e:<2}' for e in row), sep='')
