# Itertools в Python

https://habr.com/ru/company/otus/blog/529356/

Модуль __itertools__ стандартизирует основной набор быстрых эффективных по памяти инструментов, которые полезны сами по себе или в связке с другими инструментами. Вместе они формируют «алгебру итераторов», которая позволяет лаконично и эффективно создавать специализированные инструменты на чистом Python.

Модуль itertools находится в стандартной библиотеке Python.

Модуль представляет следующие типы итераторов: 

+ Бесконечные итераторы;
+ Конечные итераторы;
+ Комбинаторные генераторы.

Возвращаемый объект также будет итератором. Мы можем проходиться по итератору с помощью:

+ функции «next»
+ цикла for
+ конвертации в список с помощью list()

# Бесконечные итераторы:

count(), cycle(), repeat()

# count()

Создает итератор, который возвращает равномерно распределенные значения, начиная с числа, указанного в аргументе start. 

По умолчанию start равен 0, а step -1. Шаг также может быть нецелым значением. Эта функция вернет бесконечный итератор.
```python
    import itertools
    c=itertools.count()
    #next() function returns next item in the iterator.By default starts with number 0 and increments by 1.
    print (next(c))#Output:0
    print (next(c))#Output:1
    print (next(c))#Output:2
    print (next(c))#Output:3


    #Returns an infinite iterator starting with number 5 and incremented by 10. The values in the iterator are accessed by next()
    c1=itertools.count(5,10)
    print(next(c1))#Output:5
    print(next(c1))#Output:10
    print(next(c1))#Output:15


    #accessing values in the iterator using for loop.step argument can be float values also.
    c2=itertools.count(2.5,2.5)
    for i in c2:
        #including terminating condition, else loop will keep on going.(infinite loop)
        if i>25:
            break
        else:
            print (i,end=" ") #Output:2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0 22.5 25.0
            

    #step can be negative numbers also.negative numbers count backwards.
    c3=itertools.count(2,-2.5)
    print (next(c3))#Output:2
    print (next(c3))#Output:-0.5
    print (next(c3))#Output:-3.0
```
Также она используется в качестве аргумента в функциях map() и zip().

zip() – это встроенная функция Python, которая позволяет комбинировать соответствующие элементы из нескольких последовательностей и возвращать объект zip, который представляет из себя итератор кортежей. 

itertools.count() можно использовать в качестве входной последовательности для функции zip().
```python
    import itertools
    #itertools.count() used in zip()
    l1=[5,15,25]
    l2=zip(itertools.count(),l1)
    #It will return zip object which is an iterable instance of zip class
    print (l2)#Output:<zip object at 0x032C92C8>


    #we can convert zip object to list.
    print (list(l2))#Output:[(0, 5), (1, 15), (2, 25)]


    # We can access the zip object by using "for loop".This is more efficient way to access large sequences.It won't be memory intensive.
    l3=zip(itertools.count(),l1)
    for i in l3:
        print (i)
    '''
    Output:
    (0, 5)
    (1, 15)
    (2, 25)
    '''
```
map() используется для применения функции ко всем элементам в указанном итераторе и возвращает объект map, который также является итератором. Мы можем использовать itertools.count() в качестве аргумента для функции map().
```python
    import itertools
    #lambda function and itertools.count() is given as argument in map()function.
    l1=map(lambda x:x**2,itertools.count())
    #It returns a map object which is an iterator.
    print(l1)#Output:<map object at 0x00E2E610>

    #iterate thorugh map object using for loop
    for i in l1:
        if i>50:
            break
        else:
            print (i ,end=" ")#Output:0 1 4 9 16 25 36 49
```
# cycle()

Создает итератор, возвращающий элементы из итерируемого объекта и сохраняющий копию каждого из них. Когда итерируемый объект заканчивается, возвращается элемент из сохраненной копии. Работает бесконечно.
```python
    itertools.cycle(iterable)

    import itertools
    l1=[1,2,3]
    #using list iterable as an argument in itertools.cycle()
    l2=itertools.cycle(l1)
    print (l2)#Output:<itertools.cycle object at 0x02F794E8>

    count=0
    for i in l2:
        #It will end in infinite loop. So have to define terminating condition.
        if count > 15:
            break
        else:
            print (i,end=" ")#Output:1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1
            count+=1

            
    #string is given as an argument in itertools.cycle() function.
    s1="hello"
    l3=itertools.cycle(s1)
    #accessing the iterator using next()
    print (next(l3))    #Output:h
    print (next(l3))    #Output:e
    print (next(l3))    #Output:l
    print (next(l3))    #Output:l
    print (next(l3))    #Output:o
```
# repeat():

