"""
В ожидании доставки
Сегодня в NN часов MM минут хозяин магазина заказал доставку нового товара. Оператор сказал, что продукты доставят через TT минут.
Сколько будет времени на электронных часах, когда привезут долгожданные продукты?

Формат ввода
В первой строке записано натуральное число NN (0 \le N \lt 240≤N<24).
Во второй строке записано натуральное число MM (0 \le M \lt 600≤M<60).
В третьей строке записано натуральное число TT (30 \le T \lt 10^930≤T<10 
9
 ).

Формат вывода
Одна строка, представляющая циферблат электронных часов.

Пример 1
Ввод
8
0
65
Вывод
09:05
Пример 2
Ввод
10
15
2752
Вывод
08:07
"""
number_of_hours = int(input())
number_of_minutes = int(input())
number_of_minutes_of_delivery = int(input())

result_of_minutes = (number_of_minutes + number_of_minutes_of_delivery) % 60
result_of_hours = ((number_of_minutes + number_of_minutes_of_delivery) // 60 + number_of_hours) % 24

output_of_minutes = '0' * (2 - len(str(result_of_minutes))) + str(result_of_minutes)
output_of_hours = '0' * (2 - len(str(result_of_hours))) + str(result_of_hours)

print(f"{output_of_hours}:{output_of_minutes}")
