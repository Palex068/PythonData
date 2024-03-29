# 5.2. Волшебные методы, переопределение методов. Наследование

В прошлой главе мы узнали, что такое классы и научились их создавать. 

Мы также столкнулись с тем, что при создании похожих классов появляется дублирование кода. 

В ООП для создания новых классов на основе других применяется принцип наследования.

Наследование позволяет при создании нового класса указать для него базовый класс. 

От базового класса наследуется вся его структура – атрибуты и методы. 

Созданный класс-наследник называется производным классом.

Покажем принцип наследования на примере. 

Напишем класс "карандаш"" Pencil, который в качестве атрибута хранит цвет карандаша. 

Карандашом можно нарисовать рисунок. 

Также напишем класс "ручка" Pen, который также хранит цвет, но кроме создания рисунка может ещё и подписать документ, если цвет ручки синий, чёрный или фиолетовый.

    class Pencil:

        def __init__(self, color="серый"):
            self.color = color

        def draw_picture(self):
            return f"Нарисован рисунок цветом '{self.color}'."


    class Pen(Pencil):

        def sign_document(self):
            if self.color not in ("синий", "чёрный", "фиолетовый"):
                return f"Ручкой цвета '{self.color}' нельзя подписать документ."
            return f"Подписан документ."


    blue_pen = Pen(color="синий")
    print(blue_pen.draw_picture())
    print(blue_pen.sign_document())
    red_pen = Pen(color="красный")
    print(red_pen.draw_picture())
    print(red_pen.sign_document())

Вывод программы:

    Нарисован рисунок цветом 'синий'.
    Подписан документ.
    Нарисован рисунок цветом 'красный'.
    Ручкой цвета 'красный' нельзя подписать документ.

Класс Pen является производным от базового класса Pencil. 

За счёт этого мы не описывали заново методы \_\_init__ и draw_picture, и они работают так же, как и в базовом классе. 

Атрибут color тоже унаследован из базового класса Pencil. 

Интерпретатор при вызове метода или атрибута сначала ищет их в текущем производном классе. 

Если их нет в текущем классе, то происходит поиск в базовом классе. 

Если и в базовом их нет, то происходит поиск в вышестоящем базовом классе (в базовом классе для текущего базового класса). 

И так далее, пока метод или атрибут не буден найден в одном из базовых классов. Иначе программа выдаст ошибку класса AttributeError.

Добавим в классе "ручка" возможность указать тип ручки:
+ шариковая,
+ гелевая,
+ перьевая и так далее. 

И пусть подписать документ можно любой ручкой кроме гелевой. 

Для получения типа ручки нам нужно модифицировать метод \_\_init__, добавив в него аргумент pen_type и сохранив его значение в атрибуте. 

Таким образом, нам нужно дополнить метод базового класса. 

Такая операция при наследовании называется расширением метода.

# super()

При расширении методов необходимо вначале вызвать метод базового класса с помощью функции super(). 

Если этого не сделать, то не будут созданы атрибуты базового класса в производном классе, и это приведет к ошибке отсутствия атрибутов.

Модифицируем нашу программу:

    class Pencil:

        def __init__(self, color="серый"):
            self.color = color

        def draw_picture(self):
            return f"Нарисован рисунок цветом '{self.color}'."


    class Pen(Pencil):

        def __init__(self, color, pen_type):
            super().__init__(color=color)
            self.pen_type = pen_type

        def sign_document(self):
            if self.color not in ("синий", "чёрный", "фиолетовый"):
                return f"Ручкой цвета '{self.color}' нельзя подписать документ."
            elif self.pen_type == "гелевая":
                return f"Ручкой типа '{self.pen_type}' нельзя подписать документ."
            return f"Подписан документ."


    blue_ball_pen = Pen(color="синий", pen_type="шариковая")
    print(blue_ball_pen.draw_picture())
    print(blue_ball_pen.sign_document())
    blue_gel_pen = Pen(color="синий", pen_type="гелевая")
    print(blue_gel_pen.draw_picture())
    print(blue_gel_pen.sign_document())

Вывод программы:

    Нарисован рисунок цветом 'синий'.
    Подписан документ.
    Нарисован рисунок цветом 'синий'.
    Ручкой типа 'гелевая' нельзя подписать документ.