Создает итератор, который возвращает объект снова и снова. Выполняется бесконечно, если не указано значение аргумента times.

Может использоваться как аргумент в функциях map() и zip().
```python
    itertools.repeat(object,times)

    import itertools
    #times argument is not mentioned. It will result in infinite loop.
    l1=itertools.repeat(2)
    print (next(l1))#Output:2
    print (next(l1))#Output:2


    #string is used as an argument.times argument is mentioned as 10.It will repeat the string 10 times.
    l2=itertools.repeat("hello",times=10)
    for i in l2:
        print (i,end=" ")#Output:hello hello hello hello hello hello hello hello hello hello
    print (" ")


    #list is used as argument
    l3=itertools.repeat([1,2,3],times=3)
    for i in l3:
        print (i,end=" ")#Output:[1, 2, 3] [1, 2, 3] [1, 2, 3]
    print (" ")


    #tuple is used as an argument
    l4=itertools.repeat(('red','blue'),times=3)
    for i in l4:
        print (i,end=" ")#Output:('red', 'blue') ('red', 'blue') ('red', 'blue')
```
Здесь функция используется в качестве аргумента функции map().
```python
    import itertools
    #It will return square of numbers from 0 to 9.
    l1=map(pow,range(10),itertools.repeat(2))
    print(l1)#Output:<map object at 0x011CEC10>

    #iterate through map object using for loop
    for i in l1:
        print (i,end=" ") #Output:0 1 4 9 16 25 36 49 64 81
```
Здесь функция используется в качестве аргумента в функции zip().
```python
    import itertools
    #itertools.repeat() used in zip()
    l1=[5,15,25]
    l2=zip(itertools.repeat(2),l1)
    #It will return zip object which is an iterable instance of zip class
    print (l2)#Output:<zip object at 0x032794E8>


    #we can convert zip object to list.
    print (list(l2))#Output:[(2, 5), (2, 15), (2, 25)]


    # We can access zip object by using for loop.This is more efficient way to access large sequences.It won't be memory intensive.
    l3=zip(itertools.repeat("hello"),l1)
    for i in l3:
        print (i)
    '''
    Output:
    ('hello', 5)
    ('hello', 15)
    ('hello', 25)
    '''
```
# Конечные итераторы:

# accumulate():

Создает итератор, который возвращает накопленную сумму или накопленный результат других бинарных функций, которые указаны в параметре func. 

Обычно количество элементов в выходной итерации совпадает с количеством элементов во входной итерации. Если указывается параметр initial, он также учитывается, поэтому выходная итерация содержит на один элемент больше, чем входная. 

functools.reduce() возвращает только конечное накопленное значение для аналогичной функции. 

Параметр initial добавлен в Python версии 3.8.
```python
    itertools.accumulate(iterable,func,*,initial=None)

    import itertools
    #using add and mul operator,so importing operator module
    import operator
    #using reduce(),so importing reduce() from functools module
    from functools import reduce

    #If func parameter is not mentioned,by default it will perform addition operation)
    l1=itertools.accumulate([1,2,3,4,5])
    print (l1)#Output:<itertools.accumulate object at 0x02CD94C8>
    #Converting iterator to list object.
    print (list(l1))#Output:[1, 3, 6, 10, 15]
    #using reduce() for same function
    r1=reduce(operator.add,[1,2,3,4,5])
    print (r1)#Output:15


    #If initial parameter is mentioned, it will start accumulating from the initial value.
    #It will contain more than one element in the ouptut iterable.
    l2=itertools.accumulate([1,2,3,4,5],operator.add,initial=10)
    print (list(l2))#Output:[10, 11, 13, 16, 20, 25]


    #it takes operator mul as function
    # It will perform multiplication on first two elements, then it will perform multiplication of next two element in the iterable.
    l3=itertools.accumulate([1,2,3,5,5],operator.mul)
    print (list(l3))#Output:[1, 2, 6, 30, 150]
    #using reduce() for same function mul.
    r2=reduce(operator.mul,[1,2,3,4,5])
    print (r2)#Output:120


    l4=itertools.accumulate([2,4,6,3,1],max)
    print (list(l4))#Output:[2, 4, 6, 6, 6]
    #using reduce for same function max
    r3=reduce(max,[2,4,6,3,1])
    print (r3)#Output:6


    #It takes min function as parameter.
    # It will compare two elements and find the minimum element,then compare the other elements and find the mininum element.
    l5=itertools.accumulate([2,4,6,3,1],min)
    print (list(l5))#Output:[2, 2, 2, 2, 1]
    #using reduce() for same function min
    r4=reduce(min,[2,4,6,3,1])
    print (r4)#Output:1
```
# chain():

