# from datetime import date

# my_date = date(2020, 15, 10)        

# print(my_date)

# from datetime import date

# my_date = date(2020, 6, 17)        
# my_date.replace(month=9, day=29)

# print(my_date)

# from datetime import date

# my_date = date(2020, 6, 17)        
# new_date = my_date.replace(month=9, day=29)

# print(new_date)

# import datetime

# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)

# from datetime import date

# dates = [date(2000, 12, 31), date(1999, 3, 8), date(1999, 2, 22)]

# max_date = max(dates)
# min_date = min(dates)

# print(max_date.year + min_date.day)

# from datetime import date

# dates = [date(2023, 1, 1), date(2020, 7, 20), date(2021, 9, 17), date(2022, 6, 10)]

# print(*sorted(dates, key=lambda d: d.day), sep=', ')

"""
Дополните приведенный ниже код, чтобы он вывел текущую дату в ISO формате (YYYY-MM-DD).
"""

# # импортируем тип date из модуля datetime
# from datetime import date
# creation_date = date.today()
# # выводим текущую дату
# print(creation_date)

"""
Ураган Эндрю, обрушившийся на Флориду 24 августа 1992 года, 
был одним из самых дорогостоящих и смертоносных ураганов в истории США. 
Дополните приведенный ниже код, чтобы он вывел день недели (начиная с 0),
 в который ураган Эндрю достиг берегов США.

Примечание. Подробнее об урагане Эндрю можно почитать тут.
https://buildwiki.ru/wiki/Hurricane_Andrew
"""
# импортируем тип date из модуля datetime
# from datetime import date

# # создаем объект, соответсвующий дате урагана
# hurricane_andrew = date(1978, 6, 1)

# # выводим день недели
# print(hurricane_andrew.weekday())
# print(int(hurricane_andrew.strftime("%j").lstrip("0")))

"""
На Флориду с 1950 по 2017 год всего обрушилось 235 ураганов. 
В переменной florida_hurricane_dates хранится список дат, 
в которые произошел ураган. Сезон ураганов в Атлантике 
официально начинается 1 июня. Дополните приведенный ниже код,
чтобы он вывел количество ураганов с 1950 года, которые 
обрушились на Флориду до официального начала сезона ураганов.

Примечание 1. Считайте, что переменная florida_hurricane_dates объявлена и доступна вашей программе.

Примечание 2. Считайте, что тип date уже импортирован в программу.
"""

# # счетчик для нужного количества ураганов
# early_hurricanes = 0

# # цикл по датам в которые был ураган
# for hurricane in florida_hurricane_dates:
#     # если месяц урагана меньше чем июнь (порядковый номер 6)
#     if hurricane.month < 6:
#         early_hurricanes += 1

# print(early_hurricanes)

"""
Вам доступен список dates, содержащий даты. Дополните приведенный ниже код, 
чтобы он вывел год и номер квартала каждой даты из данного списка. 
Компоненты дат должны быть расположены в исходном порядке, каждые на 
отдельной строке, в следующем формате:

<год>-Q<номер квартала>
Примечание 1. Продолжительность кварталов:

1 квартал	январь, февраль, март
2 квартал	апрель, май, июнь
3 квартал	июль, август, сентябрь
4 квартал	октябрь, ноябрь, декабрь
Примечание 2. Начальная часть ответа выглядит так:

2010-Q3
2017-Q1
...
"""

# from datetime import date


# dates = [date(2010, 9, 28), date(2017, 1, 13),
#          date(2009, 12, 25), date(2010, 2, 27),
#          date(2021, 10, 11), date(2020, 3, 13),
#          date(2000, 7, 7), date(1999, 4, 14),
#          date(1789, 11, 19), date(2013, 8, 21),
#          date(1666, 6, 6), date(1968, 5, 26)]

# for d in dates:
#     print(f"{d.year}-Q{int((d.month - 0.5)/3 + 1)}")

"""
Функция get_min_max()
Реализуйте функцию get_min_max(), которая принимает один аргумент:

dates — список дат (тип date)
Функция должна возвращать кортеж, первым элементом которого является 
минимальная дата из списка dates, вторым — максимальная дата из списка dates. 
Если список dates пуст, функция должна вернуть пустой кортеж.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию get_min_max(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:
"""

# from datetime import date

# def get_min_max(dates):
#     if dates:
#         return min(dates), max(dates)
#     return ()
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
# print(get_min_max(dates))
# print(get_min_max([]))



"""
Функция get_date_range()
Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start 
до end включительно. Если start > end, функция должна вернуть пустой список.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию 
get_date_range(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:
"""

