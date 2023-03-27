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