Создает итератор, который возвращает элемент из итерируемого объекта до тех пор, пока он не закончится, а потом переходит к следующему. Он будет рассматривать последовательности, идущие друг за другом, как одну. 
```python
    itertools.chain(*iterables)
```

```python
    import itertools
    l1=itertools.chain(["red","blue"],[1,2,3],"hello")
    #Returns an iterator object
    print (l1)      #Output:<itertools.chain object at 0x029FE4D8>
                    #converting iterator object to list object
    
    print(list(l1)) #Output:['red', 'blue', 1, 2, 3, 'h', 'e', 'l', 'l', 'o']


    l2=itertools.chain("ABC","DEF","GHI")
    print (list(l2))#Output:['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
```
# chain.from_iterable()

Эта функция берет один итерируемый объект в качестве входного аргумента и возвращает «склеенный» итерируемый объект, содержащий все элементы входного. Все элементы, подаваемые на вход, должны быть итерируемыми, иначе выпадет исключение TypeError.
```python
    chain.from_iterable(iterable)
```
```python
    import itertools
    l1=itertools.chain.from_iterable(["ABC","DEF","GHI"])
    print (list(l1))#Output:['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    l2=itertools.chain(["ABC","DEF","GHI"])
    print (list(l2))#Output:['ABC', 'DEF', 'GHI']

    #all elements in the input iterable should be iterable.Otherwise it will raise TypeError.
    l3=itertools.chain.from_iterable([1,2,3])
    print (list(l3))#Output:TypeError: 'int' object is not iterable
```
# compress()

Создает итератор, который фильтрует элементы data, возвращая только те, которые содержат соответствующий элемент в селекторах (selectors), стоящих в True. Прекращает выполнение, когда либо данные, либо селекторы закончились. 
```python
    itertools.compress(data,selectors)
```

```python
    import itertools
    selectors=[True,False,True,False]
    l1=itertools.compress([1,2,3,4],selectors)
    #Only returns element whose corresponding selector is True.
    print (list(l1))#Output:[1,3]


    #filter - instead of passing an iterable of True and False. function is used to determine the value "True or False"
    l2=filter(lambda x:x%2!=0,[1,2,3,4])
    print (list(l2))#Output:[1,3]
```
# dropwhile()

Создает итератор, который выбрасывает элементы из итерируемого объекта до тех пор, пока предикат (predicate) имеет значение True, а затем возвращает каждый элемент. Итератор не вернет выходных данных, пока предикат не получит значение False.
```python
    itertools.dropwhile(predicate,iterable)
```
# takewhile()

Создает итератор, который возвращает элементы из итерируемого объекта до тех пор, пока предикат имеет значение True.
```python
    itertools.takewhile(predicate,iterable)
```
```python
    import itertools
    ##iterator will start displaying after condition is False.
    l1=itertools.dropwhile(lambda x:x>4,[5,6,7,8,9,1,2,3])
    print (l1)#Output:<itertools.dropwhile object at 0x02E592C8>
    print (list(l1))#Output:[1, 2, 3]
    #iterator used to print values till condition is False.
    l4=itertools.takewhile(lambda x:x>4,[5,6,7,8,9,1,2,3])
    print (list(l4))#Output:[5, 6, 7, 8, 9]


    #iterator will start displaying after condition is False.
    l2=itertools.dropwhile(lambda x:x%2==0,[2,4,6,8,10])
    print (list(l2))#Output:[]
    #iterator used to print values till condition is False.
    l3=itertools.takewhile(lambda x:x%2==0,[2,4,6,8,10])
    print (list(l3))#Output:[2, 4, 6, 8, 10]
```
# filterfalse():

