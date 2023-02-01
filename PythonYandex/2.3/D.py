"""
Считалочка 2.0
Дети продолжают запоминать цифры, а мы им помогать.
Нам вновь называют начало и конец последовательности чисел, а мы выводим их и числа между.

Формат ввода
Два числа, каждое с новой строки.

Формат вывода
Все числа от начала до конца (включительно), записанные через пробел.

Пример 1
Ввод
1
10
Вывод
1 2 3 4 5 6 7 8 9 10
Пример 2
Ввод
3
-3
Вывод
3 2 1 0 -1 -2 -3
"""

first_number, last_number = int(input()), int(input())
result = []
if first_number >= last_number:
    for i in range(first_number, last_number - 1, -1):
        result.append(i)
else:        
    for i in range(first_number, last_number + 1):
        result.append(i)
print(*result)