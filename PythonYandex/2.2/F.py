"""
Сила прокрастинации
Вася любит полениться. Особенно ему нравится, 
когда в году появляется такой лишний денёк, которого обычно не бывает.
Напишите программу, которая поможет Васе определить,
удастся ли ему побездельничать в определённом году или нет.

Формат ввода
Одно число — год.

Формат вывода
Одно слово «YES» (удастся) или «NO» (не удастся).

Пример 1
Ввод
2022
Вывод
NO
Пример 2
Ввод
2020
Вывод
YES
"""

year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")