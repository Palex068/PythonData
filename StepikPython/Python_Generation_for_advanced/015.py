# def fancy(length, char1, char2):
#     return (char1 + char2) * length + char1


# print(fancy(5, '-', '*'))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(3))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(3, '.'))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(2, ':', '|'))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(4, char2='#'))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1


# print(fancy(char2='$', length=3))

"""
Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера. 
При этом (в зависимости от переданных аргументов) она должна вести себя так:

matrix() — возвращает матрицу 1 x 1, в которой единственное число равно нулю;
matrix(n) — возвращает матрицу n x n, заполненную нулями;
matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями;
matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой каждый элемент равен числу value.
При создании функции пользуйтесь аргументами по умолчанию.

Примечание 1. Приведенный ниже код:

    print(matrix())                   # матрица 1 x 1 из 0
    print(matrix(3))                  # матрица 3 x 3 из 0
    print(matrix(2, 5))               # матрица 2 x 5 из 0
    print(matrix(3, 4, 9))            # матрица 3 x 4 из 9

должен выводить:

    [[0]]
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]

    Примечание 2. Вызывать функцию matrix() не нужно, требуется только реализовать ее.
"""
# def matrix(rows = 1, columns = None, volume = 0):
#     if columns == None:
#         columns = rows
#     result = [[volume for _ in range(columns)] for _ in range(rows)]
#     return result


# print(matrix())                   # матрица 1 x 1 из 0
# print(matrix(3))                  # матрица 3 x 3 из 0
# print(matrix(2, 5))               # матрица 2 x 5 из 0
# print(matrix(3, 4, 9))            # матрица 3 x 4 из 9

"""
Напишите функцию count_args(), которая принимает произвольное количество 
аргументов и возвращает количество переданных в нее аргументов.

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.

Примечание 2. Следующий программный код:

print(count_args())
print(count_args(10))
print(count_args('stepik', 'beegeek'))
print(count_args([], (''), 'a', 12, False))
должен выводить:

0
1
2
5
Примечание 3. Вызывать функцию count_args() не нужно, требуется только реализовать.
"""

# def count_args(*args):
#     return len(args)

# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))

"""
Напишите функцию sq_sum(), которая принимает произвольное количество 
числовых аргументов и возвращает сумму их квадратов.

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.

Примечание 2. Следующий программный код:

print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
должен выводить:

0
4
8.5
14
385
Примечание 3. Вызывать функцию sq_sum() не нужно, требуется только реализовать.
"""
# def sq_sum(*args):
#     return sum(list(n ** 2 for n in args))
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

"""
Напишите функцию mean(), которая принимает произвольное количество аргументов и 
возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов.

Примечание 1. Обратите внимание, что функция должна принимать не список, 
а именно произвольное количество аргументов.

Примечание 2. Функция должна игнорировать аргументы всех типов, кроме int или float.

Примечание 3. Следующий программный код:

print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
должен выводить:

0.0
7.0
2.0
0.0
3.5
5.5
Примечание 4. Для проверки типа можно использовать встроенную функцию type().

Примечание 5. Вызывать функцию mean() не нужно, требуется только реализовать.
# """
# def mean(*args):
#     result = list(n for n in args if type(n) in (int, float))
#     if result == []:
#         return 0.0
#     return sum(result) / len(result)

# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

"""
Напишите функцию greet(), которая принимает произвольное количество 
аргументов строк имен (как минимум одно) и возвращает приветствие в 
соответствии с образцом.

Примечание 1. Обратите внимание, что функция должна принимать не список, 
а именно произвольное количество аргументов.

Примечание 2. Следующий программный код:

print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
должен выводить:

Hello, Timur!
Hello, Timur and Roman!
Hello, Timur and Roman and Ruslan!
Примечание 3. Функция greet() должна принимать как минимум один обязательный аргумент!

Примечание 4. Вызывать функцию greet() не нужно, требуется только реализовать.
"""
# def greet(name, *args):
#     return "Hello, " + " and ".join(list([name] + list(args))) + "!"


# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))

"""
Напишите функцию print_products(), которая принимает произвольное количество 
аргументов и выводит список продуктов (любая непустая строка) 
по образцу: 
<номер продукта>) 
<название продукта> (нумерация продуктов начинается с единицы). 
Если среди переданных аргументов нет ни одного продукта, 
необходимо вывести текст Нет продуктов.

Примечание 1. Обратите внимание, что функция должна принимать не список, 
а именно произвольное количество аргументов.

Примечание 2. Числа, списки, кортежи, словари, множества и 
другие нестроковые объекты продуктами не являются и их нужно игнорировать.

Примечание 3. Следующий программный код:

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
должен выводить:

1) Бананы
2) Яблоки
3) Макароны
Следующий программный код:

print_products([4], {}, 1, 2, {'Beegeek'}, '') 
должен выводить:

Нет продуктов
Примечание 4. Обратите внимание: функция print_products() должна выводить (печатать) нужное значение, а не возвращать его.

Примечание 5. Вызывать функцию print_products() не нужно, требуется только реализовать
"""