Создает итератор, который фильтрует элементы итерируемого объекта, возвращая только те, для которых предикат имеет значение False. Если предикат равен None, он возвращает элементы, которые стоят в значении False. 

Метод filter() возвращает итератор, который содержит элементы итерируемого объекта, для которых функция возвращает True.
```python
    itertools.filterfalse(predicate,iterables)
```
```python
    import itertools
    #iterator will filter the elements from the iterable which returns False for the given function
    l1=itertools.filterfalse(lambda x:x>4,[1,2,3,4,5,6,7,8,9])
    print (l1)#Output:<itertools.filterfalse object at 0x0083E658>
    print (list(l1))#Output:[1, 2, 3,4]
    #filter() function will  filter the elements from the iterable which returns True for the given function
    l4=filter(lambda x:x>4,[1,2,3,4,5,6,7,8,9])
    print (list(l4))#Output:[5, 6, 7, 8, 9]


    #iterator will filter the elements from the iterable which returns False for the given function
    l2=itertools.filterfalse(lambda x:x%2==0,[2,4,6,8,10])
    print (list(l2))#Output:[]
    #filter() function will filter the elements from the iterable which returns True for the given function
    l3=filter(lambda x:x%2==0,[2,4,6,8,10])
    print (list(l3))#Output:[2, 4, 6, 8, 10]


    #If predicate is None, returns the items that are False.
    l5=itertools.filterfalse(None,[0,1,2,3,4,5])
    print (list(l5))#Output:[0]
    #If predicate is None,filter() function returns the items that are True.
    l6=filter(None,[0,1,2,3,4])
    print (list(l6))#Output:[1, 2, 3, 4]
```
# zip_longest()

Создает итератор, который агрегирует элементы из каждого итерируемого объекта. Если итераторы имеют неравномерную длину, то на место пропущенных значений ставится fillvalue. Итерация будет продолжаться до тех пор, пока не закончится самый длинный итерируемый объект.

В zip() итерация продолжается до тех пор, пока не закончится самый короткий итерируемый объект.
```python
    itertools.zip_longest(*iterables,fillvalue=None)
```
```python
    import itertools
    #fillvalue is not given,by default it will be None.
    #iteration continues until longest iterable is exhausted.
    z1=itertools.zip_longest([1,2,3,4,5],['a','b','c'])
    print (z1)#Output:<itertools.zip_longest object at 0x00AA3BE0>
    #we can iterate through zip object using for loop or we can convert to list object.
    print (list(z1))#Output:[(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]


    #fillvalue is mentioned
    z2=itertools.zip_longest([1,2,3,4,5],['a','b','c'],fillvalue="z")
    print (list(z2))#Output:[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'z'), (5, 'z')]


    #using zip(),iteration continues until shorest iterable is exhausted.
    z3=zip([1,2,3,4,5],['a','b','c'])
    print (list(z3))#Output:[(1, 'a'), (2, 'b'), (3, 'c')]
```
# starmap()

Создает итератор, который вычисляет функцию, получая аргументы из итерируемого объекта. Используется вместо map(), когда параметры аргумента уже сгруппированы в кортежи в одном итерируемом объекте (данные были предварительно сжаты).
```python
    itertools.starmap(function,iterable)
```
```python
    import itertools
    l1=itertools.starmap(pow,[(0,2),(1,2),(2,2)])
    print (l1)#Output:<itertools.starmap object at 0x00C8E4D8>
    #We can iterate through starmap object,using for loop or using next() function. We can also convert to list object.
    print (list(l1))#Output:[0, 1, 4]


    #using map()
    l2=map(pow,[0,1,2],[2,2,2])
    print (list(l2))#Output:[0, 1, 4]


    a1=map(lambda x:x**2,[1,2,3])
    print (list(a1))#Output:[1, 4, 9]

    #If elements inside the iterable are not iterable, it will raise TypeError.
    a2=itertools.starmap(lambda x:x**2,[1,2,3])
    print (list(a2))#Output:TypeError: 'int' object is not iterable

    a3=itertools.starmap(lambda x,y:x+y,[(0,1),(1,2),(2,3)])
    print (list(a3))#Output:[1, 3, 5]
```
# islice()

