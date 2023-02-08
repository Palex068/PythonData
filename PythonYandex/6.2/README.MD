# 6.2. Модуль pandas

В прошлой главе мы познакомились с библиотекой numpy и узнали, что она позволяет существенно ускорить вычисления в Python. 

Сегодня мы рассмотрим библиотеку pandas, которая применяется для обработки и анализа табличных данных. 

В этой библиотеке используется numpy для удобного хранения данных и вычислений.

Для установки pandas выполним в командной строке команду:

    pip install pandas

Во всех примерах предполагается, что библиотеки numpy и pandas импортированы следующим образом:

    import numpy as np
    import pandas as pd

В библиотеке pandas определены два класса объектов для работы с данными:

+ Series – одномерный массив, который может хранить значения любого типа данных.
+ DataFrame – двумерный массив (таблица), в котором столбцами являются объекты класса Series.

Создать объект класса Series можно следующим образом:

    s = pd.Series(data, index=index)

В качестве data могут выступать: массив numpy, словарь, число. В аргумент index передаётся список меток осей. Метка может быть числом, но чаще используются метки-строки.

Если data является массивом numpy, то index должен иметь такую же длину, как и data. Если аргумент index не передаётся, то по умолчанию для index автоматически назначается список [0, ..., len(data) - 1]:

    s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
    print(s)
    print()
    s = pd.Series(np.linspace(0, 1, 5))
    print(s)

Вывод программы:

    a    0
    b    1
    c    2
    d    3
    e    4
    dtype: int32

    0    0.00
    1    0.25
    2    0.50
    3    0.75
    4    1.00
    dtype: float64

Из вывода программы видно, что Series фактически является аналогом словаря, так как вместо числовых индексов может использовать метки в виде строк.

Если data задаётся словарём, а index не передаётся, то в качестве индекса используются ключи словари. Если index передаётся, то его длина может не совпадать с длиной словаря data. В таком случае, по индексам, для которых нет ключа с соответствующим значением в словаре, будут храниться значения NaN – стандартное обозначение отсутствия данных в библиотеке pandas.

    d = {"a": 10, "b": 20, "c": 30, "g": 40}
    print(pd.Series(d))
    print()
    print(pd.Series(d, index=["a", "b", "c", "d"]))
##
    a    10
    b    20
    c    30
    g    40
    dtype: int64

    a    10.0
    b    20.0
    c    30.0
    d     NaN
    dtype: float64

Если data задаётся числом, то index нужно обязательно передать. Количество элементов в Series будет равно числу меток в index, а значения будут равны data:

    index = ["a", "b", "c"]
    print(pd.Series(5, index=index))

Вывод программы:

    a    5
    b    5
    c    5
    dtype: int64

Для Series доступно взятие элемента по индексу, срезы, поэлементные математические операции аналогично массивам numpy.

    s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
    print("Выбор одного элемента")
    print(s["a"])
    print("Выбор нескольких элементов")
    print(s[["a", "d"]])
    print("Срез")
    print(s[1:])
    print("Поэлементное сложение")
    print(s + s)

Вывод программы:

    Выбор одного элемента
    0
    Выбор нескольких элементов
    a    0
    d    3
    dtype: int32
    Срез
    b    1
    c    2
    d    3
    e    4
    dtype: int32
    Поэлементное сложение
    a    0
    b    2
    c    4
    d    6
    e    8
    dtype: int32

Для Series можно применять фильтрацию данных по условию, записанному в качестве индекса:

    s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
    print("Фильтрация")
    print(s[s > 2])

Вывод программы:

    Фильтрация
    d    3
    e    4
    dtype: int32

Объекты Series имеют атрибут name со значением имени набора данных, а также атрибут index.name с именем для индексов:

    s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
    s.name = "Данные"
    s.index.name = "Индекс"
    print(s)

Вывод программы:

    Индекс
    a    0
    b    1
    c    2
    d    3
    e    4
    Name: Данные, dtype: int32

Объект класса DataFrame работает с двумерными табличными данными. Создать DataFrame проще всего из словаря Python следующим образом:

    students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
                        "math": [5, 3, 4],
                        "physics": [4, 5, 5]}
    students = pd.DataFrame(students_marks_dict)
    print(students)

Вывод программы:

        student  math  physics
    0  Студент_1     5        4
    1  Студент_2     3        5
    2  Студент_3     4        5

У объекта класса DataFrame есть индексы по строкам (index) и столбцам(columns):

    print(students.index)
    print(students.columns)