# def print_products(*args):
#     result = list(s for s in args if type(s) is str and s != '')
#     if result == []:
#         print("Нет продуктов")
#     else:
#         for n in range(len(result)):
#             print(f"{n + 1}) {result[n]}")

# def print_products(*args):
#     cnt = 0
#     for e in args:
#         if type(e) == str and e:
#             cnt += 1
#             print(f'{cnt}) {e}')
#     if cnt == 0:
#         print('Нет продуктов')

# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '')

"""
Напишите функцию info_kwargs(), которая принимает произвольное количество 
именованных аргументов и печатает именованные аргументы в соответствии 
с образцом: 
<имя аргумента>: <значение аргумента>, 
при этом имена аргументов следуют в алфавитном порядке (по возрастанию).

Примечание 1. Обратите внимание, что функция должна принимать не список, 
а именно произвольное количество именованных аргументов.

Примечание 2. Следующий программный код:

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 
должен выводить:

age: 28
first_name: Timur
job: teacher
last_name: Guev
Примечание 3. Вызывать функцию info_kwargs() не нужно, требуется только реализовать.
"""

# def info_kwargs(**kwargs):
#     result = sorted(kwargs)
#     for s in result:
#         print(f"{s}: {kwargs[s]}")

# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

# s1 = 'python'
# s2 = 'stepicon'
# s3 = 'beegeek'
 
# print(min(s1, s2, s3))
# print(max(s1, s2, s3))

# s1 = 'python'
# s2 = 'stepicon'
# s3 = 'beegeek'
 
# print(min(s1, s2, s3, key=len))
# print(max(s1, s2, s3, key=len))

# def f(x):
#     return x**2


# g = f
# print(f(3), g(5))

# def f(x):
#     return x**2


# def g(x):
#     return x**3


# funcs = [f, g]
# print(funcs[0](5), funcs[1](5))

# def comparator(pair):
#     return pair[1]


# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator)
# print(pairs)

# def comparator(pair):
#     return pair[0] + pair[1]


# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator, reverse=True)
# print(pairs)

# words = ['this', 'is', 'a', 'test', 'of', 'sorting']
# words.sort(key=len)
# print(words)

# def f1(x):
#     return 2*x+1


# def f2(x):
#     return x**2


# def f3(x):
#     return -x**2+1


# def f4(x):
#     return x-3


# funcs = [f1, f2, f3, f4]
# i = int(input())
# print(funcs[i](2))

"""
Дан список numbers, содержащий кортежи чисел. 
Напишите программу, которая с помощью встроенных функций 
min() и max() выводит те кортежи (каждый на отдельной строке), 
которые имеют минимальное и максимальное среднее арифметическое значение элементов.

Примечание. Используйте необязательный аргумент key.
"""


# def comparator(pair):
#     return sum(pair) / len(pair)


# numbers = [(10, 10, 10), (30, 45, 56), (81, 39),
#            (1, 2, 3), (12,), (-2, -4, 100),
#            (1, 2, 99), (89, 9, 34), (10, 20, 30, -2),
#            (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5),
#            (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

# numbers.sort(key=comparator)
# print(numbers[0])
# print(numbers[-1])

# from statistics import mean
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

# print(*(func(numbers, key=mean) for func in (min, max)), sep='\n')


"""
Напишите программу, которая сортирует список points координат точек плоскости 
в соответствии с расстоянием от начала координат (точки (0;0)). 
Программа должна вывести отсортированный список.

Примечание. Расстояние от начала координат O(0;0) до точки A(x;y) равно OA = sqrt{x^2+y^2}.
"""

# def length(pair):
#     return (pair[0] ** 2 + pair[1] ** 2) ** 0.5


# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

# print(sorted(points, key=length))

# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

# def comp_vector(point):
#     return abs(complex(point[0], point[1]))
# points.sort(key=comp_vector)

# print(points)

"""
Дан список numbers, содержащий кортежи чисел. Напишите программу, 
которая сортирует и выводит список numbers в соответствии с суммой минимального и максимального элемента кортежа.

Примечание 1. 
В этой задаче мы считаем, что кортеж (2, 1, 3) меньше кортежа (6, 4, 5), 
так как 1+3 < 4+6. При этом кортеж (1, 2, 9) равен кортежу (4, 5, 6), так как 1+9 = 4+6.

Примечание 2. Используйте необязательный аргумент key.
"""

# def comparator(pair):
#     return max(pair) + min(pair)


# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]

# print(sorted(numbers, key=comparator))

"""
Сортируй как хочешь
Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).

Напишите программу сортировки списка спортсменов по указанному полю:

1: по имени;
2: по возрасту;
3: по росту;
4: по весу.
Формат входных данных
На вход программе подается натуральное число от 1 до 4 – номер поля по которому требуется отсортировать список.

Формат выходных данных
Программа должна вывести отсортированный по заданному полю список в соответствии с примерами.

Примечание. Решите задачу без использования условного оператора.
"""


# def comparator(pair):
#     return pair[num - 1]


