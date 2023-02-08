"""
А роза упала на лапу Азора 3.0
Вернёмся к палиндромам. Напишите программу, которая 
определяет количество палиндромов в переданном списке.

Формат ввода
В первой строке записано число N Во всех последующих 
N строках указано по одному числу.

Формат вывода
Требуется вывести общее количество палиндромов среди введённых чисел
(кроме числа N).

Пример 1
Ввод
5
1
2
3
4
5
Вывод
5
Пример 2
Ввод
3
123
454
321
Вывод
1
"""

"""
def is_palindrome(n):
    N = []
    while n > 0:
        N.append(n % 10)
        n //= 10
    for i in range(int(len(N) / 2)):
        if N[i] != N[len(N) - i - 1]:
            return False
    return True


n = int(input())
counter = 0
for i in range(n):
    k = int(input())
    if is_palindrome(k):
        counter += 1

print(counter)
"""

number = int(input())
counter = 0
for i in range(number):
    temp = input()
    rev = reversed(temp)
    if list(temp) == list(rev):
        counter += 1
print(counter)