Если в производном классе метод базового класса переписывается заново, то говорят о переопределении метода. Переопределим метод draw_picture так, чтобы он выводил информацию о типе ручки, которой нарисован рисунок. В класс Pen нужно добавить следующий код:

    def draw_picture(self):
        return f"Нарисован рисунок ручкой типа '{self.pen_type}', цветом '{self.color}'."

Вывод программы с переопределенным методом:

    Нарисован рисунок ручкой типа 'шариковая', цветом 'синий'.
    Подписан документ.
    Нарисован рисунок ручкой типа 'гелевая', цветом 'синий'.
    Ручкой типа 'гелевая' нельзя подписать документ.

Наследование может производиться сразу от нескольких классов. 

В таком случае базовые классы перечисляются через запятую. 

Производный класс унаследует атрибуты и методы обоих базовых классов.

Напишем программу, в которой будут следующие классы:

+ GreetingFormal. 
    
    При инициализации объектов этого класса создаётся атрибут formal_greeting, содержащий строку "Добрый день,". 
    
    В этом классе также есть метод greet_formal, который принимает аргумент name и возвращает строку с приветствием по имени.

+ GreetingInformal. 

    При инициализации объектов этого класса создаётся атрибут informal_greeting, содержащий строку "Привет,". 
    
    В этом классе также есть метод greet_informal, который принимает аргумент name и возвращает строку с приветствием по имени.

+ GreetingMix. 
    
    Этот класс наследуется от двух предыдущих и может приветствовать пользователя по имени обоими методами.

Программа запишется так:

    class GreetingFormal:

        def __init__(self):
            self.formal_greeting = "Добрый день,"

        def greet_formal(self, name):
            return f"{self.formal_greeting} {name}!"


    class GreetingInformal:

        def __init__(self):
            self.informal_greeting = "Привет,"

        def greet_informal(self, name):
            return f"{self.informal_greeting} {name}!"


    class GreetingMix(GreetingFormal, GreetingInformal):

        def __init__(self):
            GreetingFormal.__init__(self)
            GreetingInformal.__init__(self)


    mixed_greeting = GreetingMix()
    print(mixed_greeting.greet_formal("Пользователь"))
    print(mixed_greeting.greet_informal("Пользователь"))

Вывод программы:

    Добрый день, Пользователь!
    Привет, Пользователь!

Обратите внимание на метод \_\_init__ класса GreetingMix. В нём вместо вызова метода базового класса через функцию super() используется непосредственный вызов из базовых классов с указанием имён этих классов. 

Такой вызов необходим из-за того, что метод \_\_init__ присутствует в обоих базовых классах и происходит конфликт. Интерпретатор при использовании функции super() в нашем примере использовал бы метод того класса, который стоит левее при перечислении в объявлении производного класса. 

В нашем примере это привело бы к тому, что \_\_init__ из класса GreetingInformal не был бы вызван и в производном классе не произошла бы инициализация атрибута informal_greeting. 

Тогда при вызове метода greet_informal было бы вызвано исключение AttributeError.

На основе операции наследования перепишем пример про автомобили из прошлых глав. Пусть класс ElectricCar наследуется от класса Car. 

Методы init и drive будут расширены. 

Метод recharge создан в производном классе. А остальные методы и атрибуты наследуются без изменений.

    class Car:

        def __init__(self, color, consumption, tank_volume, mileage=0):
            self.color = color
            self.consumption = consumption
            self.tank_volume = tank_volume
            self.reserve = tank_volume
            self.mileage = mileage
            self.engine_on = False

        def start_engine(self):
            if not self.engine_on and self.reserve > 0:
                self.engine_on = True
                return "Двигатель запущен."
            return "Двигатель уже был запущен."

        def stop_engine(self):
            if self.engine_on:
                self.engine_on = False
                return "Двигатель остановлен."
            return "Двигатель уже был остановлен."

        def drive(self, distance):
            if not self.engine_on:
                return "Двигатель не запущен."
            if self.reserve / self.consumption * 100 < distance:
                return "Малый запас топлива."
            self.mileage += distance
            self.reserve -= distance / 100 * self.consumption
            return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

        def refuel(self):
            self.reserve = self.tank_volume

        def get_mileage(self):
            return self.mileage

        def get_reserve(self):
            return self.reserve

        def get_consumption(self):
            return self.consumption


    class ElectricCar(Car):

        def __init__(self, color, consumption, bat_capacity, mileage=0):
            super().__init__(color, consumption, bat_capacity, mileage)
            self.bat_capacity = bat_capacity

        def drive(self, distance):
            super().drive(100)
            return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

        def recharge(self):
            self.reserve = self.bat_capacity


    electric_car = ElectricCar(color="white", consumption=15, bat_capacity=90)
    print(electric_car.start_engine())
    print(electric_car.drive(100))

