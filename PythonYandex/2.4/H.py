"""
Максимальная сумма
Ребята в детском саду снова играют с числами. 
И пусть числа они знают плохо, придумывать их они очень любят.
Они договорились, что будут называть числа по очереди и 
тот, кто назовёт число с наибольшей суммой цифр, 
будет считаться победителем. 
В качестве судьи они выбрали бедную воспитательницу, и 
она попросила нас о помощи. 
Напишите программу, которая определит победителя.

Формат ввода
В первой строке записано число N — количество детей в группе. 
Далее вводятся имя ребенка и его число (каждое на своей строке).

Формат вывода
Требуется вывести имя победителя.
Если два ребенка назвали числа с одинаковой суммой цифр, победителем должен быть признан тот, кто ходил позже.

Пример 1
Ввод
2
Аня
123
Боря
234
Вывод
Боря
Пример 2
Ввод
3
Аня
1234
Боря
234
Ваня
2323
Вывод
Ваня
"""


def digits_sum(number):
    count = 0
    while number > 0:
        count += number % 10
        number //= 10
    return count


def max_number_index(volumes):
    max_number = volumes[0]
    max_number_index = 0
    for i in range(len(volumes)):
        if volumes[i] >= max_number:
            max_number = volumes[i]
            max_number_index = i
    return max_number_index


n = int(input())
names = []
volumes = []

for i in range(n):
    names.append(input())
    volumes.append(digits_sum(int(input())))

result = names[max_number_index(volumes)]
print(result)