# from datetime import date

# def get_date_range(date1, date2):
#     if date1 <= date2:
#         return list(date.fromordinal(d) for d in range(date.toordinal(date1), date.toordinal(date2) + 1))
#     return ()
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]

# date1 = date(2021, 10, 1)
# date2 = date(2021, 10, 5)

# print(*get_date_range(date1, date2), sep='\n')

# date1 = date(2019, 6, 5)
# date2 = date(2019, 6, 5)

# print(get_date_range(date1, date2))

"""
Функция saturdays_between_two_dates()
Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.

Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, 
что первая дата меньше второй.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию saturdays_between_two_dates(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:
"""

# from datetime import date

# def saturdays_between_two_dates(date1, date2):
#     dates = sorted([date1, date2])
#     interval = list(date.fromordinal(d) for d in range(date.toordinal(dates[0]), date.toordinal(dates[1]) + 1))
#     return len(list(d for d in interval if d.weekday() == 5))

# def saturdays_between_two_dates(start, end):
#     if start > end:
#         start, end = end, start
        
#     return sum(date.fromordinal(i).weekday() == 5 for i in range(start.toordinal(), end.toordinal() + 1))


# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)

# print(saturdays_between_two_dates(date1, date2))

# date1 = date(2020, 7, 26)
# date2 = date(2020, 7, 2)

# print(saturdays_between_two_dates(date1, date2))

# date1 = date(2018, 7, 13)
# date2 = date(2018, 7, 13)

# print(saturdays_between_two_dates(date1, date2))

# from datetime import date

# my_date = date(2019, 2, 4)

# print(my_date)

# from datetime import time

# my_time = time(8, 20, 15)

# print(my_time)

# from datetime import date

# my_date = date(2021, 12, 31)

# print(my_date.strftime('%d %B %Y'))

"""
Вам доступно время alarm. Дополните приведенный ниже код, 
чтобы он вывел следующие его компоненты:

количество часов в формате HH
количество минут в формате MM
количество секунд в формате SS
"""

# from datetime import time

# alarm = time(7, 30, 25)

# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))

"""
Вам доступна дата birthday. Дополните приведенный ниже код, 
чтобы он вывел следующие её компоненты:

полное название месяца на английском
полное название дня недели на английском
год в формате YYYY
номер месяца в формате MM
день месяца в формате DD
"""

# from datetime import date

# birthday = date(1992, 10, 6)

# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))

"""
В переменной florida_hurricane_dates хранится список дат, в которые 
произошел ураган во Флориде с 1950 по 2017 год.

Дополните приведенный ниже код, чтобы он вывел самую раннюю дату из 
списка florida_hurricane_dates в трех различных форматах:

в стандарте ISO (YYYY-MM-DD)
в типичном для России стиле (DD.MM.YYYY)
в типичном для Америки стиле (MM/DD/YYYY)

Примечание 1. Считайте, что переменная florida_hurricane_dates 
объявлена и доступна вашей программе.

Примечание 2. Считайте, что тип date уже импортирован в программу.
"""

# from datetime import date
# # присваиваем самую раннюю дату урагана в переменную first_date

# florida_hurricane_dates = [date(2021, 12, 31), date(2025, 3, 19), date(2017, 5, 25)]

# first_date = min(florida_hurricane_dates)

# # конвертируем дату в ISO и RU формат
# iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
# ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
# us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

# print(iso)
# print(ru)
# print(us)

"""
Ураган Эндрю, который обрушился на Флориду 24 августа 1992 года, 
был одним из самых дорогостоящих и смертоносных ураганов в истории США. 
Дополните приведенный ниже код, чтобы он вывел дату 24 августа 1992 
года в трех различных форматах:

в формате YYYY-MM
в формате month_name (YYYY), 
    где month_name – полное название месяца на английском
в формате YYYY-day_number, где day_number – день года

"""

# from datetime import date

# andrew = date(1992, 8, 24)

# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number

# n = 'python'

# try:
#     n = int(n)
#     print(n * 2)
# except ValueError:
#     print('Произошла ошибка')

# try:
#     names = ['Tim', 'Tom', 'Jerry', 'Alvin', 'Wall-e']
#     print(names[-5])
#     print(names[5])
# except:
#     print('IndexError')

"""
Две даты
Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

Формат входных данных
На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD), каждая на отдельной строке.

Формат выходных данных
Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).

Примечание. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/Professional/tree/main/Module_3/Module_3.2/Module_3.2.12
"""
# from datetime import date

# print(min([date.fromisoformat(input()), date.fromisoformat(input())]).strftime('%d-%m (%Y)'))


