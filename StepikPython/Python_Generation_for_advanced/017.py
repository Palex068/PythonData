"""
Содержимое файла
На вход программе подается строка с именем текстового файла. 
Напишите программу, которая выводит на экран его содержимое.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести содержимое указанного файла.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Не забудьте закрыть файл 🙂.
"""


# file_name = input()
# file = open(file_name, 'r', encoding='utf-8')
# content = file.read()
# print(content)
# file.close()

# with open(input()) as f:
#     print(f.read())

"""
Предпоследняя строка
На вход программе подается строка с именем текстового файла. 
Напишите программу, которая выводит на экран его предпоследнюю строку.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести предпоследнюю строку указанного файла.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Гарантируется, что файл содержит хотя бы две строки.

Примечание 3. Не забудьте закрыть файл 🙂.
"""

# file_name = input()
# file = open(file_name, 'r', encoding='utf-8')
# content = file.readlines()
# print(content[-2].rstrip())
# file.close()

# with open(input()) as f:
#     print(f.readlines()[-2])

"""
Случайная строка
Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную строку из этого файла.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести случайную строку указанного файла.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Гарантируется, что файл содержит хотя бы одну строку.

Примечание 3. Не забудьте закрыть файл 🙂.

Примечание 4. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/519125/lines.txt
"""

# with open(lines.txt, 'x', encoding='utf-8') as f:
#     print(f.readlines()[-2])

# from random import choice

# # file_name = r"StepikPython\\Python_Generation_for_advanced\\lines.txt"
# file_name = 'lines.txt'
# file = open(file_name, 'r', encoding='utf-8')
# content = file.readlines()
# print(choice(content))
# file.close()

"""
Сумма двух-1
Вам доступен текстовый файл numbers.txt из двух строк, на 
каждой из них записано целое число. Напишите программу, 
выводящую на экран сумму этих чисел.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму чисел из указанного файла.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Не забудьте закрыть файл 🙂.

Примечание 3. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/519125/numbers.txt

"""

# file_name = r"StepikPython\\Python_Generation_for_advanced\\numbers.txt"
# # file_name = 'numbers.txt'
# with open(file_name, 'r', encoding='utf-8') as f:
#     print(sum(list((int(s) for s in f.readlines()))))

"""
Сумма двух-2
Вам доступен текстовый файл nums.txt. В файле записано два целых числа, 
они могут быть разделены символами пробела и конца строки. 
Напишите программу, выводящую на экран сумму этих чисел.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму чисел из указанного файла.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Не забудьте закрыть файл 🙂.

Примечание 3. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/519125/nums.txt
"""

# file_name = r"StepikPython\\Python_Generation_for_advanced\\nums.txt"
# # file_name = 'nums.txt'
# with open(file_name, 'r', encoding='utf-8') as f:
#     # print(f.readlines())
#     # print(sum(list((int(s)) for s in f.readlines() if s.strip().isdigit())))
#     print(sum(map(int, f.read().split())))

"""
Общая стоимость
Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина. 
В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:

наименование товара;
количество товара (целое число);
цена (в рублях) товара за 11 шт (целое число).
Напишите программу, выводящую на экран общую стоимость заказа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести общую стоимость заказа.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Не забудьте закрыть файл 🙂.

Примечание 3. Указанный файл можно скачать по ссылке.
"""

# # file_name = r"StepikPython\\Python_Generation_for_advanced\\prices.txt"
# file_name = 'prices.txt'
# with open(file_name, 'r', encoding='utf-8') as f:
#     # print(f.readlines())
#     # check = list(s.split() for s in f.readlines())
#     print(sum(list(int(n[1]) * int(n[2]) for n in list(s.split() for s in f.readlines()))))
#     # print(sum(map(int, f.read().split())))

# file = open('prices.txt')
# lines = map(str.split, file)
# print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
# file.close()

# with open("input.txt", encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')


# text = '''pop
# goes
# the
# weasel!'''

# with open('input.txt', 'w') as f:
#     f.write(text)

# with open('input.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')

"""
Переворот строки
Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку в обратном порядке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строку указанного файла в обратном порядке.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂.

Примечание 3. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/530408/text.txt


"""

# with open('text.txt') as f:
#     S = list(s for s in f)
#     print(*S[0][::-1], sep="")

"""
Обратный порядок
Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу, выводящую все строки данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строки указанного файла в обратном порядке.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂.

Примечание 3. Получить список всех строк файла можно при помощи метода readlines().

Примечание 4. Не забывайте про символ конца строки '\n'.

Примечание 5. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/530408/data.txt
"""

