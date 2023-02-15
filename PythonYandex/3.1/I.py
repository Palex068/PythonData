"""
Без комментариев
Мы надеемся, вы пишите комментарии к своему коду. 
Если так, то интерпретатор удаляет их перед тем, как выполнить код. 
Напишите программу, которая выполняет данную функцию за интерпретатор.

Формат ввода
Вводятся строки программы.
Признаком остановки является пустая строка.

Формат вывода
Каждую строку нужно очистить от комментариев.
А если комментарий — вся строка, то выводить её не надо.

Пример 1
Ввод
# Моя первая супер-пупер программа
print("What is your name?") #  Как тебя зовут?
name = input() #  Сохраняем имя
print(f"Hello, {name}!") #  Здороваемся# Конец моей супер-пупер программы

Вывод
print("What is your name?")
name = input()
print(f"Hello, {name}!")
Пример 2
Ввод
# Мой первый цикл
for i in range(10): # Считаем до 10
    print(i) # выводим число

Вывод
for i in range(10):
    print(i)
"""


def input_string_list():
    string_list = list()
    while True:
        string = input()
        if string == "":
            return string_list
        string_list.append(string)


string_list = input_string_list()

result = list()

for i in string_list:
    if i.startswith("#"):
        pass
    elif "#" in i:
        result.append(i[:i.index("#")])
    else:
        result.append(i)

print(*result, sep='\n')