Вывод программы:

    RangeIndex(start=0, stop=3, step=1)
    Index(['student', 'math', 'physics'], dtype='object')

Для индекса по строке по умолчанию задаётся числовое значение. Значения индекса можно заменить путем записи списка в атрибут index:

    students.index = ["A", "B", "C"]
    print(students)

Вывод программы:

        student  math  physics
    A  Студент_1     5        4
    B  Студент_2     3        5
    C  Студент_3     4        5

Для доступа к записям таблицы по строковой метке используется атрибут loc. При использовании строковой метки доступна операция среза:

    print(students.loc["B":])

Вывод программы:

        student  math  physics
    B  Студент_2     3        5
    C  Студент_3     4        5

Убедимся, что столбцы у DataFrame являются объектами класса Series:

    print(type(students["student"]))
Вывод программы:

    <class 'pandas.core.series.Series'>

Обычно табличные данные хранятся в файлах. 

Такие наборы данных принято называть датасетами. 

Файлы с датасетом могут иметь различный формат. pandas поддерживает операции чтения и записи для: CSV, Excel 2007+, SQL, HTML, JSON, буфер обмена и др.

Несколько примеров, как получить датасет из файлов разных форматов:
+ CSV. Используется функция read_csv(). 

    Аргумент file является строкой, в которой записан путь до файла с датасетом. 
    
    Для записи данных из DataFrame в CSV-файл используется метод to_csv(file).
+ Excel. Используется функция read_excel(). 
    
    Для записи данных из DataFrame в Excel-файл используется метод to_excel().
+ JSON. Используется функция read_json(). 
    
    Для записи данных из DataFrame в JSON используется метод to_json().

Для работы с другими форматами файлов в pandas есть функции, работающие аналогично рассмотренным. С ними можно ознакомиться в документации.

Одним из самых популярных форматов хранения табличных данных является CSV (Comma Separated Values, значения с разделителем-запятой).

В файлах этого формата данные хранятся в текстовом виде. 

Строки таблицы записываются в файле с новой строки, а столбцы разделяются определённым символом, чаще всего запятой ',' или точкой с запятой ';'. 

Первая строка, как правило, содержит заголовки столбцов таблицы. 

Пример части CSV-файла с информацией о результатах прохождения тестов студентами и некоторой дополнительной информацией:

    "gender","race/ethnicity","parental level of education","lunch","test preparation course","math score","reading score","writing score"
    "female","group B","bachelor's degree","standard","none","72","72","74"
    "female","group C","some college","standard","completed","69","90","88"

Для дальнейшей работы скачайте данный файл с датасетом.

https://yastatic.net/s3/ml-handbook/admin/Students_Performance_132b1e1ff9.csv?updated_at=2022-11-08T19:21:55.967Z

Получим датасет из CSV-файла с данными о студентах:

    import numpy as np
    import pandas as pd

    students = pd.read_csv("StudentsPerformance.csv")

олученный объект students относится к классу DataFrame.

Для получения первых n строк датасета используется метод head(n). По умолчанию возвращается 5 первых строк:

    print(students.head())

Вывод программы:

    gender race/ethnicity  ... reading score writing score
    0  female        group B  ...            72            74
    1  female        group C  ...            90            88
    2  female        group B  ...            95            93
    3    male        group A  ...            57            44
    4    male        group C  ...            78            75

    [5 rows x 8 columns]

Для получения последних n строк используется метод tail(n). По умолчанию возвращается 5 последних строк:

    print(student.tail(3))

Вывод программы:

        gender race/ethnicity  ... reading score writing score
    997  female        group C  ...            71            65
    998  female        group D  ...            78            77
    999  female        group D  ...            86            86

    [3 rows x 8 columns]

Для получения части датасета можно использовать срез:

    print(students[10:13])
##
        gender race/ethnicity  ... reading score writing score
    10    male        group C  ...            54            52
    11    male        group D  ...            52            43
    12  female        group B  ...            81            73

    [3 rows x 8 columns]

В качестве индекса можно использовать условия для фильтрации данных. Выберем 5 первых результатов теста по математике для студентов, прошедших подготовительный курс.

    print(students[students["test preparation course"] == "completed"]["math score"].head())

Вывод программы:

    1     69
    6     88
    8     64
    13    78
    18    46
    Name: math score, dtype: int64