# with open('data.txt', encoding='utf-8') as f:
#     print(*reversed(list(d.rstrip() for d in f)), sep= '\n')

"""
Длинные строки
Вам доступен текстовый файл lines.txt, в котором записаны строки текста. 
Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂.

Примечание 3. Если бы файл lines.txt содержал строки:

One
Twenty one
Two
Twenty two
то результатом будет:

Twenty one
Twenty two
Примечание 4. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/530408/lines.txt

"""
# with open('lines.txt', encoding='utf-8') as f:
#     S = list(s.rstrip() for s in f)
#     result = list(s for s in S if len(s) == len(sorted(S, key=len)[-1],))
#     print(*result, sep='\n')

"""
Сумма чисел в строках
Вам доступен текстовый файл numbers.txt, каждая строка которого может 
содержать одно или несколько целых чисел, разделенных одним или несколькими пробелами.

Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит 
эту сумму на экран (для каждой строки выводится сумма чисел в этой строке).

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму чисел в каждой строке.

Примечание 1. Если бы файл numbers.txt содержал строки:

2 1
     3    4
 1       7
то результатом было бы:

3
7
8
Примечание 2. Указанный файл можно скачать по ссылке. 
"""

# with open('numbers.txt', encoding='utf-8' ) as f:
#     print(*list((sum(map(int, s.split())) for s in list(f))), sep='\n')

# with open('numbers.txt', 'r', encoding='utf-8') as file:
#     [print(sum(map(int, i.split()))) for i in file.readlines()]

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

"""
Статистика по файлу
Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести три найденных числа в формате, приведенном в примере.

Примечание 1. Если бы файл file.txt содержал строки:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
то результатом было бы:

Input file contains:
108 letters 
20 words 
4 lines 
Примечание 2. Словом называется последовательность из непробельных символов. Например, строка

abc a21 67pop    qwert bo7ok 83456
содержит 66 слов: abc, a21, 67pop, qwert, bo7ok, 83456.

Примечание 3. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/530408/file.txt
"""
# from itertools import chain

# with open('file.txt', encoding='utf-8') as file:
#     lines = list(([string for string in file]))
#     lines_count = len(lines)
#     words = list(chain(*list(string.split() for string in lines)))
#     words_count = len(words)
#     letters = list(letter for letter in chain(*list(list(word) for word in words)) if letter.isalpha())
#     letters_count = len(letters)
#     print(f"Input file contains:\n{letters_count} letters\n{words_count} words\n{lines_count} lines")
   
# with open('lines.txt') as f:
#     txt = f.read()
#     print('Input file contains:')
#     print(sum(map(str.isalpha, txt)), 'letters')
#     print(len(txt.split()), 'words')
#     print(txt.count('\n') + 1, 'lines')

"""
Random name and surname
Вам доступны два текстовых файла first_names.txt и last_names.txt,
один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля 
random создает 3 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.

Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:

Aaron
Abdul
Abe
Abel
Abraham
Albert
и

Abramson
Adamson
Adderiy
Addington
Adrian
Albertson
Einstein
то результатом могло быть:

Abdul Albertson
Abel Adamson
Albert Einstein
Примечание 2. Указанные файлы можно скачать по ссылкам (имена, фамилии). 
https://stepik.org/media/attachments/lesson/530408/first_names.txt
https://stepik.org/media/attachments/lesson/530408/last_names.txt

"""
# from random import choice

# with open('first_names.txt') as f1, open('last_names.txt') as f2:
#     S1 = list(s.strip() for s in f1)
#     S2 = list(s.strip() for s in f2)
# for _ in range(3):
#     print(choice(S1), choice(S2))

"""
Необычные страны
Вам доступен текстовый файл population.txt с названиями стран 
и численностью их населения, разделенными символом табуляции '\t'.

Напишите программу выводящую все страны, название которых 
начинается с буквы 'G', численность населения которых больше 
чем 500 000 человек, не меняя их порядок.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести названия стран, удовлетворяющие условиям задачи,
каждое на отдельное строке.

Примечание. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/530408/population.txt
"""

# with open('population.txt') as f:
#     S = list(s.strip().split('\t') for s in f)
# # print(*filter(lambda x: x[0][0] == 'G' and int(x[1]) > 500000, S), sep='\n')
# print(*list(a for a, b in S if a[0] == 'G' and int(b) > 500000), sep='\n')

"""
CSV-файл
Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. 
Напишите функцию read_csv для чтения данных из этого файла. 
Она должна возвращать список словарей, интерпретируя 
первую строку как имена ключей, а каждую последующую 
строку как значения этих ключей.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна содержать реализованную функцию read_csv.

Примечание 1. Вызывать функцию read_csv не нужно.

Примечание 2. Функция read_csv не должна принимать аргументов. 

Примечание 2. Подробнее прочитать про CSV-файлы можно тут.

Примечание 3. Считайте, что все ключи и значения по этим ключам в 
результирующем словаре имеют строковый тип (str).

Примечание 4. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/530408/data.csv

Примечание 5. Если бы файл data.csv содержал информацию

name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
то вызов функции read_csv() вернул бы список:

[{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'},
{'name': 'John', 'address': '54 Love Ave', 'age': '21'}]
"""
# def read_csv():
#     with open('data.csv') as f:
#         S = list(s.strip().split(',') for s in f)
#     result = []
#     for i in range(1, len(S)):
#         result.append(dict(zip(S[0], S[i])))
#     return result

# def read_csv():
#     with open('data.csv') as file:
#         keys = file.readline().strip().split(',')
#         return [dict(zip(keys, line.strip().split(','))) for line in file]

# with open('words.txt', 'w') as file:
#     file.write('delphi+')
#     file.write('java')

# with open('names.txt', 'a') as file:
#     file.write('\n')
#     file.write('Michael\n')
#     file.write('Alexander')

# with open('artists.txt', 'r+') as file:
#     file.write('Mick Jagger\n')
#     file.write('Ace Canon\n')

# with open('words.txt', 'w') as output:
#     print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
#     print('python', file=output)

# with open('beegeek.txt', 'w', encoding='utf-8') as file:
#     file.writelines(['Добро пожаловать в Beegeek!\n', 'Наши курсы самые лучшие! '])
#     file.write('Позвоните нам: (916) 928-92xx')


"""
Входная строка
Напишите программу, которая считывает строку текста и записывает 
её в текстовый файл output.txt.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна создать файл с именем output.txt и 
записать в него считанную строку текста.

Примечание. Считайте, что исполняемая программа и 
указанный файл находятся в одной папке.
"""

# with open('output.txt', 'w', encoding='utf-8') as output:
#     print(input(), file=output)


"""
Случайные числа
Напишите программу, записывающую в текстовый файл random.txt 25
 случайных чисел в диапазоне от 111 до 777 (включительно), 
 каждое с новой строки.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем random.txt и 
записать в него случайные числа в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Для генерации случайных чисел используйте модуль random.
"""
# from random import randint
# with open('random.txt', 'w', encoding='utf-8') as output:
#     print(*list(randint(111, 777) for _ in range(25)), sep='\n', file=output)

# import random
# print(*[str(random.randint(111, 777)) + '\n' for _ in range(25)], sep='', file = open('random.txt', 'w'))

"""
Нумерация строк
Вам доступен текстовый файл input.txt, состоящий из нескольких строк. 
Напишите программу для записи содержимого этого файла в файл output.txt
в виде нумерованного списка, где перед каждой строкой стоит ее номер, 
символ ) и пробел. Нумерация строк должна начинаться с 1.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt и 
записать в него пронумерованные строки файла input.txt.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Используйте встроенную функцию enumerate().

Примечание 3. Если бы файл input.txt содержал строки:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
то файл output.txt имел бы вид:

1) Beautiful is better than ugly.
2) Explicit is better than implicit.
3) Simple is better than complex.
4) Complex is better than complicated.
Примечание 4. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/519126/input.txt
"""

# from itertools import count
# with open('input.txt', 'r', encoding='utf-8') as f, open('output.txt', 'w', encoding='utf-8') as output:
#     S = dict(zip(count(1), map(lambda x: x.strip(), f)))
#     [print(f"{k}) {v}", file=output) for k, v in S.items()]


# with open('input.txt') as inp, open('output.txt', 'w') as out:
#     for i, j in enumerate(inp, start=1):
#         print(f'{i}) {j}', end='', file=out)

"""
Подарок на новый год
Вам доступен текстовый файл class_scores.txt с оценками за 
итоговый тест на строках вида: 
фамилия оценка (фамилия и оценка разделены пробелом). 
Оценка - целое число от 0 до 100 включительно.

Напишите программу для добавления 5 баллов к каждому
результату теста и вывода фамилий и новых результатов 
тестов в файл new_scores.txt.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Если бы файл class_scores.txt содержал строки:

Washington 83
Adams 86
Kingsman 100
MacDonald 95
Thomson 98
то файл new_scores.txt имел бы вид:

Washington 88
Adams 91
Kingsman 100
MacDonald 100
Thomson 100
Примечание 3. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/519126/class_scores.txt
"""

# with open('class_scores.txt', encoding='utf-8') as inp, open('new_scores.txt', 'w', encoding='utf-8') as out:
#     S = list(map(lambda x: x.strip().split(), inp))
#     for s in S:
#         print(*(s[0], 100) if int(s[1]) + 5 >= 100 else (s[0], (int(s[1]) + 5)), file=out)
        
"""
Загадка от Жака Фреско 🌶️
Однажды Жака Фреско спросили:

"Если ты такой умный, почему не богатый?"

Жак не стал отвечать на столь провокационный вопрос, 
вместо этого он задал загадку спрашивающему:

"Были разноцветные козлы. Сколько?"
"Сколько чего?"
"Сколько из них составляет более 7% от общего количества козлов?"

Вам доступен текстовый файл goats.txt 
в первой строке которого написано слово COLOURS, 
далее идет список всех возможных цветов козлов. 
Затем идет строка со словом GOATS, и 
далее непосредственно перечисление козлов разных цветов. 
Перечень козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода 
в него списка козлов, которые удовлетворяют условию 
загадки от Жака Фреско.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем answer.txt и 
вывести в него в алфавитном порядке названия цветов козлов, 
которые удовлетворяют условию загадки Жака Фреско.

Примечание 1. Считайте, что исполняемая программа и 
указанные файлы находятся в одной папке.

Примечание 2. Если бы файл goats.txt содержал строки:

COLOURS
Pink goat
Green goat
Black goat
GOATS
Pink goat
Pink goat
Black goat
Pink goat
Pink goat
Black goat
Green goat
Pink goat
Black goat
Black goat
Pink goat
Pink goat
Black goat
Black goat
Pink goat
то файл answer.txt имел бы вид:

Black goat
Pink goat
Примечание 3. Указанный файл можно скачать по ссылке. 
https://stepik.org/media/attachments/lesson/519126/goats.txt
"""

# with open('goats.txt', encoding='utf-8') as inp, open('answer.txt', 'w', encoding='utf-8') as out:
#     S = list(s.strip() for s in inp)
#     key = list(S[1:S.index('GOATS')])
#     result = dict(((k, S.count(k) - 1)) for k in key)
#     print(*sorted(k for k, v in result.items() if int(v) / (len(S) - len(key) - 2) > 0.07), sep = '\n', file=out)

"""
Конкатенация файлов 🌶️
На вход программе подается натуральное число n и 
n строк с названиями файлов. 
Напишите программу, которая создает файл output.txt 
и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

Формат входных данных
На вход программе подается натуральное число n и n строк названий существующих файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
"""
# files = list(input() for _ in range(int(input())))
# with open('output.txt', 'a', encoding='utf-8') as out:
#     for file in files:
#         with open(file, encoding='utf-8') as inp:
#             S = inp.read()
#             out.write(S)

"""
Лог файл 🌶️
Вам доступен текстовый файл logfile.txt с информацией о времени входа 
пользователя в систему и выхода из нее. Каждая строка файла содержит 
три значения, разделенные запятыми и символом пробела: имя пользователя, 
время входа, время выхода, где время указано в 24-часовом формате.

Напишите программу, которая создает файл output.txt и выводит в него 
имена всех пользователей (не меняя порядка следования), которые были в 
сети не менее часа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Считайте, что каждый пользователь был только раз в системе, 
то есть в файле нет двух строк с одинаковым пользователем.

Примечание 3. Если бы файл logfile.txt содержал строки:

Тимур Гуев, 14:10, 15:50
Руслан Гриценко, 12:00, 12:59
Роман Гацалов, 09:10, 17:45
Габолаев Георгий, 11:10, 12:10
то файл output.txt имел бы вид:

Тимур Гуев
Роман Гацалов
Габолаев Георгий
Примечание 4. Указанный файл можно скачать по ссылке.
https://stepik.org/media/attachments/lesson/519126/logfile.txt
"""

# def minutes(x):
#     res = [int(i) for i in x.split(':')]
#     return res[0]*60 + res[1]

# with open('logfile.txt', encoding='utf-8') as inp,\
#      open('output.txt', 'w', encoding='utf-8') as out:
#     S = list(s.strip().split(', ') for s in inp)
#     result = list(s[0] for s in S if (minutes(s[2]) - minutes(s[1]) >= 60))
#     print(*result,sep='\n', file=out)