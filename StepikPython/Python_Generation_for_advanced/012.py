"""
Напишите программу, которая с помощью модуля random моделирует броски монеты. 
Программа принимает на вход количество попыток и выводит результаты бросков: 
Орел или Решка (каждое на отдельной строке).

Примечание. Например, при n=7 ваша программа может выводить:

Орел
Решка
Решка
Орел
Орел
Орел
Решка
"""
# from random import randint
# gen = randint(0, 2)
# for _ in range(int(input())):
#     print("Орел" if gen else "Решка")

"""
Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 66 гранями. Программа принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано на грани кубика (каждое на отдельной строке).

Примечание. Например, при n=7n=7 ваша программа может выводить:

5
5
6
6
2
6
2
"""

# from random import randint

# for _ in range(int(input())):
#     print(randint(1, 6))


"""
Напишите программу, которая с помощью модуля random генерирует случайный пароль. 
Программа принимает на вход длину пароля и выводит случайный пароль, 
содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).

Примечание 1. Символам A..Z английского языка соответствуют номера с 65 по 90 в таблице символов ASCII.

Примечание 2. Символам a..z английского языка соответствуют номера с 97 по 122 в таблице символов ASCII.

Примечание 3. Используйте функцию chr() для получения символа по его номеру в таблице символов ASCII.

Примечание 4. Например, при длине пароля, равной 15 символам ваша программа может выводить:

peJFAmhqfaAeKDu
"""
# from random import randint
# result = []
# for _ in range(int(input())):
#     result.append(chr(randint(65, 90)) if randint(0,1) else chr(randint(97, 122)))
# print(*result, sep='')

"""
Лотерейный билет содержит 7 чисел из диапазона от 1 до 49 (включительно).

Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета. 
Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.

Примечание. Убедитесь, что сгенерированные числа не содержат дубликатов.
"""

# from random import randint
# result = []
# while len(result) != 7:
#     n = randint(1, 49)
#     if n not in result:
#         result.append(n)
# print(*sorted(result))

# import random

# s = set()

# while len(s) < 7:
#     s.add(random.randint(1, 49))

# print(*sorted(s))

"""
IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.

Напишите функцию generate_ip(), которая с помощью модуля random  
генерирует и возвращает случайный корректный IP адрес.

Примечание 1. Пример правильного (неправильного) IP адреса:

192.168.5.250        # правильный
199.300.521.255      # неправильный
Примечание 2. Вызывать функцию generate_ip() не нужно, требуется только реализовать.
"""
# from random import randint
# def generate_ip():
#     result = []
#     for _ in range(4):
#         result.append(str(randint(0, 255)))
#     return '.'.join(result)

# print(generate_ip())

# from random import randrange as r

# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'

"""
Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, 
где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:

AB23_56VG          # правильный
V3F_231GT          # неправильный
Примечание 2. Обратите внимание на символ _ в почтовом индексе.

Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.
"""
# from random import choice
# import string
# def generate_index():
#     result = ''
#     for _ in 'abcd':
#         result += choice(string.ascii_uppercase)
#     for _ in '1234':
#         result += str(choice(string.digits))
#     return result[:2] + result[-2:] + '_' + result[-3:1:-1]
# print(generate_index())

# from random import choice, randint
# from string import ascii_uppercase as letter

# def generate_index():
#     return f'{choice(letter)}{choice(letter)}{randint(0, 99)}_{randint(0, 99)}{choice(letter)}{choice(letter)}'

"""
Напишите программу, которая с помощью модуля random перемешивает случайным 
образом содержимое матрицы (двумерного списка).

Примечание. Выводить содержимое матрицы не нужно.
"""

# from random import sample

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for i in range(len(matrix)):
#     matrix[i] = sample(matrix[i], len(matrix[i]))

# print(matrix)

"""
Напишите программу, которая с помощью модуля random генерирует 
100 случайных номеров лотерейных билетов и выводит их каждый на 
отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

номер не может начинаться с нулей;
номер лотерейного билета должен состоять из 7 цифр;
все 100 лотерейных билетов должны быть различными.
"""
# from random import randint as rint
# result = []
# while len(result) < 100:
#     n = rint(1000000, 9999999)
#     if n not in result:
#         result.append(n)
# print(*result, sep='\n')

"""
Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.

Например, слова пила и липа или пост и стоп – анаграммы.

Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.

Примечание. Обратите внимание на то, что метод shuffle() работает со списком, а не со строкой.
"""
# from random import shuffle
# S = (list(input()))
# shuffle(S)
# print(*S, sep='')