Выведем 5 лучших результатов тестов по трём дисциплинам для предыдущей выборки с помощью сортировки методом sort_values(). Сортировка по умолчанию производится в порядке возрастания значений. Для сортировки по убыванию в именованный аргумент ascending передаётся значение False.

    with_course = students[students["test preparation course"] == "completed"]
    print(with_course[["math score",
                    "reading score",
                    "writing score"]].sort_values(["math score",
                                                    "reading score",
                                                    "writing score"], ascending=False).head())

Вывод программы:

        math score  reading score  writing score
    916         100            100            100
    149         100            100             93
    625         100             97             99
    623         100             96             86
    114          99            100            100

При сортировке сравнивались последовательно значения в перечисленных столбцах. Проведём сортировку по сумме баллов за тесты. Для этого создадим ещё один столбец total_score и произведём по нему сортировку:

    with_course = students[students["test preparation course"] == "completed"]
    students["total score"] = students["math score"] + students["reading score"] + students["writing score"]
    print(students.sort_values(["total score"], ascending=False).head())

Вывод программы:

        gender race/ethnicity  ... writing score total score
    916    male        group E  ...           100         300
    458  female        group E  ...           100         300
    962  female        group E  ...           100         300
    114  female        group E  ...           100         299
    179  female        group D  ...           100         297

    [5 rows x 9 columns]

Чтобы в таблицу добавить колонку, подойдёт метод assign(). Данный метод даёт возможность создавать колонки при помощи лямбда-функции. Обратите внимание: данный метод возвращает новую таблицу, а не меняет исходную. Перепишем предыдущий пример с использованием assign():

    scores = students.assign(total_score=lambda x: x["math score"] + x["reading score"] + x["writing score"])
    print(scores.sort_values(["total_score"], ascending=False).head())

Вывод программы:

        gender race/ethnicity  ... writing score total_score
    916    male        group E  ...           100         300
    458  female        group E  ...           100         300
    962  female        group E  ...           100         300
    114  female        group E  ...           100         299
    179  female        group D  ...           100         297


При анализе данных часто требуется сгруппировать записи по какому-то признаку. 

Для выполнения операции группировки в pandas используется метод groupby(). 

Сама по себе группировка для рассматриваемого датасета даёт мало информации. 

Поэтому воспользуемся методом count(), чтобы определить количество сгруппированных записей. 

Получим информацию о количестве студентов мужского и женского пола (поле "gender") прошедших курс по подготовке к тестированию (поле "test preparation course"):

    print(students.groupby(["gender", "test preparation course"])["writing score"].count())

Вывод программы:

    gender  test preparation course
    female  completed                  184
            none                       334
    male    completed                  174
            none                       308
    Name: race/ethnicity, dtype: int64

Если необходимо выполнить операцию, которая позволяет получить сводные данные, то такая операция называется агрегацией. 

Примерами функции агрегации являются сумма, среднее арифметическое, минимум, максимум и др. 

Для применения функции агрегации к нескольким столбцам подойдёт метод agg(), в который можно передать словарь с ключами-названиями столбцов, а значения по ключам могут быть списками функций агрегации.

Покажем использование агрегации на примере. Определим среднее арифметическое и медианное значения балла за тест по математике для студентов мужского и женского пола в зависимости от прохождения подготовительного курса:

    agg_functions = {"math score": ["mean", "median"]}
    print(students.groupby(["gender", "test preparation course"]).agg(agg_functions))

Вывод программы:

                                math score       
                                        mean median
    gender test preparation course                  
    female completed                67.195652   67.0
        none                     61.670659   62.0
    male   completed                72.339080   73.0
        none                     66.688312   67.0

Для визуализации данных pandas использует библиотеку matplotlib. Для её установки выполните в командной строке следующую команду:

    pip install matplotlib

Для использования визуализации добавьте следующую строку импорта в начало программы:

    import matplotlib.pyplot as plt

Построим гистограмму, которая показывает распределение количества студентов по баллам за тест по математике:

    plt.hist(students["math score"], label="Тест по математике")
    plt.xlabel("Баллы за тест")
    plt.ylabel("Количество студентов")
    plt.legend()
    plt.show()

В результате работы программы получим следующую гистограмму:

## Ещё по теме
Библиотека pandas предоставляет широкие возможности по обработке и анализу данных, поэтому в этой главе мы рассмотрели лишь базовые методы обработки, анализа и визуализации данных. Для более детального изучения советуем почитать документацию.
https://pandas.pydata.org/docs/

