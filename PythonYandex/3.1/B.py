"""
Кручу-верчу
Очень часто в текстовых редакторах требуется траспонировать (повернуть) текст.
К сожалению, в Python такая функция по-умолчанию отсутствует. 
Давайте создадим программу, которая преобразует введённую 
стоку из горизонтальной записи в вертикальную.

Формат ввода
Одна строка.

Формат вывода
Вертикальное представление введённой строки.

Пример 1
Ввод
Привет
Вывод
П
р
и
в
е
т
Пример 2
Ввод
Питон
Вывод
П
и
т
о
н
"""

string = input()

for i in range(len(string)):
    print(string[i])
