"""
Очистка данных
Местный провайдер собирает большое количество логов, однако 
зачастую файлы с отчётами приходят в негодность.
Самые частые проблемы — ошибки вида ## и @@@.
Напишите программу, которая избавляется от:

Двух символов # в начале информационных сообщений;
Строк, заканчивающихся тремя символами @.

Формат ввода

Вводятся строки отчёта. Признаком завершения ввода считается
пустая строка.

Формат вывода
Очищенные данные.

Пример 1
Ввод
Hello, world
Hello, @@@
##Goodbye

Вывод
Hello, world
Goodbye
Пример 2
Ввод
First Message
##Second Message
@@@Third Message##
##Fourth Message@@@

Вывод
First Message
Second Message
@@@Third Message##
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
    if i.startswith("##") and not i.endswith("@@@"):
        result.append(i.lstrip("#"))
    elif not i.endswith("@@@"):
        result.append(i)
print(*result, sep='\n')