# athletes = [('Дима', 10, 130, 35),
#             ('Тимур', 11, 135, 39),
#             ('Руслан', 9, 140, 33),
#             ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70),
#             ('Рома', 16, 188, 100),
#             ('Матвей', 17, 168, 68),
#             ('Петя', 15, 190, 90)]
# num = int(input())
# for s in sorted(athletes, key=comparator):
#     print(*s)

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

# def gen_comparator(field=1):
#     def comp(seq):
#         return seq[field - 1]
#     return comp

# cmp = gen_comparator(int(input()))
# athletes.sort(key=cmp)
# for a in athletes:
#     print(*a)

"""
Математические функции
Напишите программу, которая принимает число и название функции, 
а выводит результат применения функции к данному числу.

Список возможных функций:

квадрат: функция принимает число и возвращает его квадрат;
куб: функция принимает число и возвращает его куб;
корень: функция принимает число и возвращает корень квадратный из этого числа;
модуль: функция принимает число и возвращает его модуль;
синус: функция принимает число (в радианах) и возвращает синус этого числа.
Формат входных данных

На вход программе подается целое число и название функции, записанные на отдельных строках.

Формат выходных данных
Программа должна выдать результат применения функции к числу.

Примечание. Решите задачу без использования условного оператора.
"""
# from math import sin

# F = {'квадрат': lambda x: x ** 2,
#      'куб': lambda x: x ** 3,
#      'корень': lambda x: x ** 0.5,
#      'модуль': lambda x: abs(x),
#      'синус': lambda x: sin(x)}
# n = int(input())
# print(F[input()](n))

# from math import sin

# def math_func(n, f):
#     return {'квадрат': n**2, 'куб': n**3, 'корень': n**0.5, 'модуль': abs(n), 'синус': sin(n)}[f]

# print(math_func(int(input()), input()))  # число, команда

"""
Интересная сортировка-1
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.

Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. 
При этом, если два числа имеют одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы одним пробелом.

Подсказка
Сортировка при помощи функции sorted() и списочного метода sort() является стабильной, то есть она гарантирует неизменность расположения равных между собой элементов.
"""

# def comparator(num):
#     return sum(map(int, list(num)))

# print(*sorted(input().split(), key=comparator))

# print(*sorted(input().split(), key=lambda x: sum(map(int, x))))

"""
Интересная сортировка-2
На вход программе подается строка натуральных чисел. 
Из элементов строки формируется список чисел.

Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. 
При этом, если у двух чисел одинаковая сумма цифр, их следует вывести в порядке неубывания.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести отсортированный список чисел в соответствии с условием задачи, 
разделяя его элементы одним пробелом.

Подсказка
Вспомните каким образом сортируются кортежи.
"""

# print(*sorted(sorted(map(int, input().split())), key=lambda x: sum(map(int, str(x)))))

# print(*sorted(sorted(input().split(), key=int), key=lambda x: sum(map(int, x))))

# def high_order_function(func):
#     return func(10)


# def square(x):
#     return x**2


# def minus_one(x):
#     return x - 1


# num1 = high_order_function(square)
# num2 = high_order_function(minus_one)

# print(num1*num2)


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'deified', 'bbbbb', 'mother', 'surface', 'sister']

# words_len = map(len, words)
# print(max(words_len))


# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result


# def predicate(word):
#     return word == word[::-1]


# words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
# filtered = filter(predicate, words)
# print(len(filtered))


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]

# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))

# print(var1 + var2)


"""
Напишите программу, которая с помощью функции map() 
округляет все элементы списка numbers до 2 десятичных знаков, 
а затем выводит их, каждый на отдельной строке.
"""

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# numbers = [3.56773, 5.57668, 4.00914, 56.24241,
#            9.01344, 32.12013, 23.22222, 90.09873,
#            45.45, 314.1528, 2.71828, 1.41546]
# print(*map(lambda x: round(x, 2), numbers), sep='\n')

"""
Напишите программу, которая с помощью функций filter() и map() отбирает 
из заданного списка numbers трёхзначные числа, дающие при делении на 5 
остаток 2, и выводит их кубы, каждый в отдельной строке.

Примечание. Остаток 2 при делении на 5 должно давать само число, а не его куб.
"""


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result


# numbers = [1014, 1321, 675, 1215, 56, 1386,
#            1385, 431, 1058, 486, 1434, 696,
#            1016, 1084, 424, 1189, 475, 95,
#            1434, 1462, 815, 776, 657, 1225,
#            912, 537, 1478, 1176, 544, 488,
#            668, 944, 207, 266, 1309, 1027,
#            257, 1374, 1289, 1155, 230, 866,
#            708, 144, 1434, 1163, 345, 394,
#            560, 338, 232, 182, 1438, 1127,
#            928, 1309, 98, 530, 1013, 898,
#            669, 105, 130, 1363, 947, 72,
#            1278, 166, 904, 349, 831, 1207,
#            1496, 370, 725, 926, 175, 959,
#            1282, 336, 1268, 351, 1439, 186,
#            273, 1008, 231, 138, 142, 433,
#            456, 1268, 1018, 1274, 387,
#            120, 340, 963, 832, 1127]


