"""
Простая задача 2.0
В банке решили переписать программу для шифрования данных и попросили, чтобы 
вы взяли на себя часть данной задачи. 
Напишите программу для разложения числа на простые множители. 
Только внимательно, ведь работать придётся вновь с простыми числами.

Формат ввода
Вводится одно натуральное число.

Формат вывода
Требуется составить математическое выражение — произведение простых неубывающих чисел, 
которое в результате даёт исходное.

Пример 1
Ввод
120
Вывод
2 * 2 * 2 * 3 * 5
Пример 2
Ввод
98
Вывод
2 * 7 * 7
"""


def is_prime_number(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        for i in range(3, int((n ** 0.5) + 1), 2):
            if (n % i == 0):
                return False
        return True


def prime_factorization(n):
    result = []
    while n > 1:
        for i in range(2, int((n + 1) / 2)):
            if is_prime_number(i):
                while n % i == 0:
                    result.append(i)
                    n /= i
    return result


n = int(input())
print(*prime_factorization(n), sep=" * ")