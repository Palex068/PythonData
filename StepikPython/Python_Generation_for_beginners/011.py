"""
Список чисел
На вход программе подается одно число n. Напишите программу, которая выводит список [1, 2, 3, ..., n].

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
# print(list(i for i in range(1, int(input()) + 1)))

"""
Список букв
На вход программе подается одно число nn. Напишите программу, 
которая выводит список, состоящий из nn букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

Формат входных данных
На вход программе подается натуральное число n ≤ 26.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""

# D = list("abcdefghijklmnopqrstuvwxyz")
# result = list()

# for i in range(int(input())):
#     result.append(D[i])
# print(result)

"""
Дополните приведенный код, используя индексатор, так чтобы он вывел 17-ый элемент списка primes.
"""
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[16])

"""
Дополните приведенный код, используя индексатор, так чтобы он вывел последний элемент списка primes.
"""
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[-1])

"""
Дополните приведенный код, используя срезы, так чтобы он вывел первые 6 элементов списка primes.

Примечание. Результатом вывода должна быть строка [2, 3, 5, 7, 11, 13].
"""

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[:6])

"""
Дополните приведенный код, так чтобы он вывел сумму минимального и максимального элементов списка numbers.
"""

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

# print(max(numbers) + min(numbers))

"""
Дополните приведенный код так, чтобы он вывел среднее арифметическое элементов списка evens.
"""

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / len(evens)

# print(average)

"""
Дополните приведенный код так, чтобы элемент списка имеющий значение Green заменился на значение Зеленый,
а элемент Violet на Фиолетовый. Далее необходимо вывести полученный список.
"""
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[rainbow.index('Green')] = 'Зеленый'
# rainbow[rainbow.index('Violet')] = 'Фиолетовый'

# print(rainbow)

"""
Дополните приведенный код так, чтобы он вывел элементы списка languages в обратном порядке.

Примечание. Для вывода списка воспользуйтесь функцией print().
"""
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

# print(languages[::-1])

"""
Дополните приведенный код, используя операторы конкатенации (+) и умножения списка на число (*), так чтобы он вывел список:

[1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13].
"""

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]

# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# numbers = [4, 2]
# numbers.extend([1, 2, 3])
# numbers.extend([7, 17, 777])
# print(numbers)

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'magenta']
# del colors[2]
# del colors[6]
# print(colors)

"""
Все сразу 1 🌶️
Дополните приведенный код, чтобы он:

1. Вывел длину списка;
2. Вывел последний элемент списка;
3. Вывел список в обратном порядке (вспоминаем срезы);
4. Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
5. Вывел список с удаленным первым и последним элементами.

Примечание. Каждый вывод осуществлять с новой строки.
"""
# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1,
#             0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0,
#               0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14,
#                 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

# # Вывел длину списка;
# print(len(numbers))
# # Вывел последний элемент списка;
# print(numbers[-1])
# # Вывел список в обратном порядке (вспоминаем срезы);
# print(numbers[::-1])
# # Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
# print("YES" if 5 in numbers and 17 in numbers else "NO")
# # Вывел список с удаленным первым и последним элементами.
# print(numbers[1:-1:])

"""
Список строк
На вход программе подается натуральное число n, а затем n строк. 
Напишите программу, которая создает из указанных строк список и выводит его.

Формат входных данных
На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести список состоящий из указанных строк.
"""

# print(list(input() for _ in range(int(input()))))

"""
Алфавит
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Формат выходных данных
Программа должна вывести указанный список.

Примечание. Последний элемент списка состоит из 26 символов z.
"""

# D = list("abcdefghijklmnopqrstuvwxyz")

# print(list((D[i] * (i + 1) for i in range(len(D)))))

"""
Список кубов
На вход программе подается натуральное число n, 
а затем n целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список, состоящий из кубов указанных чисел.
"""
# print(list(int(input()) ** 3 for _ in range(int(input()))))

"""
Список делителей
На вход программе подается натуральное число n. 
Напишите программу, которая создает список состоящий из делителей введенного числа.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести список, состоящий из делителей введенного числа.
"""

# n = int(input())
# N = list()
# for i in range(1, n + 1):
#     if n % i == 0:
#         N.append(i)
# print(N)

"""
Суммы двух
На вход программе подается натуральное число n (n ≥ 2), 
а затем n целых чисел. Напишите программу, которая создает 
из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список, состоящий из сумм соседних чисел.
"""

# N = list(int(input()) for _ in range(int(input())))
# result = list()

# for i in range(len(N) - 1):
#     result.append(N[i] + N[i + 1])
# print(result)

"""
Удалите нечетные индексы
На вход программе подается натуральное число n, а затем n целых чисел. 
Напишите программу, которая создает из указанных чисел список, затем 
удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список в соответствии с условием задачи.

Примечание. Используйте оператор del.
"""

# N = list(int(input()) for _ in range(int(input())))
# del N[1::2]
# print(N)

"""
k-ая буква слова 🌶️🌶️
На вход программе подается натуральное число n и n строк, а затем число k. 
Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

Формат входных данных
На вход программе подается натуральное число n,  далее n строк, каждая на отдельной строке. 
В конце вводится натуральное число k – номер буквы (нумерация начинается с единицы).

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, 
то такие строки при выводе нужно игнорировать.
"""
# S = list(input() for _ in range(int(input())))
# k = int(input())
# result = list()
# for s in S:
#     if len(s) < k + 1:
#         pass
#     else:
#         result.append(s[k - 1])
# print(*result, sep= '')

"""
Символы всех строк
На вход программе подается натуральное число n, а затем n строк. 
Напишите программу, которая создает список из символов всех строк, а затем выводит его.

Формат входных данных
На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести список состоящий из символов всех введенных строк.

Примечание. В результирующем списке могут содержаться одинаковые символы.
"""
# S = list()
# for _ in range(int(input())):
#     S.extend(input())
# print(S)

"""
Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.
"""
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

# print(sum(i ** 2 for i in numbers))

"""
Значение функции
На вход программе подается натуральное число n, а затем n целых чисел. 
Напишите программу, которая для каждого введенного числа xx выводит значение функции f(x) = x^2 + 2x + 1, 
каждое на отдельной строке.

Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции.
"""
# N = list(int(input()) for _ in range(int(input())))
# print(*N, sep = '\n')
# print()
# print(*list(i ** 2 + 2 * i + 1 for i in N), sep= '\n')

"""
Remove outliers
При анализе данных, собранных в рамках научного эксперимента, 
бывает полезно удалить самое большое и самое маленькое значение.

На вход программе подается натуральное число n, а 
затем n различных натуральных чисел. 
Напишите программу, которая удаляет наименьшее и наибольшее
значение из указанных чисел, а затем выводит оставшиеся числа 
каждое на отдельной строке, не меняя их порядок.

Формат входных данных
На вход программе подаются натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""

# N = list(int(input()) for _ in range(int(input())))
# n = N.index(max(N))
# del N[n]
# n = N.index(min(N))
# del N[n]
# print(*N, sep= '\n')

"""
Без дубликатов
На вход программе подается натуральное число n, а затем n строк. 
Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число n, а затем nn строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Считайте, что все строки состоят из строчных символов.
"""
# S = list(input() for _ in range(int(input())))

# result = list()
# for s in S:
#     if s not in result:
#         result.append(s)
# print(*result, sep= '\n')

"""
Google search - 1
На вход программе подается натуральное число n, затем n строк, 
затем еще одна строка — поисковый запрос. 
Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

Формат входных данных
На вход программе подаются натуральное число n — количество строк, 
затем сами строки в указанном количестве, затем один поисковый запрос.

Формат выходных данных
Программа должна вывести все введенные строки, в которых встречается поисковый запрос.

Примечание. Поиск не должен быть чувствителен к регистру символов.
"""

# S, search = list(input() for _ in range(int(input()))), input()

# for s in S:
#     if search.lower() in s.lower():
#         print(s, end= '\n')

"""
Google search - 2 🌶️🌶️
На вход программе подается натуральное число n, затем n строк, 
затем число k — количество поисковых запросов, затем k строк — поисковые запросы. 
Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

Формат входных данных
На вход программе подаются натуральное число n — количество строк, 
затем сами строки в указанном количестве, затем число k, затем сами поисковые запросы.

Формат выходных данных
Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.

Примечание. Поиск не должен быть чувствителен к регистру символов.
"""
# S = list(input() for _ in range(int(input())))
# k = int(input())
# Sh = list(input() for _ in range(k))
# result = list()
# for sh in Sh:
#     for s in S:
#         if sh.lower() in s.lower():
#             result.append(s)
# to_print = list()
# for r in result:
#     if result.count(r) == k and r not in to_print:
#         to_print.append(r)
# print(*to_print, sep= '\n')

# s = [input() for _ in range(int(input()))]
# d = [input() for _ in range(int(input()))]
# for i in s:
#     for j in d:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)

# s = [input() for _ in range(int(input()))]
# k = [input() for _ in range(int(input()))]
# for i in s:
#     count = 0
#     for j in k:
#         if j.lower() in i.lower():
#             count += 1
#             if count == len(k):
#                 print(i)

# s = [input() for i in range(int(input()))]
# k = [input() for j in range(int(input()))]
# for i in s:
#   flag = True
#   for j in k:
#     if j.lower() not in i.lower():
#       flag = False
#   if flag == True:
#     print(i)

"""
Negatives, Zeros and Positives
На вход программе подается натуральное число n, а затем n целых чисел. 
Напишите программу, которая сначала выводит все отрицательные числа, 
затем нули, а затем все положительные числа, каждое на отдельной строке. 
Числа должны быть выведены в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

"""

# N = list(int(input()) for _ in range(int(input())))

# Negatives, Zeros, Positives = [], [], []

# for n in N:
#     if n < 0:
#         Negatives.append(n)
#     elif n == 0:
#         Zeros.append(n)
#     else:
#         Positives.append(n)
# result = Negatives + Zeros + Positives
# print(*result, sep= '\n')

# s = [int(input()) for _ in range(int(input()))]
# for i in range(3):
#     for c in s:
#         if (c < 0, c == 0, c > 0)[i]:
#             print(c)

# print(*sorted([int(input()) for _ in range(int(input()))], key=lambda x: (x > 0, x == 0, x < 0)), sep='\n')

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

"""
Построчный вывод
На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""

# print(*input().split(), sep= '\n')

"""
Инициалы
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. 
Напишите программу, которая выводит инициалы человека.

Формат входных данных
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
# S = list(input().split())
# result = []
# for s in S:
#     result.append(s[0].upper() + '.')
# print(*result, sep='')

"""
Windows OS
В операционной системе Windows полное имя файла состоит из буквы диска, 
после которого ставится двоеточие и символ  "\",  затем через такой же символ перечисляются подкаталоги (папки), 
в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).

На вход программе подается одна строка с корректным именем файла в операционной системе Windows. 
Напишите программу, которая разбирает строку на части, разделенные символом "\". 
Каждую часть вывести в отдельной строке.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
# print(*list(input().split('\\')), sep= '\n')

# print(*(input().split(chr(92))),sep='\n')

"""
Диаграмма
На вход программе подается строка текста, содержащая целые числа. 
Напишите программу, которая по заданным числам строит столбчатую диаграмму.

Формат входных данных
На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.

Формат выходных данных
Программа должна вывести столбчатую диаграмму.
"""
# print(*list('+' * i for i in list(map(int, input().split()))), sep= '\n')

"""
Корректный ip-адрес
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. 
Напишите программу, которая определяет является ли введенная строка текста корректным ip-адресом.

Формат входных данных
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.

Формат выходных данных
Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.

Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.
"""

# print("ДА" if sum(list(1 for i in list(map(int, input().split('.'))) if 0 <= i <= 255)) == 4 else "НЕТ")

"""
Добавь разделитель
На вход программе подается строка текста и строка разделитель. 
Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.

Формат входных данных
На вход программе подается строка текста и строка разделитель, каждая на отдельной строке

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
# S, r = list(input()), input()
# print(r.join(S))

# print(*list(input()), sep=input())

"""
Количество совпадающих пар
На вход программе подается строка текста, содержащая натуральные числа. 
Из данной строки формируется список чисел. 
Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, 
равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести одно число – количество пар элементов, равных друг другу.
"""

# N, counter = list(map(int, input().split())), 0

# for i in range(len(N) - 1):
#     for j in range(i + 1, len(N)):
#         if N[i] == N[j]:
#             counter += 1
# print(counter)

# a = input().split()
# s = 0
# for i in range(len(a) - 1):
#     s += a[i + 1:].count(a[i])
# print(s)

"""
Все сразу 2 🌶️
Дополните приведенный код, чтобы он:

Заменил второй элемент списка на 17;
Добавил числа 4, 5 и 6 в конец списка;
Удалил первый элемент списка;
Удвоил список;
Вставил число 25 по индексу 3;
Вывел список, с помощью функции print()
"""

# numbers = [8, 9, 10, 11]

# # Заменил второй элемент списка на 17;
# numbers[1] = 17
# # Добавил числа 4, 5 и 6 в конец списка;
# numbers.extend([4, 5, 6])
# # Удалил первый элемент списка;
# del numbers[0]
# # Удвоил список;
# numbers *= 2
# # Вставил число 25 по индексу 3;
# numbers.insert(3, 25)
# print(numbers)

"""
Переставить min и max
На вход программе подается строка текста, содержащая различные натуральные числа. 
Из данной строки формируется список чисел. 
Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

Формат входных данных
На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести строку текста в соответствии с условием задачи.

Примечание. Используйте подходящие встроенные функции и списочные методы.
"""

# N = list(map(int, input().split()))
# min_index = N.index(min(N))
# max_index = N.index(max(N))
# N[min_index], N[max_index] = N[max_index], N[min_index]
# print(*N)

"""
Количество артиклей
На вход программе подается строка, содержащая английский текст. 
Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

Формат входных данных
На вход программе подается строка, содержащая английский текст. Слова текста разделены символом пробела.

Формат выходных данных
Программа должна вывести общее количество артиклей 'a', 'an', 'the' вместе с поясняющим текстом.

Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.
"""

# S, count = list(input().split()), 0
# for s in S:
#     for a in ['a', 'an', 'the']:
#         if s.lower() == a:
#             count += 1
# print("Общее количество артиклей: " + str(count))

"""
злом Братства Стали 🌶️
Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали, 
и любезно соглашается помочь им в решении их проблем. Одной из такой проблем являлся странный 
компьютерный вирус, который проявлялся в виде появления комментариев к программам на терминалах 
Братства Стали. Известно, что программисты Братства никогда не оставляют комментарии к коду, и 
пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им. 
Помогите писцу Ибсену удалить все комментарии из программы.

Формат входных данных
На первой строке вводится символ решётки и сразу же натуральное число n — количество строк в программе, не считая первой. 
Далее следует n строк кода.

Формат выходных данных
Нужно вывести те же строки, но удалить комментарии и символы пустого пространства в конце строк. 
Пустую строку вместо первой строки ввода выводить не надо.
"""

# N = list(input() for _ in range(int(input().lstrip("#"))))

# for i in range(len(N)):
#     if '#' in N[i]:
#        N[i] = N[i][:N[i].index('#')]
#     N[i] = N[i].rstrip(' ')
# print(*N, sep= '\n')

# numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
# numbers.sort()
# del numbers[0]
# del numbers[-1]
# numbers.sort(reverse=True)
# print(numbers)

"""
Сортировка чисел
На вход программе подается строка текста, содержащая целые числа. 
Из данной строки формируется список чисел. Напишите программу, 
которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию. 

Формат входных данных
На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести две строки текста в соответствии с условием задачи.
"""
# N = sorted(list(map(int, input().split())))
# print(N)
# print(N[::-1])

"""
Дополните приведенный код, используя списочное выражение так, 
чтобы получить новый список, содержащий строки исходного списка с удаленным первым символом.
"""

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [s[1:] for s in keywords]

# print(new_keywords)

"""
Дополните приведенный код, используя списочное выражение, 
так чтобы получить новый список, содержащий длины строк исходного списка.
"""

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# lengths = [len(s) for s in keywords] 

# print(lengths)

"""
Дополните приведенный код списочным выражением, чтобы получить новый список, 
содержащий только слова длиной не менее пяти символов (включительно).
"""

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [w for w in keywords if len(w) >= 5]

# print(new_keywords)

"""
Дополните приведенный код, используя списочное выражение, 
так чтобы получить список всех чисел палиндромов от 100 до 1000.
"""

# palindromes = [pal for pal in range(100, 1000) if str(pal) == str(pal)[::-1]]

# print(palindromes)

"""
Списочное выражение 1
На вход программе подается натуральное число n. 
Напишите программу, использующую списочное выражение, 
которая создает список содержащий квадраты чисел от 1 до n,
а затем выводит его элементы построчно, то есть каждый на отдельной строке.

Формат входных данных
На вход программе подается натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Для вывода элементов списка используйте цикл for.
"""
# print(*list(i ** 2 for i in range(1, int(input()) + 1)), sep= '\n')

"""
Списочное выражение 2
На вход программе подается строка текста, содержащая целые числа. 
Напишите программу, использующую списочное выражение, которая выведет 
кубы указанных чисел также на одной строке.

Формат входных данных
На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Для вывода элементов списка используйте цикл for.

Примечание 2. Используйте метод split().
"""

# print(*list(n ** 3 for n in list(map(int, input().split()))))

"""
В одну строку 1
На вход программе подается строка текста, содержащая слова. 
Напишите программу, которая выводит слова введенной строки в столбик.

Формат входных данных
На вход программе подается строка текста, содержащая слова, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Программу можно написать в одну строку кода.
"""
# print(*list(s for s in list(input().split())), sep= '\n')

"""
В одну строку 2
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, 
которая выводит все цифровые символы данной строки.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Программу можно написать в одну строку кода.
"""

# print(*list(n for n in list(input()) if n in list('0123456789')), sep='')

# print(*(i for i in input() if i.isdigit()), sep="")

"""
В одну строку 3
На вход программе подается строка текста, содержащая целые числа. 
Напишите программу, использующую списочное выражение, которая выведет 
квадраты четных чисел, которые не оканчиваются на цифру 4.

Формат входных данных
На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Программу можно написать в одну строку кода.
"""

# print(*list(n ** 2 for n in list(map(int, list(input().split()))) if n % 2 == 0 and (n ** 2) % 10 != 4))

# print(*[int(i) ** 2 for i in input().split() if i[-1] in "046"])

"""
Оптимизируйте приведенный код, реализующий алгоритм пузырьковой сортировки.
"""
a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

# n = len(a)

# for i in range(n - 1):
#     flag = True
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = False
#     if flag:
#         break
# print(a)

# a.sort()
# print(a)

# s, b = len(a), []

# while s != 0:
#     b.append(min(a))
#     a.remove(b[-1])
#     s -=1
# print(b)