# print(*map(lambda x: x ** 3, filter(lambda x: x % 5 == 2 and len(str(x)) == 3, numbers)), sep='\n')


"""
Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers.

Примечание. Попробуйте решить задачу двумя способами: с помощью функции reduce(), 
и с помощью функций map() и sum().
"""

# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc


# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1,
#            11, -2, 75, 5, 51, 34, 28, 46, 1,
#            -8, 84, 16, 51, 90, 56, 65, 90, 23,
#            35, 11, -10, 70, 90, 90, 12, 96, 58,
#            -8, -4, 91, 76, 94, 60, 72, 43, 4,
#            -6, -5, 51, 58, 60, 30, 38, 67, 62,
#            36, 72, 34, 82, 62, -1, 60, 82, 87,
#            81, -7, 57, 26, 36, 17, 43, 80, 40,
#            75, 94, 91, 64, 38, 72, 29, 84, 38,
#            35, 7, 54, 31, 95, 78, 27, 82, 1, 64,
#            94, 31, 29, -8, 98, 24, 61, 7, 73]

# print((sum(map(lambda x: x ** 2, numbers))))

"""
Напишите программу для вычисления и вывода суммы квадратов двузначных чисел,
которые делятся на 7 без остатка.

Примечание 1. При решении задачи используйте функции filter(), map() и sum().

Примечание 2. На 7 должно делиться исходное двузначное число, а не его квадрат.

Примечание 3. Не забывайте про отрицательные двузначные числа.
"""

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result


# numbers = [77, 293, 28, 242, 213, 285, 71, 286,
#            144, 276, 61, 298, 280, 214, 156, 227,
#            228, 51, -4, 202, 58, 99, 270, 219, 94,
#            253, 53, 235, 9, 158, 49, 183, 166, 205,
#            183, 266, 180, 6, 279, 200, 208, 231,
#            178, 201, 260, -35, 152, 115, 79, 284,
#            181, 92, 286, 98, 271, 259, 258, 196,
#            -8, 43, 2, 128, 143, 43, 297, 229, 60,
#            254, -9, 5, 187, 220, -8, 111, 285, 5,
#            263, 187, 192, -9, 268, -9, 23, 71, 135,
#            7, -161, 65, 135, 29, 148, 242, 33, 35,
#            211, 5, 161, 46, 159, 23, 169, 23, 172,
#            184, -7, 228, 129, 274, 73, 197, 272, 54,
#            278, 26, 280, 13, 171, 2, 79, -2, 183,
#            10, 236, 276, 4, 29, -10, 41, 269, 94,
#            279, 129, 39, 92, -63, 263, 219, 57, 18,
#            236, 291, 234, 10, 250, 0, 64, 172, 216,
#            30, 15, 229, 205, 123, -105]

# print(sum(map(lambda x: x **2, filter(lambda x: x % 7 == 0 and len(str(abs(x))) == 2, numbers))))

"""
Напишите функцию func_apply(), принимающую на вход функцию и список значений и 
возвращающую список, в котором каждое значение будет результатом применения 
переданной функции к переданному списку.

Примечание 1. Приведенный ниже код, при условии, что функция func_apply() написана правильно
"""

# def add3(x):
#     return x + 3


# def mul7(x):
#     return x * 7


# def func_apply(F, array):
#     return list(map(F, array))

# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))

# iterable = [1, 2, 3]
# result = list(map(len, iterable))
# print(result)

# def filter_vowels(letter):
#     return letter in 'aeiou'


# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# filtered_vowels = filter(filter_vowels, letters)

# print(*filtered_vowels)

# random_list = [1, 'a', 0, False, True, '0', 7, '']
# filtered_list = list(filter(None, random_list))
# print(filtered_list)

# listA = [2, 3, 4]
# listB = [3, 2, 1]

# result = sum(map(pow, listA, listB))
# print(result)

# from operator import mul
# from functools import reduce

# result = reduce(mul, range(1, 6))
# print(result)

# from operator import add

# result = list(map(add, 'abc', '1234'))
# print(result)

# from operator import mul

# result = list(map(mul, ['a', 'b', 'c'], [1, 2, 3]))
# print(result)

# from operator import add
# from functools import reduce

# result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(result)

# from functools import reduce

# numbers = range(10)
# obj = list(map(lambda x: x + 1, numbers))
# print(*obj)
# obj = list(filter(lambda x: x % 2 == 1, obj))
# print(*obj)
# result = reduce(lambda x, y: x + y, obj, 0)

# print(result)

# result = list(map(lambda x: x.split(), ['a', 'a b', 'a b c']))

# print(result)

# high_ord_func = lambda x, func: x + func(x)

# result = high_ord_func(2, lambda x: x * x) + high_ord_func(5, lambda x: x + 3)

# print(result)

# dict1 = {'x': 1}
# dict2 = {'y': 2}
# dict3 = {'x': 3, 'y': 4}

# result = list(filter(lambda d: 'x' in d.keys(), [dict1, dict2, dict3]))

# print(result)

