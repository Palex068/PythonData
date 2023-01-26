import os
os.system('cls')

# print(5, 8, 6)


# n = 5
# print(n)

# n = None
# print(n)

# n = 1.89
# print(n)

# n = 'qwer'
# n1 = "qwerty"

# print(n, n1)





# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{} -- {}'.fotmat(a, b))



# print('Введите а')
# a = input() # 10
# print('Введите b')
# b = input() # 20
# c = a + b
# print(a, ' + ', b, ' = ', c)

# print('Введите а')
# a = int(input()) # 10
# print('Введите b')
# b = int(input()) # 20
# c = a + b
# print(a, ' + ', b, ' = ', c)

# print('Введите а')
# a = float(input()) # 10
# print('Введите b')
# b = float(input()) # 20
# c = a + b
# print(a, ' + ', b, ' = ', c)

# n = 5
# print(type(n))

# n = 'qwer'
# print(type(n))

# n = 'qw\'er'
# print(n)

# a = 5
# b = 5.89
# c = 'Hallo'

# c = 5.89
# print(c)
# print(type(c))

# c = int(c)
# print(c)
# print(type(c))

# c = str(c)
# print(c)
# print(type(c))

# c = 1
# c = bool(c)
# print(c)
# print(type(c))

# a = int(input('Введите а '))
# b = int(input('Введите b '))
# c = a + b

# print(a, ' + ', b, ' = ', c)
# print(a,' + ',b,' = ',c)
# print(f"{a} + {b} = {c}")
# print("{} + {} = {}".format(a,b,c))

# a = 5.89956
# b = 6.556551
# print(round(a*b, 3))

# iter = 10
# print(iter); iter = 10
# iter += 3 # iter = iter + 3
# print(iter); iter = 10
# iter -= 4 # iter = iter - 4
# print(iter); iter = 10
# iter *= 5 # iter = iter * 5
# print(iter); iter = 10
# iter /= 3 # iter = iter / 3
# print(iter); iter = 10
# iter //= 3 # iter = iter // 3
# print(iter); iter = 10
# iter %= 3 # iter = iter % 2
# print(iter); iter = 10
# iter **= 3 # iter = iter ** 3
# print(iter)

# a = 1 > 4
# print(f'a = 1 > 4 \t\t {a}')

# a = 1 < 4 and 5 > 2
# print(f'a = 1 < 4 and 5 > 2 \t {a}')

# a = 1 == 2
# print(f'a = 1 == 2 \t\t {a}')

# a = 1 != 2
# print(f'a = 1 != 2 \t\t {a}')

# a = 'qwe'
# b = 'qwe'
# print(f'a = \'qwe\' b = \'qwe\'\t {a == b}')

# a = 1 < 3 < 4 < 5 < 10
# print(f'a = 1 < 3 < 4 < 5 < 10 \t {a}')

# username = input('Введите имя: ')
# if(username == 'Маша'):
#     print('Ура, это же МАША!')
# else:
#     print('Привет, ', username)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# original = 45
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for i in 1, -2, 3, 14, 5:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]

# numbers = list(range(1, 5))
# print(numbers) # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]

# for k in numbers:
#     k *= 2
#     print(k) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]
# num2 = [1, 2, 3]
# c = [x + y for x in numbers for y in num2]
# print(*c, sep=", ", end=';\n')


# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#      print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(*colors)
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType
