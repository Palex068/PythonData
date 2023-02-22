"""
Тимур и его числа
Тимур загадал число от 1 до n. 
За какое наименьшее количество вопросов (на которые Тимур отвечает "больше" или "меньше") 
Руслан может гарантированно угадать число Тимура?

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести наименьшее количество вопросов, которых гарантированно хватит Руслану, чтобы угадать число Тимура.
"""
# from math import log2
# n = log2(int(input()))
# print(int(n) if int(n) == n else int(n) + 1)

# S = input()
# ru_az = 'А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'.split()
# en_az = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
# shift = 0
# result = []
# if S[0] in ru_az:
#     az = ru_az
# else:
#     az = en_az

# ROT = len(az) - shift
# for j in range(len(en_az)):
#     for i in range(len(S)):
#         if S[i].upper() in az:
#             pos = az.index(S[i].upper())
#             ins = az[pos - ROT + j] if S[i].isupper() else az[pos - ROT + j].lower()
#             result.append(ins)
#         else:
#             result.append(S[i])
#     print(j)
#     print(*result, sep='')
#     result.clear()


# string = input()
# ru_az = 'А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'.split()
# en_az = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
# shift = 4
# result = []

# for S in string.split():
#     if S[0] in ru_az:
#         az = ru_az
#     else:
#         az = en_az
#     for i in range(len(S)):
#         if S[i].upper() in az:
#             shift = sum(1 for i in range(len(S)) if S[i].upper() in az)
#             ROT = len(az) - shift
#             pos = az.index(S[i].upper())
#             ins = az[pos - ROT] if S[i].isupper() else az[pos - ROT].lower()
#             result.append(ins)
#         else:
#             result.append(S[i])
#     result.append(" ")
# print(*result, sep='')
# # 

# print(int('1000000001', base=2))
# print(bin(513))
# print(oct(31))
# print(hex(1000))


# print(bin(n := int(input()))[2:], oct(n)[2:], hex(n).upper()[2:], sep='\n')