Создает итератор, который возвращает выбранные элементы из итерируемого объекта. 

Если start равен None, то итерация начинается с нуля. 

Если step равен None, то по умолчанию ему дается значение 1. 

Если stop равен None, то итерация будет продолжаться, пока элементы в итерируемом объекте не закончатся, если они вообще могут закончиться. 

В противном случае итератор остановится на определенной позиции. 

В islice() не поддерживаются отрицательные значения для параметров start, stop и step.
```python
    itertools.islice(iterable,stop)
```
```python
    itertools.islice(iterable, start, stop[, step])

    import itertools
    #if only one argument is mentioned other than iterable,it is stop value.
    l1=itertools.islice([1,2,3,4,5,6,7,8,9,10],5)
    print (list(l1))#Output:[1, 2, 3, 4, 5]


    #start=2 and stop=5 mentioned. It will start from second index and ends at fifth index
    l2=itertools.islice([1,2,3,4,5,6,7,8,9,10],2,5)
    print (list(l2))#Output:[3,4,5]


    #start=2,step=3.It will start from second index and increment by 3.
    l3=itertools.islice([1,2,3,4,5,6,7,8,9,10],2,None,3)
    print (list(l3))#Output:[3,6,9]


    #step is given as negative value,it raises ValueError
    l4=itertools.islice([1,2,3,4,5,6,7,8,9,10],2,None,-2)
    print (list(l4))#Output:ValueError: Step for islice() must be a positive integer or None.
```
# tee()

Возвращает n независимых итераторов из одного итерируемого объекта.
```python
    itertools.tee(iterable,n=2)
```
```python
    import itertools
    l1=[1,2,3,4,5]
    l2=itertools.tee(l1,3)
    print (l2)#Output:(<itertools._tee object at 0x028794C8>, <itertools._tee object at 0x028792C8>, <itertools._tee object at 0x02879528>)
    for i in l2:
        print (list(i))
    '''
    Output:    
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    '''
```
# groupby():

Создает итератор, который возвращает последовательно ключи и группы из итерируемого объекта.

key – это функция, вычисляющая значение ключа для каждого элемента по умолчанию. 

Если ключ не указан или в значении None, то по умолчанию ключ является функцией идентификации, которая возвращает элемент без изменений. 
```python
    itertools.groupby(iterable,key=None)
```
```python
    import itertools
    l1=[('color','red'),('color','blue'),('color','green'),('Numbers',1),('Numbers',5)]
    l2=itertools.groupby(l1,key=lambda x:x[0])
    print (l2)#Output:<itertools.groupby object at 0x0305F528>
    for key,group in l2:
        result={key:list(group)}
        print (result)
    '''
    Output:
    {'color': [('color', 'red'), ('color', 'blue'), ('color', 'green')]}
    {'Numbers': [('Numbers', 1), ('Numbers', 5)]}
    '''

    #list doesn't contain sorted data based on the key function.It breaks the group every time,when value of key function changes.
    l1=[('color','red'),('color','blue'),('color','green'),('Numbers',1),('Numbers',5),('color','purple')]
    l2=itertools.groupby(l1,key=lambda x:x[0])
    print (l2)#Output:<itertools.groupby object at 0x028AF5A0>

    for key,group in l2:
        result={key:list(group)}
        print (result)
    '''
    Output:
    {'color': [('color', 'red'), ('color', 'blue'), ('color', 'green')]}
    {'Numbers': [('Numbers', 1), ('Numbers', 5)]}
    {'color': [('color', 'purple')]}
    '''


    #key is not mentioned
    l1=[('color','red'),('color','blue'),('color','green'),('Numbers',1),('Numbers',5),('color','purple')]
    l2=itertools.groupby(l1)
    print (l2)#Output:<itertools.groupby object at 0x028AF578>
    for key,group in l2:
        result={key:list(group)}
        print (result)
    '''
    Output:
    {('color', 'red'): [('color', 'red')]}
    {('color', 'blue'): [('color', 'blue')]}
    {('color', 'green'): [('color', 'green')]}
    {('Numbers', 1): [('Numbers', 1)]}
    {('Numbers', 5): [('Numbers', 5)]}
    {('color', 'purple'): [('color', 'purple')]}

    '''
```
# Комбинаторные генераторы:

