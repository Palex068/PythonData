# def add_five(a, b):
#     return a+5, b+5

# result = add_five(3, 2)
# print(result)

# def display(*args):
#     for i in args:
#         print(i, end=' ')

# display(name='Emma', age=25)

# def display(*args):
#     for i in args:
#         print(i, end=' ')

# display(name='Emma', age=25)

# def display(**kwargs):
#     for i in kwargs:
#         print(i, end=' ')

# display(emp='Kelly', salary=9000)

# def outer_func(a, b):
#     def inner_func(c, d):
#         return c + d + a*b
#     return inner_func

# res = outer_func(5, 10)(3, 2)

# print(res)

# num = int('1000001', 2)
# print(num)

"""
Письмо для экзамена
Напишите функцию generate_letter(), которая будет собирать электронное письмо в 
соответствии с шаблоном:

To: <mail>
Приветствую, <name>!
Вам назначен экзамен, который пройдет <date>, в <time>.
По адресу: <place>. 
Экзамен будет проводить <teacher> в кабинете <number>. 
Желаем удачи на экзамене!

Функция должна получать на вход пять обязательных аргументов 
mail, name, date, time, place и два необязательных 
teacher, number и возвращать текст готового письма. 
При отсутствии аргумента teacher учителем будет Тимур Гуев, 
а если нет аргумента number, то кабинет будет 17.

Примечание 1. Следующий программный код:

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))
должен выводить:

To: lara@yandex.ru
Приветствую, Лариса!
Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
По адресу: Часова 23, корпус 2. 
Экзамен будет проводить Тимур Гуев в кабинете 17. 
Желаем удачи на экзамене!

To: lara@yandex.ru
Приветствую, Лариса!
Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
По адресу: Часова 23, корпус 2. 
Экзамен будет проводить Василь Ярошевич в кабинете 23. 
Желаем удачи на экзамене!
Примечание 2. Вызывать функцию generate_letter() не нужно, требуется только реализовать.
"""

# def generate_letter(mail, name, date, time, place, teacher = 'Тимур Гуев', number = 17):
#     return (f"""To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}. 
# Экзамен будет проводить {teacher} в кабинете {number}. 
# Желаем удачи на экзамене!""")

# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))

"""
Pretty print
Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой. 

Функция должна получать на вход один обязательный аргумент data – список, 
который следует вывести и два необязательных строковых односимвольных  
аргумента side и delimiter и выводить содержимое списка в соответствии с примерами.

В случае если отсутствует аргумент side, то полагаем side='-', 
а если отсутствует аргумент delimiter, то полагаем delimiter='|'.

Примечание 1. Следующий программный код:

pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
должен выводить:

 ------------------------------ 
| 1 | 2 | 10 | 23 | 123 | 3000 |
 ------------------------------ 
 ------------------------- 
| abc | def | ghi | 12345 |
 ------------------------- 
 ***************** 
| abc | def | ghi |
 ***************** 
 ----------------- 
# abc # def # ghi #
 ----------------- 
 ***************** 
# abc # def # ghi #
 ***************** 
Примечание 2. Вызывать функцию pretty_print() не нужно, требуется только реализовать.

Примечание 3. Считайте, что side и delimiter состоят всегда из одного символа.
"""
# def pretty_print(*args, side='-', delimiter='|'):
#     s2 =delimiter + " "+ f' {delimiter} '.join(map(str, list(*args))) + " " + delimiter
#     s = " "+ (len(s2)-2)* side + " "
#     print(s)
#     print(s2)
#     print(s)

# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

# print((lambda x: (x + 3) * 5 / 2)(3))

# data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
# result = list(map(lambda x: '.'.join(x), data))
# print(result[1])

# result = list(filter(str.swapcase, ['a', '1', '', 'b', '2']))

# print(result)

# files = ['duwwouy440.py', 'crocst0sse.cs', 'j9t7ga2s6x.java', 'jk4nnes4tp.py', '2spc9uqzhu.doc', 
#          'qi0ujxe0c7.png', 'z5x7l1j1d8.jpg', 'i5wtdxh366.geo', 'h53s2m2p73.py', 'ojty11f02d.sx', 
#          'jyjuwlvwb3.st', 'gv4940lf8m.txt', 'op38fy9m9x.docx', 'o02ltr8vbp.xlsx', 'la97gc4js4.html', 
#          'lcihrp8c6l.py', 'z66y7dgfo1.py', 'ckoks0849e.csv']

# result = list(filter(lambda s: s.endswith('.py'), files))

# print(len(result))

# print(list(filter(None, ['', 1, 7, 'beegeek', None, False, 0])))

# from functools import reduce

# numbers = [1, 2, 3]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)

# from functools import reduce

# numbers = [1, 2, 3]
# result = reduce(lambda a, b: a * b, numbers, 10)
# print(result)

