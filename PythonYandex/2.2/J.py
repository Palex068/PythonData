"""
Лучшая защита — шифрование
Коля испугался, что Аня подсмотрит все его пароли в блокноте, и 
решил их зашифровать. Для этого он берёт 
изначальный пароль — трёхзначное число — и 
по нему строит новое число по следующим правилам:

находится сумма цифр, стоящих в двух младших разрядах (десятки и единицы);
находится сумма цифр, стоящих в двух старших разрядах (сотни и десятки)
Эти две суммы, записанные друг за другом, в порядке не возрастания, 
формируют новое число.
Помогите реализовать алгоритм шифрования.

Формат ввода
Одно трёхзначное число

Формат вывода
Результат шифрования

Пример 1
Ввод
123
Вывод
53
Пример 2
Ввод
741
Вывод
115
"""

number = input()

n1 = int(number[0]) + int(number[1])
n2 = int(number[1]) + int(number[2])

if n1 > n2:
    result = str(n1) + str(n2)
    print(result)
else:
    result = str(n2) + str(n1)
    print(result)