"""
Требовалось написать программу, которая:

преобразует список floats в список чисел, возведенных 
в квадрат и округленных с точностью до одного десятичного знака;

фильтрует список words  и оставляет только палиндромы длиной более 4 символов;

находит произведение чисел из списка numbers.

Программист торопился и написал программу неправильно. Доработайте его программу.
"""

# from functools import reduce 
# from operator import mul

# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]

# # Исправьте этот код
# map_result = list(map(lambda num: round(num ** 2, 1), floats))
# filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
# reduce_result = reduce(mul, numbers)

# print(map_result)
# print(filter_result)
# print(reduce_result)

"""
Напишите программу, которая с помощью встроенных функций 
filter(), map(), sorted() и reduce() выводит в алфавитном 
порядке список primary городов с населением более 10_000_000 человек, 
в формате:

Cities: Beijing, Buenos Aires, ...

Примечание 1. Тестирующая система никак не "покарает" вас за 
неиспользование встроенных функций filter(), map(), sorted() 
и reduce(), однако лучше сделать это задание честно 😃.

Примечание 2. Ставить запятую в конце вывода не нужно.
"""

# from functools import reduce

# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]

# print('Cities: ' + ', '.join(sorted(map(lambda x: x[0], filter(lambda x: x[2] == 'primary' and x[1] > 10000000, data)))))

# numbers = [1, 2, 5, 3, 4]
# numbers.sort(key=lambda x: -x)
# print(numbers)

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda: True, primes))
# print(result)

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda x: True, primes))
# print(result)

"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает 
целочисленный аргумент и возвращает значение True, если он делится без остатка 
на 19 или на 13 и False в противном случае.

Примечание 1. Следующий программный код:

print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))

должен выводить:

True
True
False
False
True
"""

# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False

# print(func(19))
# print(func(13))
# print(func(20))
# print(func(15))
# print(func(247))

"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен) и False в противном случае.

Примечание 1. Следующий программный код:

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))
должен выводить:

False
False
True
False
False
True
Примечание 2. Вызывать анонимную функцию не нужно.
"""

# func = lambda x: x[0].lower() == 'a' and x[-1].lower() == 'a'

# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))

"""
Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, 
которая принимает строковый аргумент и возвращает значение True, если переданный 
аргумент является неотрицательным числом (целым или вещественным) и False в противном случае.

Примечание 1. Следующий программный код:

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))
должен выводить:

False
True
False
False
True
False
False
True
Примечание 2. Неотрицательные числа — это положительные числа и число нуль.

Примечание 3. Вызывать анонимную функцию не нужно.
"""
# is_non_negative_num = lambda x: True if (x[0] != '-' and x.count('.') < 2 and x.replace('.', '').isdigit()) else False

# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))

"""
Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает 
строковый аргумент и возвращает значение True, если переданный аргумент является 
числом (целым или вещественным) и False в противном случае.

Примечание 1. Следующий программный код:

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
должен выводить:

False
True
True
True
True
False
False
True
False
Примечание 2. Используйте вспомогательную функцию из прошлого степа.

Примечание 3. Вызывать анонимную функцию не нужно.
"""

# def is_num(num): 
#     try:
#         number = float(num)
#         return True
#     except ValueError:
#         return False

# is_num = lambda x: x.strip('-').replace('.', '', 1).isdigit()

# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))

"""
Напишите программу, которая с помощью встроенных функций filter() и sorted() 
выводит слова из списка words, имеющие длину ровно 66 символов. Слова следует 
вывести в алфавитном порядке на одной строке, разделив символом пробела.

Примечание. Используйте анонимную функцию в качестве критерия фильтрации.
"""

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish',
#          'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray',
#          'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides',
#          'access', 'friday', 'bestow', 'abound', 'absent', 'beware',
#          'abundant', 'abnormal', 'aboard', 'about', 'accelerate',
#          'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond',
#          'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept',
#          'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
# print(*sorted(filter(lambda x: len(x) == 6, words)))

"""
Напишите программу, которая с помощью встроенных функций map() и filter() 
удаляет из списка numbers все нечетные элементы, большие 47, а все четные 
элементы нацело делит на два (целочисленное деление – //). Полученные числа 
следует вывести на одной строке, разделив символом пробела и сохранив исходный порядок.

Примечание. Используйте анонимную функцию в качестве критерия фильтрации.
"""

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37,
#            80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66,
#            83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40,
#            93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41,
#            59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48,
#            17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26,
#            6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94,
#            37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89,
#            8, 36, 94, 46, 33]

# print(*map(lambda x: x if x % 2 else x // 2, filter(lambda x: not (x % 2 == 1 and x > 47), numbers)))

"""
Список data содержит информацию о численности населения некоторых штатов США. 
Напишите программу сортировки по убыванию списка data на основании последнего 
символа в названии штата. Затем распечатайте элементы этого списка, каждый на новой строке в формате:

<название штата>: <численность населения>

Vermont: 626299
Massachusetts: 7029917
...
Примечание 1. Сортировка производится в лексикографическом порядке (по алфавиту) 
по убыванию на основании последнего символа в названии штата. При этом, если два 
штата имеют одинаковый последний символ, следует сохранить их взаиморасположение 
в начальном списке.

Примечание 2. Используйте анонимную функцию в качестве критерия сортировки.
"""

