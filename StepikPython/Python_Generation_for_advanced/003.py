# num1 = 3 * True - (True + False)
# num2 = (True + True + False) ** 3 + 5
# print(num1 + num2)

# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1) 
# print(res)

# print(bool(0.0))
# print(bool())
# print(bool('abc'))
# print(bool(list(range(10))))

"""
Предикат делимости
Напишите функцию func(num1, num2), принимающую в качестве 
аргументов два натуральных числа num1 и num2 и возвращающую 
значение True если число num1 делится без остатка на число 
num2 и False в противном случае.

Результатом вывода программы должно быть "делится" 
(если функция func() вернула True) и "не делится" 
(если функция func() вернула False).

Примечание. Следующий программный код:

print(func(10, 2))
print(func(5, 7))
print(func(15, 15))
должен выводить:

True
False
True
а вся программа должна выводить:

делится
не делится
делится
"""

# a, b = int(input()), int(input())
# if a % b:
#     print("не делится")
# else:
#     print("делится")

# # объявление функции
# def func(num1, num2):
#     return num1 % num2

# # считываем данные
# num1, num2 = int(input()), int(input())

# # вызываем функцию
# if func(num1, num2):
#     print("не делится")
# else:
#     print("делится")