"""
Для игры в бинго требуется карточка размером 5 x 5, содержащая различные (уникальные) 
целые числа от 1 до 75 (включительно), при этом центральная клетка является 
пустой (она заполняется числом 0).

Напишите программу, которая с помощью модуля random генерирует и 
выводит случайную карточку для игры в бинго.

Примечание 1. Для наглядности рекомендуем отводить на вывод каждого числа ровно 3 символа. 
Для этого используйте строковый метод ljust().

Примечание 2. Пример возможного ответа:

1  16 31 46 61
10 30 42 47 68
3  18 0  48 63
9  19 34 49 70
5  20 35 50 65
"""

# from random import sample

# result = list(sample(range(1, 76), 24))
# result.insert(12, 0)
# for _ in range(5):
#     for _ in range(5):
#         print(str(result.pop()).ljust(3), end=' ')
#     print()

# from random import sample

# numbers = sample(list(range(1, 76)), 25)
# bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
# bingo[2][2] = 0

# for i in range(5):
#     for j in range(5):
#         print(str(bingo[i][j]).ljust(3), end=' ')
#     print()

"""
Тайный друг 🌶️
Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, 
который будет вместе с ним решать задачи по программированию.

Формат входных данных
На вход программе в первой строке подается число n – общее количество учеников. 
Далее идут n строк, содержащих имена и фамилии учеников.

Формат выходных данных
Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком) 
и имя и фамилию его тайного друга, разделённые дефисом.

Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и 
нельзя быть тайным другом для нескольких учеников.

Примечание 2. Приведенные ниже тесты это лишь образцы возможного ответа. 
Возможны и другие способы выбора тайных друзей
"""
# from random import shuffle

# S = list(input() for _ in range(int(input())))

# shuffle(S)

# for i in range(len(S)):
#     print(f"{S[i - 1]} - {S[i]}")

"""
Генератор паролей 1
Напишите программу, которая с помощью модуля random генерирует 
n паролей 
длиной m символов, 
состоящих из строчных и прописных английских букв и цифр, 
кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).

Формат входных данных

На вход программе подаются два числа n и m, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести n паролей длиной m символов в соответствии 
с условием задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа n и m всегда таковы, что требуемые пароли сгенерировать возможно.

Примечание 2. В каждом пароле необязательно должна присутствовать хотя 
бы одна цифра и буква в верхнем и нижнем регистре.

Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.

Примечание 4. Приведенные ниже тесты – это лишь образцы возможного ответа. 
Возможны и другие способы генерации паролей.


"""

# from random import choice
# import string
    

# def generate_password(length):
#     result = ''
#     while len(result) < (length):
#         s = choice(string.ascii_letters + string.digits)
#         if s not in 'lI1oO0':
#             result += s
#     return result

# def generate_passwords(count, length):
#     result = []
#     for _ in range(count):
#         result.append(generate_password(length))
#     return result
# n, m = int(input()), int(input())

# print(*generate_passwords(n, m), sep='\n')


"""
Генератор паролей 2 🌶️
Напишите программу, которая с помощью модуля random генерирует 
n паролей 
длиной m символов, состоящих из строчных и прописных английских букв и цифр, 
кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).

Дополнительное условие: в каждом пароле обязательно должна присутствовать 
хотя бы одна цифра и 
как минимум по одной букве в верхнем и нижнем регистре.

Формат входных данных
На вход программе подаются два числа n и m, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести n паролей длиной m символов в соответствии с условием задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа n и m всегда таковы, что требуемые пароли сгенерировать возможно.

Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, состоящий из 
count случайных паролей длиной length символов.

Примечание 3. Приведенные ниже тесты – это лишь образцы возможного ответа. 
Возможны и другие способы генерации паролей.
"""

# from random import choice
# from random import shuffle
# import string
    

# def generate_password(length):
#     result = [choice('23456789'),
#              choice('abcdefghijkmnpqrstuvwxyz'),
#              choice('ABCDEFGHJKLMNPQRSTUVWXYZ')]
#     while len(result) < (length):
#         s = choice(string.ascii_letters + string.digits)
#         if s not in 'lI1oO0':
#             result.append(s)
#     shuffle(result)
#     return ''.join(result)

# def generate_passwords(count, length):
#     result = []
#     for _ in range(count):
#         result.append(generate_password(length))
#     return result
# n, m = int(input()), int(input())

# print(*generate_passwords(n, m), sep='\n')

# import random

# n = 10**6
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)

#     if x ** 3 + y ** 4 >= -2 and 3 * x + y ** 2 <= 2:
#         k += 1

# print((k/n)*s0)

"""
Напишите программу, которая при помощи метода Монте-Карло 
определяет приближённое значение числа π.

Примечание 1. Площадь единичного круга, то есть круга с радиусом, 
равным R = 1 равна S = π * R **2 = π.

Примечание 2. Уравнение единичной окружности имеет вид x ** 2 y **2 = 1.
"""

# import random

# n = 10**6
# k = 0
# s0 = 4
# for _ in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)

#     if x ** 2 + y ** 2 <= 1:
#         k += 1

# print((k/n)*s0)