"""
Сумма чисел в файле
Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые 
неотрицательные числа и все, что угодно. Числом назовем последовательность 
одной и более цифр, идущих подряд (число всегда неотрицательно).

Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму всех чисел, записанных в файле.

Примечание 1. Если бы файл nums.txt содержал строки:

 123   jhjk
bhjip456qwerty
1x2y3 4 5 6
sfsd 0 dfgfd
10abc20de30pop5 5 5 5
то результатом было бы:

680
Примечание 2. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/530408/nums.txt
"""
# import re
# with open('nums.txt', encoding='utf-8' ) as file:
#     print(sum([sum(map(int, re.findall('\d+', i))) for i in file.readlines()]))

# with open('nums.txt', encoding='utf-8') as file:
#     row = ''.join(c if c.isdigit() else ' ' for c in file.read())
#     print(sum(map(int, row.split())))

# from operator import add
# from functools import reduce

# result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(result)

# # [1, 2, 3, 4, 5, 6, 7, 8, 9]