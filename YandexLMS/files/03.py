'''
Антитела

Напишите программу, которая выводит строки с нулевыми антителами. 
Если таких несколько, вывести в алфавитном порядке через запятую и пробел.

Вводится три строки с названиями антител и через пробел их количеством.

Вывести одну строку.
'''

# Это решение добавим позже, когда изучим методы списков

# str = [input() for _ in range(3)]
# res = []
# for i in str:
#     count = 0
#     for ch in '123456789':
#         if ch in i:
#             count += 1
#             break
#     if count == 0:
#         res.insert(3, i)
# print(*res, sep=', ')

# Это решение короче

# str = [input() for _ in range(3)]
# res = []
# for i in str:
#     if ' 0' in i:
#         res.insert(3, i)
# print(*res, sep=', ')

print(*[str for str in (input(), input(), input()) if ' 0' in str], sep=', ')