# from functools import reduce

# words = ['beegeek', 'stepik', 'python', 'iq-option']
# result = reduce(lambda a, b: a if len(a) > len(b) else b, words)
# print(result)

# from functools import reduce

# result = reduce(lambda s, x: s + str(x), [1, 2, 3, 4, 5], '+')
# print(result)

# from functools import reduce
# import operator

# def flatten(data):
#     return reduce(operator.concat, data, [])

# result = flatten([[1, 2], [3, 4], [], [5]])

# print(result)

"""
Напишите функцию concat(), принимающую переменное количество аргументов и 
объединяющую их в одну строку через разделитель (sep). 
Если разделитель не задан, им служит пробел.

Примечание 1. Обратите внимание, что функция concat() должна принимать не список, а именно переменное количество аргументов.

Примечание 2. Приведенный ниже код, при условии, что функция concat() написана правильно

print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
должен выводить:

hello python and stepik
hello*python*and*stepik
hello()()()python
hello
1$$2$$3$$4$$5$$6$$7$$8$$9
Примечание 3. Вызывать функцию concat() не нужно, требуется только реализовать.

"""
# def concat(*args, sep=' '):
#     data = f'{sep}'.join(map(str, list(args)))
#     return data

# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

"""
Перепишите функцию product_of_odds() в функциональном стиле 
с использованием встроенных функций filter() и reduce().

def product_of_odds(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result

Примечание 1. Тестирующая система никак не "покарает" вас за 
неиспользование встроенных функций filter() и reduce(), однако 
лучше сделать это задание честно 😃.

Примечание 2. Вызывать функцию product_of_odds() не нужно, 
требуется только реализовать ее в функциональном стиле.
"""

# from functools import reduce
# from operator import mul

# def product_of_odds(data):
#     return reduce(mul, filter(lambda x: x % 2 == 1, data), 1)

"""
Дан список слов words. Допишите код после оператора распаковки (*), 
который оборачивает в двойные кавычки все элементы списка words, 
а затем печатает результат на одной строке через пробел.

Примечание. Вспомните про встроенную функцию map() и анонимные функции lambda.
"""

# words = 'the world is mine take a look what you have started'.split()

# print(*map(lambda x: f'"{x}"', words))

"""
Дан список целых чисел numbers. Допишите код после оператора распаковки (*), 
для удаления из списка всех чисел-палиндромов и печати результата на одной 
строке через пробел.

Примечание. Вспомните про встроенную функцию filter() и анонимные функции lambda.
"""

# numbers = [18, 191, 9009, 5665, 78, 77, 45,
#            23, 19991, 908, 8976, 6565, 5665,
#            10, 1000, 908, 909, 232, 45654, 786]

# print(*filter(lambda x: str(x) != str(x)[::-1], numbers))

"""
Дан список numbers, состоящий из кортежей. Допишите пропущенную 
часть программы, чтобы список sorted_numbers был упорядочен 
по убыванию среднего арифметического элементов кортежей списка numbers.

Примечание. Вспомните про анонимные функции lambda.
"""

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

# sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)

# print(sorted_numbers)

"""
Напишите функцию call(), которая принимает произвольную функцию и аргументы для неё и делает вызов переданной функции, возвращая ее значение.

Примечание 1. Приведенный ниже код, при условии, что функция call() написана правильно

def mul7(x):
    return x * 7


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z


print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))
должен выводить:

70
9
80
False
Примечание 2. Вызывать функцию call() не нужно, требуется только реализовать ее.
"""

# def mul7(x):
#     return x * 7


# def add2(x, y):
#     return x + y


# def add3(x, y, z):
#     return x + y + z


# def call(f, *args):
#     return f(*args)

# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))

"""
Напишите функцию compose(), которая принимает на вход две других 
одноаргументных функции f и g и возвращает новую функцию. 
Эта новая функция также должна принимать один аргумент x 
и применять к нему исходные функции в нужном порядке: 
для функций f и g порядок применения должен выглядеть, как f(g(x)).

Примечание 1. Приведенный ниже код, при условии, что функция compose() написана правильно

def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))

должен выводить:

28
17
3333333
35

Примечание 2. Вызывать функцию compose() не нужно, требуется только реализовать ее.

Примечание 3. С точки зрения математики, композиция функций f и g — 
это новая функция h(x) = f(g(x)), при этом порядок применения функций f и g важен! 
"""

# def add3(x):
#     return x + 3


# def mul7(x):
#     return x * 7

# def compose(f, g):
#     return lambda x: f(g(x))

# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))


"""
Напишите функцию arithmetic_operation(), которая принимает символ одной 
из четырех арифметических операций (+, -, *, /) и возвращает функцию 
двух аргументов для соответствующей операции.

Примечание 1. Приведенный ниже код, при условии, что функция 
arithmetic_operation() написана правильно

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
должен выводить:

30
4.0
Примечание 2. Вызывать функцию arithmetic_operation() не нужно, 
требуется только реализовать ее.

Примечание 3. Модуль operator может быть полезен при решении этой задачи (функции модуля тут). 
"""