Описание класса ElectricCar существенно сократилось за счёт использования наследования.

Давайте посмотрим, что выведет функция print, если передать в неё объект созданного нами класса ElectricCar. Добавим в программу следующий код:

    print(electric_car)

Вывод программы:

    <__main__.electriccar object at 0x000002365ddd8a00>

Такой вывод говорит нам только о том, что переменная electric_car является объектом класса ElectricCar и расположена по определённому адресу в памяти. 

Можно этот вывод сделать более информативным. 

Когда в функцию print для вывода передаётся аргумент, не являющийся строкой, к нему применяется стандартная функция str. 

При этом в классе, к которому относится аргумент, для аргумента вызывается специальный (ещё говорят "магический") метод \_\_str__. 

Остаётся только описать, какую строку вернёт этот метод. 

И тогда это значение и будет выводиться функцией print. 

Дополним класс ElectricCar методом \_\_str__:

    def __str__(self):
        return f"Электромобиль. " \
            f"Цвет: {self.color}. " \
            f"Пробег: {self.mileage} км. " \
            f"Остаток заряда: {self.reserve} кВт*ч."

Проверим как будет работать наш код:

    electric_car = ElectricCar(color="белый", consumption=15, bat_capacity=90)
    print(electric_car.start_engine())
    print(electric_car.drive(100))
    print(electric_car)

Вывод программы:

    Двигатель запущен.
    Проехали 100 км. Остаток заряда: 75.0 кВт*ч.
    Электромобиль. Цвет: белый. Пробег: 100 км. Остаток заряда: 75.0 кВт*ч.

# Специальных методов в Python довольно много.

Они нужны для описания взаимодействия с объектами при помощи стандартных операций и встроенных функций. 

Описание специальных методов называется перегрузкой операторов (operator overloading).

Имена специальных методов выделены слева и справа двумя символами подчёркивания. 

Как можно заметить, метод \_\_init__ также является специальным.

Рассмотрим назначение некоторых специальных методов.

+ Метод \_\_repr__ вызывается стандартной функцией repr и возвращает строку, которая является представлением объекта в формате инициализации. 
    
    Этот метод может быть также полезен, если необходимо вывести информацию об объектах, когда они являются элементами коллекции.

## Методы для операций сравнения:
+ \_\_lt__(self, other) – <;
+ \_\_le__(self, other) – <=;
+ \_\_eq__(self, other) – ==;
+ \_\_ne__(self, other) – !=;
+ \_\_gt__(self, other) – >;
+ \_\_ge__(self, other) – >=.

Метод \_\_call__(arg1, arg2, ...) вызывается, когда сам объект вызывается как функция с аргументами.

## Методы для работы с объектом как с коллекцией:
+ \_\_getitem__(self, key) используется для получения элемента коллекции по ключу self[key];
+ \_\_setitem__(self, key, value) используется для записи значения по ключу self[key] = value;
+ \_\_delitem__(self, key) используется для удаления ключа и соответствующего ему значения;
+ \_\_len__(self) вызывается стандартной функцией len
+ \_\_contains__(self, item) вызывается при проверке принадлежности значения item объекту-коллекции self с помощью оператора in.