# product()

Декартово произведение итерируемых объектов, подаваемых на вход.

Определение декартова произведения: произведение множества X и множества Y – это множество, содержащее все упорядоченные пары (x, y), в которых x принадлежит множеству X, а y принадлежит множеству Y.

Чтобы вычислить произведение итерируемого объекта умноженного самого на себя, нужно указать количество повторений с помощью опционального аргумента с ключевым словом repeat. Например, product(A, repeat=4) – тоже самое, что и product(A, A, A, A).
```python
    itertools.product(*iterables,repeat)
```
```python
    import itertools
    #Only one iterable is given
    l1=itertools.product("ABCD")
    print (list(l1))#Output:[('A',), ('B',), ('C',), ('D',)]


    #two iterables are given
    l2=itertools.product("ABC",[1,2])
    print (list(l2))#Output:[('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)]


    #one iterable and repeat is mentioned.
    l3=itertools.product("xy",repeat=2)
    print (list(l3))#Output:[('x', 'x'), ('x', 'y'), ('y', 'x'), ('y', 'y')]


    l4=itertools.product("aa",repeat=2)
    print (list(l4))#Output:[('a', 'a'), ('a', 'a'), ('a', 'a'), ('a', 'a')]


    #More than two iterables is mentioned
    l5=itertools.product([1,2],[3,4],[5,6])
    print (list(l5))#Output:[(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]
```
# permutations()

Возвращает последовательные r перестановок элементов в итерируемом объекте. 

Если параметр r не указан или стоит в значении None, то по умолчанию r принимает длину итерируемого объекта и генерирует все возможные полноценные перестановки. 

Кортежи перестановок выдаются в лексикографическим порядке в соответствии с порядком итерации входных данных. 

Таким образом, если входные данные итерируемого объекта отсортированы, то комбинация кортежей будет выдаваться в отсортированном порядке.

Элементы рассматриваются как уникальные в зависимости от их позиции, а не от их значения. 

Таким образом, если входные элементы уникальны, то в каждой перестановке не будет повторяющихся значений. 
```python
    itertools.permutations(iterable,r=None)
```
```python
    import itertools
    l1=itertools.permutations("ABC")
    print (list(l1))#Output:[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]


    l2=itertools.permutations([3,2,1])
    print (list(l2))#Output:[(3, 2, 1), (3, 1, 2), (2, 3, 1), (2, 1, 3), (1, 3, 2), (1, 2, 3)]


    #elements are treated as unique based on their position and not by their value.
    l3=itertools.permutations([1,1])
    print (list(l3))#Output:[(1, 1), (1, 1)]


    l4=itertools.permutations(["ABC"])
    print (list(l4))#Output:[('ABC',)]


    #r value is mentioned as 2. It will return all different permutations in 2 values.
    l5=itertools.permutations([1,2,3,4],2)
    print (list(l5))#Output:[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
```
Примечание: в перестановках порядок элементов имеет значение.

# combinations()

Возвращает подпоследовательности длины r из элементов итерируемого объекта, подаваемого на вход. 

Комбинация кортежей генерируется в лексикографическом порядке в соответствии с порядком элементов итерируемого объекта на входе. Таким образом, если входной итерируемый объект отсортирован, то комбинация кортежей будет генерироваться в отсортированном порядке.

Лексикографический порядок – способ упорядочивания слов в алфавитном порядке. 

Элементы рассматриваются как уникальные в зависимости от их позиции, а не значения. Таким образом, если выходные элементы уникальны, то в каждой комбинации не будет повторяющихся значений.
```python
    itertools.combinations(iterable, r)
```
# combinations_with_replacement():