# from operator import *
# def arithmetic_operation(operation):
#     result = {'+': add, '-': sub, '*': mul, '/': truediv}
#     return result[operation]
 
    
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))

"""
В одну строку
Дана строка из разделенных пробелами слов в разных регистрах. 
Напишите программу, которая отсортирует слова независимо от регистра, 
а затем выведет их. Отсортированные слова должны выводиться на печать 
в исходном регистре, в каком переданы программе на вход.

Формат входных данных
На вход программе подается строка из разделенных пробелами слов в разных регистрах.

Формат выходных данных
Программа должна вывести строку разделенных пробелом отсортированных слов в прежних регистрах.

Примечание 1. Решите задачу в одну строку кода 😎.

Примечание 2. Встроенная функция sorted() сортирует строки в 
лексикографическом порядке, но учитывает регистр буквы. 
Любая буква в верхнем регистре считается идущей раньше, чем буква в нижнем регистре.

Тестовые данные 🟢
Sample Input:

cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo
Sample Output:

bee cat CatAlo cate CATERS Cats cATwalk dolphin Frog FROGs mOus mouse
"""

# print(*sorted(input().split(), key=lambda x: x.lower()))

"""
Гематрия слова
Гематрией слова называется сумма числовых значений входящих в него букв.

Для вычисления гематрии слова в этой задаче:

переведём слово в верхний регистр;
числовое значение буквы вычислим как код(буквы) - код(буквы A).

На вход программе подается натуральное число n, а затем n строк английских слов в разных регистрах.

Напишите программу, которая выводит слова в начальном регистре 
(каждое на отдельной строке) в порядке возрастания их гематрии. 
Если гематрия слов совпадает, они выводятся в алфавитном (лексикографическом) порядке.

Формат входных данных
На вход программе подается натуральное число n, а затем n строк английских слов в разных регистрах.

Формат выходных данных
Программа должна отсортировать слова в соответствии с условием задачи.

Примечание 1. Для получения кода символа воспользуйтесь встроенной функцией ord().

Примечание 2. Слова во входных данных могут повторяться.

Примечание 3. Пусть требуется вычислить гематрию слова BaSis. 
Переводим его в верхний регистр BASIS. 
Для каждого символа в слове находим его код с помощью встроенной функции ord():

ord('B') = 66
ord('A') = 65
ord('S') = 83
ord('I') = 73
ord('S') = 83

В соответствии с условием задачи вычисляем 
числовое значение буквы как 
код(буквы) - код(буквы A). 
Вычитаем из кода каждой буквы значение ord('A') = 65:

ord('B') - ord('A') = 66 - 65 = 1
ord('A') - ord('A') = 65 - 65 = 0
ord('S') - ord('A') = 83 - 65 = 18
ord('I') - ord('A') = 73 - 65 = 8
ord('S') - ord('A') = 83 - 65 = 18

Гематрия слова BaSis равна 1+0+18+8+18 = 45. 
"""
# S = sorted(input() for _ in range(int(input())))

# def geom(S):
#     result = 0
#     for ch in S.upper():
#         result += ord(ch) - ord('A')
#     return result

# print(*sorted(S, key=lambda x: geom(x)), sep='\n')

"""
Сортировка IP-адресов
IP-адрес – уникальный числовой идентификатор устройства 
в компьютерной сети, работающий по протоколу TCP/IP.

В 4-й версии IP-адрес представляет собой 32-битное число. 
Адрес записывается в виде четырёх десятичных чисел (октетов) 
со значением от 0 до 255, разделённых точками, например, 192.168.1.2

Напишите программу, которая считывает IP-адреса и выводит 
их в порядке возрастания в соответствии с десятичным представлением.

Формат входных данных
На вход программе подается число n (n ≥ 1) – количество IP-адресов. 
Затем n строк с корректными IP-адресами.

Формат выходных данных

Программа должна вывести IP-адреса в порядке возрастания в соответствии с десятичным представлением.

Примечание 1. Чтобы перевести IP-адрес 192.168.1.2 в десятичное число мы используем формулу:

192 * 256 ** 3 + 168 * 256 ** 2 + 1 * 256 * 1 + 2 * 256 * 0 = 3232235778
Примечание 2. Используйте необязательный аргумент key.
"""

# S = list(input() for _ in range(int(input())))

# def ip_sum(x):
#     N = list(map(int, x.split('.')))
#     return N[0] * 256 ** 3 + N[1] * 256 ** 2 + N[2] * 256 + N[3]
    

# print(*sorted(S, key=lambda x: ip_sum(x)), sep='\n')