# data = [(19542209, 'New York'), (4887871, 'Alabama'),
#         (1420491, 'Hawaii'), (626299, 'Vermont'),
#         (1805832, 'West Virginia'), (39865590, 'California'),
#         (11799448, 'Ohio'), (10711908, 'Georgia'),
#         (10077331, 'Michigan'), (10439388, 'Virginia'),
#         (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

# for s in sorted(data, key=lambda x: x[1][-1], reverse=True):
#     print(f"{s[1]}: {s[0]}")

"""
Список data содержит слова на русском языке. Напишите программу его сортировки 
по возрастанию длины слов, а затем в лексикографическом порядке. Отсортированные 
слова следует вывести на одной строке, разделив символом пробела.

Примечание 1. Используйте анонимную функцию в качестве критерия сортировки.

Примечание 2. Если длина слов совпадает, сортировать нужно в лексикографическом порядке.
"""

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день',
#         'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
#         'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна',
#         'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец',
#         'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

# print(*sorted(sorted(data), key=lambda x: len(x)))

# print(*sorted(sorted(data), key=len))

"""
Список mixed_list содержит целочисленные и строковые значения. 
Напишите программу, которая с помощью встроенной функции max() 
находит и выводит наибольшее числовое значение в указанном списке.

Примечание 1. Для решения задачи используйте анонимную функцию и необязательный аргумент key  функции max().

Примечание 2. Обратите внимание, что сравнивать числа и строки нельзя.
"""

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday',
#               'abate', 'accessory', 'absorb', 1384878, 'sunday',
#               'about', 454805, 'saturday', 'abort', 2121919,
#               2552839, 977970, 1772933, 1564063, 'abduct',
#               901271, 2680434, 'bicycle', 'accelerate', 1109147,
#               942908, 'berry', 433507, 'bias', 'bestow', 1875665,
#               'besides', 'bewilder', 1586517, 375290, 1503450,
#               2713047, 'abnormal', 2286106, 242192, 701049, 2866491,
#               'benevolent', 'bigot', 'abuse', 'abrupt', 343772,
#                'able', 2135748, 690280, 686008, 'beyond', 2415643,
#                'aboard', 'bet', 859105, 'accident', 2223166, 894187,
#                146564, 1251748, 2851543, 1619426, 2263113, 1618068,
#                'berth', 'abolish', 'beware', 2618492, 1555062,
#                'access', 'absent', 'abundant', 2950603, 'betray',
#                'beverage', 'abide', 'abandon', 2284251, 'wednesday',
#                2709698, 'thursday', 810387, 'friday', 2576799,
#                2213552, 1599022, 'accept', 'abuse', 'abound',
#                1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]


# print(max(filter(lambda x: str(x).isdigit(), mixed_list), key=int))

"""
Список mixed_list содержит целочисленные и строковые значения. 
Напишите программу его сортировки по неубыванию значений элементов, 
при этом числа должны следовать до строк.  Элементы отсортированного 
списка выведите на одной строке, разделив символом пробела.

Примечание 1. Для решения задачи используйте анонимную функцию и необязательный аргумент key  функции sorted().

Примечание 2. Если бы список mixed_list содержал значения:

mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
то результатом работы программы должно быть:

0 1 3 5 8 a aab ab ac c
"""

# mixed_list = ['beside', 48, 'accelerate', 28, 'beware',
#               'absorb', 'besides', 'berry', 15, 65,
#               'abate', 'thursday', 76, 70, 94, 35, 36,
#               'berth', 41, 'abnormal', 'bicycle', 'bid',
#               'sunday', 'saturday', 87, 'bigot', 41,
#               'abort', 13, 60, 'friday', 26, 13, 'accident',
#               'access', 40, 26, 20, 75, 13, 40, 67, 12,
#               'abuse', 78, 10, 80, 'accessory', 20,
#               'bewilder', 'benevolent', 'bet', 64, 38,
#               65, 51, 95, 'abduct', 37, 98, 99, 14,
#               'abandon', 'accept', 46, 'abide', 'beyond',
#               19, 'about', 76, 26, 'abound', 12, 95,
#               'wednesday', 'abundant', 'abrupt', 'aboard',
#               50, 89, 'tuesday', 66, 'bestow', 'absent',
#               76, 46, 'betray', 47, 'able', 11]

# digits = sorted(filter(lambda x: str(x).isdigit(), mixed_list))
# words = sorted(filter(lambda x: not str(x).isdigit(), mixed_list))
# print(*(digits + words))

"""
Противоположный цвет
В цветовой схеме RGB цвета задаются с помощью трех компонентов:

R — интенсивность красной составляющей цвета;
G — интенсивность зеленой составляющей цвета;
B — интенсивность синей составляющей цвета.
Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B). 
Считается, что такие цвета хорошо гармонируют друг с другом.

Напишите программу, которая по трем компонентам заданного цвета, находит компоненты противоположного цвета. 

Формат входных данных
На вход программе подается строка, содержащая три целых неотрицательных числа, 
компоненты R, G и B начального цвета,  разделенные символом пробела.

Формат выходных данных
Программа должна вывести три компонента R, G и B противоположного цвета, разделенные символом пробела.

Примечание. Попробуйте решить задачу в одну строку с помощью встроенной функции map()
"""

