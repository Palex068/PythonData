"""
Звездный прямоугольник 1
Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14 \times 1014×10 в соответствии с образцом:

**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
Примечание. Для вывода прямоугольника используйте цикл for.
"""

# def draw_box():
#     for i in range(14):
#         if i == 0 or i == 13:
#             print('*' * 10)
#         else:
#             print('*' + ' ' * 8 + '*')

# # основная программа
# draw_box()  # вызов функции

"""
Звездный треугольник 1
Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 1010 в соответствии с образцом:

*
**
***
****
*****
******
*******
********
*********
**********
Примечание. Для вывода треугольника используйте цикл for.  
"""
# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
# # основная программа
# draw_triangle()  # вызов функции

"""
Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.
"""
# def draw_triangle(fill, base):
#     for i in range(1, base + 1):
#         print(fill * min(i, base - i + 1))


# def draw_triangle(fill = '*', base = 7):
#     for i in range(1, base + 1):
#         print(fill * (i if i <= (base + 1) // 2 else base - i + 1))

# # считываем данные
# fill = input()
# base = int(input())

# # вызываем функцию
# draw_triangle(fill, base)

"""
ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.

Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
"""

# # объявление функции
# def print_fio(name, surname, patronymic):
#     result = str.upper(surname[0] + name[0] + patronymic[0])
#     print(result)

# # считываем данные
# name, surname, patronymic = input(), input(), input()

# # вызываем функцию
# print_fio(name, surname, patronymic)

"""
Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
"""

# # объявление функции
# def print_digit_sum(num):
#     print(sum(list(map(int, list(str(num))))))

# # считываем данные
# n = int(input())

# # вызываем функцию
# print_digit_sum(n)

# def swap(a, b):
#     a, b = b, a

# a = 4
# b = 3
# swap(a, b)
# print(a - b)

# number = 101

# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#             break
#     if num != 1 and flag == True:
#         print('Число', num, 'простое.')
#     else:
#         print('Число', num, 'составное.')


# x = 17
# y = int(input())
# is_prime(x)
# is_prime(y)
# is_prime(number)

"""
Конвертер километров
Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента 
расстояние в километрах и возвращает расстояние в милях. 
Формула для преобразования: мили = километры * 0.6214.

Примечание. Следующий программный код:

print(convert_to_miles(1))
print(convert_to_miles(5))
print(convert_to_miles(10))
должен выводить:

0.6214
3.107
6.214
"""

# # объявление функции
# def convert_to_miles(km):
#     return km * 0.6214

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(convert_to_miles(num))

"""
Количество дней
Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца
 и возвращает количество дней в данном месяце.

Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.

Примечание 2. Считайте, что год является невисокосным.

Примечание 3. Следующий программный код:

    print(get_days(1))
    print(get_days(2))
    print(get_days(9))

должен выводить:

    31
    28
    30
"""

# # объявление функции
# def get_days(month):
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif month == 2:
#         return 28
#     return 30

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(get_days(num))

"""
Делители 1
Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное
число и возвращающую список всех делителей данного числа.

Примечание. Следующий программный код:

print(get_factors(1))
print(get_factors(5))
print(get_factors(10))
должен выводить:

[1]
[1, 5]
[1, 2, 5, 10]
"""

# # объявление функции
# def get_factors(num):
#     factors = []
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             factors.append(i)
#     factors.append(num)
#     return factors

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_factors(n))

"""
Делители 2
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и 
возвращающую количество делителей данного числа.

Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

Примечание 2. Следующий программный код:

print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))
должен выводить:

1
2
4
"""

# # объявление функции
# def number_of_factors(num):
#     factors = []
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             factors.append(i)
#     factors.append(num)
#     return len(factors)
# # считываем данные
# n = int(input())

# вызываем функцию
# print(number_of_factors(n))

"""
Найти всех
Напомним, что строковый метод find('a') возвращает местоположение 
первого вхождения символа a в строке. Проблема заключается в том, 
что данный метод не находит местоположение всех символов а.

Напишите функцию с именем find_all(target, symbol), которая принимает 
два аргумента: строку target и символ symbol и возвращает 
список, содержащий все местоположения этого символа в строке.

Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

Примечание 2. Следующий программный код:

print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))
должен выводить:

[0, 4, 7, 8, 9]
[]
[4]
"""