Возвращает подпоследовательности длины r из элементов итерируемого объекта, подаваемого на вход, при этом отдельные элементы могут повторяться больше одного раза. 
```python
    itertools.combinations_with_replacement (iterable, r)
```
```python
    import itertools
    l1=itertools.combinations("ABC",2)
    print (list(l1))#Output:[('A', 'B'), ('A', 'C'), ('B', 'C')]
    l1=itertools.combinations_with_replacement("ABC",2)
    print (list(l1))#Output:[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


    l2=itertools.combinations([3,2,1],3)
    print (list(l2))#Output:[(3, 2, 1)]
    l2=itertools.combinations_with_replacement([3,2,1],3)
    print(list(l2))#Output:[(3, 3, 3), (3, 3, 2), (3, 3, 1), (3, 2, 2), (3, 2, 1), (3, 1, 1), (2, 2, 2), (2, 2, 1), (2, 1, 1), (1, 1, 1)]


    #elements are treated as unique based on their position and not by their value.
    l3=itertools.combinations([1,1],2)
    print (list(l3))#Output:[(1, 1)]
    l3=itertools.combinations_with_replacement([1,1],2)
    print (list(l3))#Output:[(1, 1), (1, 1), (1, 1)]


    #since list contains only one element, given r value is 2. So it returns empty list.
    l4=itertools.combinations(["ABC"],2)
    print (list(l4))#Output:[]
    #In combinations_with_replacement,it allows repeated element.
    l4=itertools.combinations_with_replacement(["ABC"],2)
    print (list(l4))#Output:[('ABC', 'ABC')]


    #r value is not mentioned. It will raise TypeError
    #l5=itertools.combinations([1,2,3,4])
    #print (list(l5))#Output:TypeError: combinations() missing required argument 'r' (pos 2)
    l5=itertools.combinations_with_replacement([1,2,3,4])
    print (list(l5))#Output:TypeError: combinations_with_replacement() missing required argument 'r' (pos 2)
```
# Примечание:

1. Используется в качестве аргумента в map() и zip():

+ count() 
+ repeat()

repeat() - передача потока постоянных значений в функцию map() или zip().

count() - будет подавать различные значения в функции map() или zip().

2. Разница между cycle() и repeat():

cycle() – итерирует один и тот же объект снова и снова;

repeat() – возвращает снова и снова один и тот же объект.

3. Разница между reduce() и itertools.accumulate():

reduce():

Возвращает только конечную сумму;

Первый аргумент должен быть функцией, а второй – итерируемым объектом.

accumulate():

Возвращает текущее накопленное значение. Элементы в выходном итерируемом объекте будут равны элементам во входном объекте, если не будет указано начальное значение.

Первый аргумент должен быть итерируемым объектом, а второй – функцией.

4. Разница между filter() и itertools.compress():

Функция filter() фильтрует заданный итерируемый объект с помощью функции, которая проверяет, стоит каждый элемент в значении True или нет.

Функция compress() фильтрует заданный итерируемый объект на основе соответствующего элемента в параметре селектора. В качестве селектора задается итерируемый объект со значениями True/False. 

5. Разница между filter() и itertools.filterfalse():

filter(): создает итератор из элементов итерируемого объекта, для которых заданная функция возвращает значение True.

filterfalse(): создает итератор из элементов итерируемого объекта, для которых заданная функция возвращает значение False.

6. Разница между zip() и itertools.zip_longest():

zip(): Итерация продолжается до тех пор, пока не закончится самый короткий итерируемый объект.

zip_longest(): Итерация продолжается до тех пор, пока не закончится самый длинный итерируемый объект.

7. Разница между срезом списка и itertools.islice():

Срез списка создает новый список;

islice() – возвращает итератор. С помощью итератора мы можем организовать цикл так, как нам удобно. 

8. Разница между itertools.permutations() и itertools.combinations():

itertools.permutations(): Порядок элементов имеет значение;

itertools.combinations(): Порядок элементов не имеет значения. 

Комбинации и перестановки не содержат повторяющихся значений.

9. Разница между itertools.combinations() и itertools.combination_swith_replacement:

combinations(): Порядок элементов не имеет значения, и значения не повторяются.

combinations_with_replacement(): Порядок элементов не имеет значения, и значения повторяются.

10. Разница между itertools.takewhile() и itertools.dropwhile():

takewhile(): Создает итератор, который возвращает элементы из итерируемого объекта, пока предикат находится в значении True.

dropwhile(): Создает итератор, который выбрасывает элементы из итерируемого объекта, пока предикат находится в значении True, а затем возвращает каждый элемент.

Источники:

https://docs.python.org/3/library/itertools.html