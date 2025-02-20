"""
НОК
Спустя время НИИ потребовалось находить наименьшее общее кратное (НОК) двух чисел.
К нам вновь обратились за помощью.

Формат ввода
Вводится два натуральных числа, каждое на своей строке.

Формат вывода
Требуется вывести одно натуральное число — НОК двух данных чисел.

Пример 1
Ввод
12
42
Вывод
84
Пример 2
Ввод
512
625
Вывод
320000
"""

num1, num2 = ar1, ar2 = int(input()), int(input())

while num1 != 0 and num2 != 0:
    if num1 >= num2:
        num1 %= num2
    else:
        num2 %= num1

result = (ar1 * ar2) / (num1 + num2)

print(int(result))