# # объявление функции
# def find_all(target, symbol):
#     return list(i for i in range(len(target)) if target[i] == symbol)


# # считываем данные
# s = input()
# char = input()

# # вызываем функцию
# print(find_all(s, char))

"""
Merge lists 1
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов 
два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.

Примечание 1. Списки list1 и list2 могут иметь разную длину.

Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎.

Примечание 3. Следующий программный код:

print(merge([1, 2, 3], [5, 6, 7, 8]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
должен выводить:

[1, 2, 3, 5, 6, 7, 8]
[1, 5, 6, 7, 10, 13, 16, 20]
"""

# # объявление функции
# def merge(list1, list2):
#     return sorted(list(list1 + list2))

# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# # вызываем функцию
# print(merge(numbers1, numbers2))

"""
Merge lists 2
На вход программе подается число n, а затем n строк, содержащих 
целые числа в порядке возрастания. Из данных строк формируются списки чисел. 
Напишите программу, которая объединяет указанные списки в один отсортированный 
список с помощью функции quick_merge(), а затем выводит его.

Формат входных данных
На вход программе подается натуральное число n, а затем n строк, содержащих 
целые числа в порядке возрастания, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
# def merge_lists():
#     result = []
#     for _ in range(int(input())):
#         for j in input().split():
#             result.append(int(j))
#     return sorted(result)

# print(merge_lists())

"""
Is Valid Triangle?
Напишите функцию is_valid_triangle(side1, side2, side3), которая 
принимает в качестве аргументов три натуральных числа, и возвращает 
значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.

Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.

Примечание 2. Следующий программный код:

print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))
должен выводить:

True
False
True
"""

# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     N = sorted(list(n for n in [side1, side2, side3]))
#     return N[2] < N[0] + N[1]

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))

"""
Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента 
натуральное число и возвращает значение 
True если число является простым и False в противном случае.

Примечание. Следующий программный код:

print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
должен выводить:

False
False
True
"""

# # объявление функции
# def is_prime(num):
#     if n == 2:
#         return True
#     elif n == 1 or n % 2 == 0:
#         return False
#     for i in range(3, int((n ** 0.5) + 1), 2):
#         if (n % i == 0):
#             return False
#     return True

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))

"""
Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента 
натуральное число num и возвращает первое простое число большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

 Примечание 2. Следующий программный код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
должен выводить:

7
11
17
"""

# объявление функции
# from itertools import count

# def is_prime(n):
#     if n == 2:
#         return True
#     elif n == 1 or n % 2 == 0:
#         return False
#     for i in range(3, int((n ** 0.5) + 1), 2):
#         if (n % i == 0):
#             return False
#     return True

# def get_next_prime(num):
#     for i in count(num + 1):
#         if is_prime(i):
#             return i


# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_next_prime(n))

"""
Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве аргумента 
строковое значение пароля password и возвращает значение True если пароль является 
надежным и False в противном случае.

Пароль является надежным если:

его длина не менее 8 символов; 
он содержит как минимум одну заглавную букву (верхний регистр); 
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.

Примечание. Следующий программный код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
должен выводить:

True
False
"""


# def is_password_good(password):
#     good_password_len = 8
#     if (len(password) >= good_password_len 
#         and str.upper(password) != password 
#         and str.lower(password) != password
#         and any(list(str.isdigit(ch) for ch in list(password)))):
#             return True
#     return False


# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))

"""
Ровно в одном
Напишите функцию is_one_away(word1, word2), которая 
принимает в качестве аргументов два слова word1 и word2 и 
возвращает значение True если слова имеют одинаковую длину и 
отличаются ровно в 1 символе и False в противном случае.

Примечание. Следующий программный код:

print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
должен выводить:

True
True
False
False
"""
# объявление функции
# def is_one_away(w1, w2):
#     return True if len(list(w1[i] for i in range(len(w1)) if w1[i] != w2[i])) == 1 else False 
    
# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))

"""
Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает 
в качестве аргумента строку text и возвращает значение 
True если указанный текст является палиндромом и False в противном случае.

Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

Примечание 3. Следующий программный код:

print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))
должен выводить:

True
True
False
"""

# # объявление функции
# def is_palindrome(text):
#     T = []
#     for ch in list(text):
#         if str.isalpha(ch):
#             T.append(str.lower(ch))
#     print(T)
#     if T == T[::-1]:
#         return True
#     return False

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_palindrome(txt))

"""
BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные 
банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид 
a:b:c, где a, b и c – натуральные числа. 
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:

