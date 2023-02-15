"""
А роза упала на лапу Азора 4.0
Вернёмся к палиндромам — числам, словам и предложениям, 
которые читаются одинаково в оба направления.
Напишите программу, которая определяет, 
относится ли введённая строка к палиндромам.

Формат ввода
Вводится строка.

Формат вывода
Требуется вывести YES — если введенная 
строка является палиндромом, иначе – NO.

Пример 1
Ввод
мама
Вывод
NO
Пример 2
Ввод
анна
"""
"""
def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return False
    return True


string = input()
if is_palindrome:
    print("YES")
else:
    print("NO")
"""

string = input()
rev = reversed(string)
if list(string) == list(rev):
    print("YES")
else:
    print("NO")