# print(*map(lambda x: 255 - int(x), input().split()))

"""
Значение многочлена 🌶️
Многочленом степени n называется выражение вида 
a_n * x ** n + a_{n-1} * x ** {n-1} + ... + a_2 * x ** 2 + a_1 * x + a_0, где a_n, a_{n-1}, ... , a_2, a_1,
a_0a — коэффициенты многочлена (a_n != 0).

На вход программе на первой строке подаются коэффициенты многочлена, 
разделенные символом пробела и целое число x на второй строке. 
Напишите программу, которая вычисляет значение указанного многочлена при заданном значении x.

Формат входных данных
На вход программе на первой строке подаются коэффициенты многочлена (целые числа), 
разделенные символом пробела и целое число xx на второй строке.

Формат выходных данных
Программа должна вывести одно число — значение указанного многочлена при заданном значении x.

Примечание 1. Первый тест задает многочлен 2 * x ** 2 + 4 * x + 3, 
второй тест задает многочлен x ** 6 + 2 * x ** 5 + 3 * x ** 4 + 4 * x ** 3 + 5 * x ** 2 + 6 * x + 7.

Примечание 2. Решение задачи необходимо оформить в виде функции evaluate(coefficients, x), 
которая принимает список коэффициентов и значение аргумента. 
Функция evaluate() должна быть реализована на основе встроенных функций map() и reduce().

Примечание 3. Не забудьте вызвать функцию evaluate(), чтобы вывести результат 😀.
"""
        


# def evaluate(coefficients, x):
#     result = 0
#     for i in range(len(coefficients)):
#         result += coefficients[-1 - i] * x ** i
#     return result


# coefficients = list(map(int, input().split()))
# x = int(input())

# print(evaluate(coefficients, x))

# print(all([True, False]), all([False, False]), all([True, True]), all([10, 100, 1000]), all([10, 100, 0, 1000]), all(['Python', 'C#']), all(['school', '', 'language']), all([(1, 2, 3), []]), all([]), all([[], []]), all({0: 'Monday', 1: 'Tuesday', 2: 'Wednesday'}), all({'name': 'Timur', 'age': 28}), all({'': 'None', 'age': 28}))

# print(any([True, False]))
# print(any([False, False]))
# print(any([True, True]))
# print(any([10, 100, 1000]))
# print(any([0, 0, 0, 0]))
# print(any(['Python', 'C#']))
# print(any(['', '', 'language']))
# print(any([(1, 2, 3), []]))
# print(any([]))
# print(any([[], []]))
# print(any({0: 'Monday', 1: 'Tuesday', 2: 'Wednesday'}))
# print(any({0: 'Monday'}))
# print(any({'name': 'Timur', 'age': 28}))
# print(any({'': 'None', 'age': 28}))


# numbers = [1, 2, 3, 4, 5, 6]

# for index, elem in enumerate(numbers):
#     if elem % 2 == 0:
#         numbers[index] *= 2

# print(numbers)

# numbers = [10, 30, 20, 50, 40, 60, 70, 80]

# total = 0
# for index, number in enumerate(numbers, 1):
#     if index % 2 == 0:
#         print(number)
#         total += number
# print(total)

# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]

# result = 0
# for x, y in zip(list1, list2):
#     result += x*y
# print(result)

# words1 = ['яблоко', 'ананас', 'апельсин', 'хурма', 'гранат', 'мандарин', 'айва']
# words2 = ['林檎', 'パイナップル', 'オレンジ', '柿']
# words3 = ['apple', 'pineapple', 'orange', 'persimmon', 'pomegranate']

# print(len(list(zip(words1, words2, words3))))

"""
Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,

и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False
Перепишите функцию ignore_command(), чтобы она использовала встроенные функции all()/any() сохранив при этом ее функционал.

Примечание 1. Следующий программный код:

print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))
должен выводить:

True
True
True
False
Примечание 2. Вызывать функцию ignore_command() не нужно, требуется только реализовать.
"""

# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql',
#               'select', 'update', 'exec', 'del', 'truncate']

#     return all(command.split() in ignore)

# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql',
#               'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x: x in command, ignore))

# print(ignore_command('get ip'))
# print(ignore_command('select all'))
# print(ignore_command('delete'))
# print(ignore_command('trancate'))

"""
Используя параллельную итерацию сразу по трем спискам countries, 
capitals и population выведите информацию о стране в формате:

<capital> is the capital of <country>, population equal <population> people.


Moscow is the capital of Russia, population equal 145934462 people.
Washington is the capital of USA, population equal 331002651 people.
...
Для каждой страны информацию выводить на отдельной строке. 
"""

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

# for a, b, c in zip(capitals, countries, population):
#     print(f"{a} is the capital of {b}, population equal {c} people.")