True
False
False
False
"""


# def is_prime(n):
#     if n == 2:
#         return True
#     elif n == 1 or n % 2 == 0:
#         return False
#     for i in range(3, int((n ** 0.5) + 1), 2):
#         if (n % i == 0):
#             return False
#     return True


# def is_palindrome(n):
#     if list(str(n)) == list(str(n))[::-1]:
#         return True
#     return False

# def is_even(n):
#     return not n % 2


# def is_valid_password(password):
#     T = list(int(n) for n in password.split(':'))
    
#     if (len(T) == 3
#         and is_palindrome(T[0])
#         and is_prime(T[1])
#         and is_even(T[2])):
#         return True
#     return False

# # считываем данные
# psw = input()

# # вызываем функцию
# print(is_valid_password(psw))

# def is_valid_password(password):
#     password = password.split(':')
#     a, b, c = password[0], int(password[1]), int(password[2])
#     if len(password) != 3 or a != a[::-1] or c % 2 != 0:
#         return False
#     for i in range(2, b):
#         if b % i == 0:
#             return False
#     return True   
    
# psw = input()
# print(is_valid_password(psw))

"""
Правильная скобочная последовательность 🌶️
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента 
непустую строку text, состоящую из символов ( и ) и возвращает значение 
True если поступившая на вход строка является правильной скобочной 
последовательностью и False в противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка, 
состоящая только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.

Примечание 2. Следующий программный код:

print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))
должен выводить:

True
False
"""

# # объявление функции

# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return not text

# def is_correct_bracket(text):
#     while len(text) != 0:
#         if text[0] == ')' or text[-1] == '(':
#             return False
#         text = text.replace('()', '')
#         print(text)
#     else:
#         return True
    
# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_correct_bracket(txt))

"""
Змеиный регистр
Напишите функцию convert_to_python_case(text), которая 
принимает в качестве аргумента строку в «верблюжьем регистре» и 
преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
должен выводить:

this_is_camel_cased
is_prime_number
"""

# # объявление функции
 

# def convert_to_python_case(text):
#     return ''.join(['_' + i if i.isupper() else i for i in text]).lstrip('_').lower()


# def convert_to_python_case(text):
#     s = ''
#     for el in text:
#         if el.isupper():
#             s += '_'
#         s += el.lower()
#     return s[1:]


# def convert_to_python_case(text):
#     T = list(text)
#     T[0] =  T[0].lower()
#     for i in range(len(T)):
#         if T[i].isupper():
#             T[i] = "_" + T[i].lower()            
#     return "".join(T)

# # считываем данные
# txt = input()

# # вызываем функцию
# print(convert_to_python_case(txt))

"""
Середина отрезка
Напишите функцию get_middle_point(x1, y1, x2, y2), которая 
принимает в качестве аргументов координаты концов отрезка (x_1; y_1) и (x_2; y_2) и 
возвращает координаты точки являющейся серединой данного отрезка.

Примечание 1. Координаты середины отрезка с концами в точках (x_1; y_1) и (x_2; y_2)

x = (x_1 + x_2) / 2
y = (y_1 + y_2) / 2

Примечание 2. Следующий программный код:

print(get_middle_point(0, 0, 10, 0))
print(get_middle_point(1, 5, 8, 3))
должен выводить:

5.0 0.0
4.5 4.0

"""

# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y

# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

"""
Площадь и длина
Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и 
возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.

Примечание 1. Длина окружности и площадь круга радиуса rr вычисляются по формулам:

С=2πr,S=πr ** 2.

Примечание 2. Для числа π используйте глобальную константу из модуля math.

Примечание 3. Следующий программный код:

print(get_circle(1))
print(get_circle(1.5))

должен выводить:

6.283185307179586 3.141592653589793
9.42477796076938 7.0685834705770345
"""
# from math import pi

# # объявление функции
# def get_circle(radius):
#     C = 2 * pi * radius
#     S = pi * radius ** 2
#     return C, S

# # считываем данные
# r = float(input())

# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)



def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    x1 = (- b + D ** 0.5) / (2 * a)
    x2 = (- b - D ** .5) / (2 * a)
    return min(x1, x2), max(x1, x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)