## Математические операции:
+ \_\_add__(self, other) – self + other;
+ \_\_sub__(self, other) – self - other;
+ \_\_mul__(self, other) – self * other;
+ \_\_matmul__(self, other) – self @ other;
+ \_\_truediv__(self, other) – self / other;
+ \_\_floordiv__(self, other) – self // other;
+ \_\_mod__(self, other) – self % other;
+ \_\_divmod__(self, other) – divmod(self, other);
+ \_\_pow__(self, other) – self ** other;
+ \_\_lshift__(self, other) – self << other;
+ \_\_rshift__(self, other) – self >> other;
+ \_\_and__(self, other) – self & other;
+ \_\_xor__(self, other) – self ^ other;
+ \_\_or__(self, other) – self | other;
+ \_\_radd__(self, other) – other + self;
+ \_\_rsub__(self, other) – other - self;
+ \_\_rmul__(self, other) – other * self;
+ \_\_rmatmul__(self, other) – other @ self;
+ \_\_rtruediv__(self, other) – other / self;
+ \_\_rfloordiv__(self, other) – other // self;
+ \_\_rmod__(self, other) – other % self;
+ \_\_rdivmod__(self, other) – divmod(other, self);
+ \_\_rpow__(self, other) – other ** self;
+ \_\_rlshift__(self, other) – other << self;
+ \_\_rrshift__(self, other) – other >> self;
+ \_\_rand__(self, other) – other & self;
+ \_\_rxor__(self, other) – other ^ self;
+ \_\_ror__(self, other) – other | self;
+ \_\_iadd__(self, other) – self += other;
+ \_\_isub__(self, other) – self -= other;
+ \_\_imul__(self, other) – self *= other;
+ \_\_imatmul__(self, other) – self @= other;
+ \_\_itruediv__(self, other) – self /= other;
+ \_\_ifloordiv__(self, other) – self //= other;
+ \_\_imod__(self, other) – self %= other;
+ \_\_ipow__(self, other) – self **= other;
+ \_\_ilshift__(self, other) – self <<= other;
+ \_\_irshift__(self, other) – self >>= other;
+ \_\_iand__(self, other) – self &= other;
+ \_\_ixor__(self, other) – self ^= other;
+ \_\_ior__(self, other) – self |= other.

Покажем отличие методов математических операций с буквами r и i в начале имени от методов, без этих букв:

    class A:

        def __init__(self):
            self.value = 10

        def __add__(self, other):
            return "Выполняется метод __add__."

        def __radd__(self, other):
            return "Выполняется метод __radd__."

        def __iadd__(self, other):
            self.value += other
            return self

        def __str__(self):
            return f"value: {self.value}."

            
    a = A()
    print(a + 1)
    print(1 + a)
    a += 1
    print(a)

Вывод программы:

    Выполняется метод __add__.
    Выполняется метод __radd__.
    value: 11.

Для операции a + 1 был использован метод \_\_add__. 

Для операции 1 + a был использован метод \_\_radd__. 

А для операции += использован \_\_iadd__. 

Обратите внимание: при выполнении методов, начинающихся с буквы i недостаточно только изменить атрибуты объекта, нужно ещё вернуть объект из метода, иначе в объект запишется None.

Напишем метод \_\_repr__ для класса ElectricCar:

    def __repr__(self):
        return f"ElectricCar('{self.color}', " \
            f"{self.consumption}, " \
            f"{self.bat_capacity}, " \
            f"{self.mileage})"

Код для проверки работы метода:

    electric_car = ElectricCar(color="белый", consumption=15, bat_capacity=90)
    print(repr(electric_car))
    electric_car_1 = ElectricCar(color="чёрный", consumption=17, bat_capacity=80)
    print([electric_car, electric_car_1])

Вывод программы:

    ElectricCar('белый', 15, 90, 0)
    [ElectricCar('белый', 15, 90, 0), ElectricCar('чёрный', 17, 80, 0)]

Опишем операцию сложения для объектов класса ElectricCar: 
+ возвращается новый объект класса ElectricCar, у которого:
    + цвет такой же как у левого слагаемого, а 
    + уровень заряда батареи, 
    + ёмкость батареи, 
    + расход энергии на 100 км пути и 
    + общий пробег вычисляется как сумма соответствующих атрибутов слагаемых объектов:

    def __add__(self, other):
        new_car = ElectricCar(self.color,
                            self.consumption + other.consumption,
                            self.bat_capacity + other.bat_capacity,
                            self.mileage + other.mileage)
        new_car.reserve = self.reserve + other.reserve
        return new_car

Код для проверки метода:

    electric_car = ElectricCar(color="белый", consumption=15, bat_capacity=90)
    electric_car_1 = ElectricCar(color="чёрный", consumption=17, bat_capacity=80)
    electric_car.start_engine()
    electric_car_1.start_engine()
    electric_car.drive(300)
    electric_car_1.drive(100)
    new_electric_car = electric_car + electric_car_1
    print(new_electric_car)

Вывод программы:

    Электромобиль. Цвет: белый. Пробег: 200 км. Остаток заряда: 138.0 кВт*ч.

## Ещё по теме

Полный список специальных методов с описанием можно посмотреть в документации.

https://docs.python.org/3/reference/datamodel.html#special-method-names