"""
Внутри шара
На вход программе подаются три строки текста с вещественными числами, 
значениями абсцисс (x), ординат (y) и аппликат (z) точек трехмерного пространства. 
Напишите программу для проверки расположения всех точек с введенными координатами 
внутри либо на поверхности шара с центром в начале координат и радиусом R = 2.

Формат входных данных
На вход программе подаются три строки текста с вещественными числами, 
разделенными символом пробела – абсциссы, ординаты и аппликаты точек 
в трехмерной системе координат.

Формат выходных данных
Программа должна вывести True если все точки с введенными 
координатами находятся внутри или на границе шара и False, если вне.

Примечание 1. Гарантируется, что количество чисел во всех трех строках одинаковое.

Примечание 2. Уравнение поверхности шара (сферы) имеет вид x ** 2 + y ** 2 + z ** 2 = R ** 2.

Примечание 3. Для решения задачи используйте встроенные функции all() и zip().

Примечание 4. Используйте следующие названия abscissas, ordinates, applicates для соответствующих списков.

Примечание 5. Указанный шар имеет вид:
"""

# abscissas = list(map(float, input().split()))
# ordinates = list(map(float, input().split()))
# applicates = list(map(float, input().split()))
# R = 2
# data = list(zip(abscissas, ordinates, applicates))

# print(all(map(lambda x: (x[0] ** 2 + x[1] ** 2 + x[2] ** 2) <= R ** 2, data)))

"""
Корректный IP-адрес
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, 
работающей по протоколу TCP/IP.

В 4-й версии IP-адрес представляет собой 32-битное число. 
Адрес записывается в виде четырёх десятичных чисел (октетов) 
со значением от 0 до 255 (включительно), разделённых точками, например, 192.168.1.2

Напишите программу с использованием встроенной функции all() 
для проверки корректности IP-адреса: все ли октеты в IP-адресе – 
числа со значением от 0 до 255.

Формат входных данных
На вход программе подается строка в формате x.x.x.x, 
где x – непустой набор символов 0-9, a-z.

Формат выходных данных
Программа должна вывести True если введенная строка – корректный IP-адрес и False в противном случае.

Примечание. Ведущие нули следует игнорировать:

0001 = 1
006 = 6
0213 = 213
0000 = 0
00345 = 345
...
"""


# print(all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, input().split('.'))))

"""
Интересные числа
На вход программе подаются два натуральных числа a и b. 
Напишите программу с использованием встроенной функции all() 
для обнаружения всех целых чисел в диапазоне [a; b], 
которые делятся на каждую содержащуюся в них цифру без остатка.

Формат входных данных
На вход программе подаются два натуральных числа a и b на отдельных строках.

Формат выходных данных
Программа должна вывести все числа из диапазона [a; b], удовлетворяющие условию задачи, 
на одной строке, разделяя их символом пробела.

Примечание. Числа, содержащие нули, неинтересны, их выводить не нужно.
"""
# N = list(range(int(input()), int(input()) + 1))

# for n in N:
#     res = []
#     for d in str(n):
#         if d == '0':
#             res.append(0)
#         else:
#             res.append(n % int(d) == 0)
#     if all(res):
#         print(n, end=" ")

# def check(num):
#     return all(map(lambda x: int(x) and num % int(x) == 0, str(num)))

# a, b = int(input()), int(input())
# seq = range(a, b + 1)
# print(*filter(check, seq))

"""
Хороший пароль
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, 
содержит хотя бы одну цифру, заглавную и строчную букву. 
Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.
"""

# from string import digits as d, ascii_lowercase as low, ascii_uppercase as up
# result = [0, 0, 0]
# password = list(input())

# for s in password:
#     if s in d:
#         result[0] += 1
#     elif s in low:
#         result[1] += 1
#     elif s in up:
#         result[2] += 1

# print("YES" if all(result) and len(password) >=7 else "NO")

# s = input()
# print('YES' if all((any(i.isupper() for i in s), 
#                     any(i.islower() for i in s), 
#                     any(i.isdigit() for i in s), 
#                     len(s) >= 7)) else 'NO')


# print('YES' if (len(s := input()) >= 7 and
#                 any(i.isupper() for i in s) and 
#                 any(i.islower() for i in s) and
#                 any(i.isdigit() for i in s)) else 'NO')

"""
Отличники
Учитель Тимур проверял контрольные работы по математике в 
нескольких классах онлайн-школы BEEGEEK и решил убедиться, 
что в каждом классе есть хотя бы один отличник – ученик с 
оценкой 5 по контрольной работе. Напишите программу с 
использованием встроенных функций all(), any() для помощи Тимуру в проверке.

Формат входных данных
На вход программе подается натуральное число n – количество классов. 
Затем для каждого класса вводится блок информации вида:

натуральное число k – количество учеников в классе;
далее вводится k строк вида: фамилия оценка.
Формат выходных данных
Программа должна вывести YES, если в каждом классе есть хотя бы один отличник, 
и NO в противном случае.
"""

# result = []

# for _ in range(int(input())):
#     res = 0
#     for _ in range(int(input())):
#         S = input().split()
#         if int(S[1]) == 5:
#             res += 1
#     result.append(res)
# print("YES" if all(result) else "NO")