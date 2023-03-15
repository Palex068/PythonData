# numbers = (0, 1, 3, 14, 2, 7, 9, 8, 10)
# print(numbers)

# names = ('Michael', 'John', 'Freddie')
# print(names)

# colors = ('red', 'green', 'blue')
# colors[0] = 'black'
# print(colors)

# a = (3, 4, 5)
# for i in range(3):
#     a[i] += 3
# print(sum(a))

#        (2, 3, 5, 7, 11, 13)
# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71) 
# print(primes[:6])

#                                   ('Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:-2])

# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
# number = len(countries)
# print(number)

# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)

# print(min(numbers) + max(numbers))

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
# number = countries.count('Spain')
# print(number)

# (1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13)

# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)

# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# # non_empty_tuples = list(filter(bool, tuples))
# non_empty_tuples = list(elem for elem in tuples if len(elem) > 0)

# print(non_empty_tuples)

# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = list(elem[:-1] + (100,) for elem in tuples)
# print(new_tuples)

# poets = [
#     ('Есенин', 13),
#     ('Тургенев', 14),
#     ('Маяковский', 28),
#     ('Лермонтов', 20),
#     ('Фет', 15)]

# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i][1] > poets[j][1]:
#             poets[i], poets[j] = poets[j], poets[i]

# print(poets[0])
# print(poets[-1])

# poets = [
#     ('Тургенев', 14),
#     ('Есенин', 13),
#     ('Маяковский', 28),
#     ('Фет', 15),
#     ('Лермонтов', 20)]

# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i] > poets[j]:
#             poets[i], poets[j] = poets[j], poets[i]

# print(poets[0])
# print(poets[-1])

# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# result = 1
# for n in numbers:
#     result *= n
# print(result)

# data = 'Python для продвинутых!'
# tup = tuple(data)
# print(tup)

"""
Программист Тимур написал программу для работы с биографическими 
данными русских поэтов. Данные содержатся в кортежах вида 
(фамилия, год рождения, город рождения). В процессе работы программы 
в некотором кортеже poet_data обнаружилась ошибка: 
('Пушкин', 1799, 'Санкт-Петербург'), неверно указано место рождения, 
ведь Александр Пушкин родился в Москве.

Дополните приведенный код так, чтобы в переменной poet_data находился 
правильный кортеж (с исправленным значением), а затем выведите его содержимое.
"""
# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = poet_data[:-1] + ("Москва", )
# print(poet_data)

"""
Дополните приведенный код так, чтобы он вывел список, содержащий 
средние арифметические значения чисел каждого вложенного кортежа 
в заданном кортеже кортежей numbers.
"""

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

# print(list(sum(nums) / len(nums) for nums in numbers))

"""
Вершина параболы
Уравнение параболы имеет вид y = a * x ** 2 + b * x + c, где a != 0. 
Напишите программу, которая по введенным значениям a, b, c определяет и выводит вершину параболы.
x = - b / (2 * a)
y = (4 * a * c - b ** 2) / (4 * a)
Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести координаты вершины параболы.

Примечание. Координаты вершины параболы 
x = - b / (2 * a)
y = (4 * a * c - b ** 2) / (4 * a)
"""

# a, b, c = map(int, list(input() for _ in 'abc'))

# x = - b / (2 * a)
# y = (4 * a * c - b ** 2) / (4 * a)
# coor = (x, y)
# print(coor)

"""
Конкурсный отбор
Напишите программу, которая выводит список хорошистов и отличников в классе.

Формат входных данных
На вход программе подается натуральное число n, далее следует n
 строк с фамилией школьника и его оценкой на каждой из них.

Формат выходных данных
Программа должна вывести сначала все введённые строки с фамилиями
и оценками учеников в том же порядке. Затем следует пустая строка, 
а затем выводятся строки с фамилиями и оценками хорошистов 
и отличников (в том же порядке).

Примечание 1. Оценка ученика – это натуральное число от 1 до 5.

Примечание 2. Гарантируется, что в классе есть хотя бы один хорошист
 – обладатель оценки 4, или отличник – получивший 5.
"""

# N = int(input())
# data = list(input().split() for _ in range(N))
# result = []

# for i in data:
#     print(*i)
#     if int(i[1]) >= 4:
#         result.append(i)
# print()

# for i in result:
#     print(*i)

# a, b, c = 10, 20, 30
# c, b, a = a + b, b*2, a + b + c

# print(a, b, c)

# points = [('матан', 100), ('линал', 98), ('ангем', 90)]

# subject, value = points[1]

# print(subject, value)

# notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')

# do, re, mi, *tail = notes

# print(tail)

"""
Последовательность Трибоначчи
Напишите программу, которая считывает натуральное число n и 
выводит первые n чисел последовательности Трибоначчи.

Формат входных данных
На вход программе подается одно число n (n ≤ 100) – количество членов последовательности.

Формат выходных данных
Программа должна вывести члены последовательности Трибоначчи, отделенные символом пробела.

Примечание. Последовательность Трибоначчи – последовательность натуральных чисел, 
где каждое последующее число является суммой трех предыдущих:
"""

# N = int(input())

# trib = [1, 1, 1]

# if N == 1:
#     print(1)
# elif N == 2:
#     print('1 1')
# elif N == 3:
#     print('1 1 1')
# else:
#     for i in range(3, N):
#         trib.append(trib[i - 3] + trib[i - 2] + trib[i - 1])
#     print(*trib)


# tpl = (100,)
# print(tpl * 2)

# tpl = (10, 20, 30, 40, 50, 60, 70, 80)
# print(tpl[2:5], tpl[:4], tpl[3:])

# tpl = ('Orange', [10, 20, 30], (5, 15, 25))
# print(tpl[1:2])

# tpl = (1777, 'a')
# print(max(tpl))

# tpl = ('Green')
# print(type(tpl))

# a, *b, c = 'No bees', 'no honey'
# print(b)