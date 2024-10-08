"""
Не таблица умножения
Фабрика вернулась с новой задачкой — другим вариантом таблицы умножения.
Она нужна в виде списка. Продолжим помогать местному бизнесу.

Формат ввода
Вводится одно натуральное число — требуемый размер «таблицы».

Формат вывода
Не таблица умножения заданного размера.

Пример 1
Ввод
3
Вывод
1 * 1 = 1
2 * 1 = 2
3 * 1 = 3
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
Пример 2
Ввод
5
Вывод
1 * 1 = 1
2 * 1 = 2
3 * 1 = 3
4 * 1 = 4
5 * 1 = 5
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
4 * 2 = 8
5 * 2 = 10
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
4 * 3 = 12
5 * 3 = 15
1 * 4 = 4
2 * 4 = 8
3 * 4 = 12
4 * 4 = 16
5 * 4 = 20
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
"""
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{j} * {i} = {i * j}")
