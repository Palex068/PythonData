# 5.1. Объектная модель Python. Классы, поля и методы

Прежде чем приступить к теории, давайте решим следующую задачу.

Напишем программу, которая будет моделировать объекты класса "автомобиль". 

При моделировании необходимо определить степень детализации объектов, которая зависит от действий, выполняемых этими объектами.

+ Пусть все автомобили имеют разный цвет.
+ Двигатель можно запустить, если в баке есть топливо.
+ Двигатель можно заглушить.
+ На автомобиле можно отправиться в путь на N километров при соблюдении следующих условий:
    + двигатель запущен и 
    + запас топлива в баке и
    + средний расход позволяют проехать этот путь.
+ После поездки запас топлива уменьшается в соответствии со средним расходом.
+ Автомобиль можно заправить до полного бака в любой момент времени.

Выделим важные для нашей программы свойства объектов класса:
+ цвет,
+ средний расход топлива,
+ объём топливного бака,
+ запас топлива,
+ общий пробег.

Определим, какие действия может выполнять объект:
+ запустить двигатель,
+ проехать N километров,
+ остановить двигатель,
+ заправить автомобиль.

Пока наши знания позволяют использовать в качестве объекта в программе словарь.

Попробуем описать объекты этого класса с помощью коллекций и функций:

    def create_car(color, consumption, tank_volume, mileage=0):
        return {
            "color": color,
            "consumption": consumption,
            "tank_volume": tank_volume,
            "reserve": tank_volume,
            "mileage": mileage,
            "engine_on": False
        }


    def start_engine(car):
        if not car["engine_on"] and car["reserve"] > 0:
            car["engine_on"] = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."


    def stop_engine(car):
        if car["engine_on"]:
            car["engine_on"] = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."


    def drive(car, distance):
        if not car["engine_on"]:
            return "Двигатель не запущен."
        if car["reserve"] / car["consumption"] * 100 < distance:
            return "Малый запас топлива."
        car["mileage"] += distance
        car["reserve"] -= distance / 100 * car["consumption"]
        return f"Проехали {distance} км. Остаток топлива: {car['reserve']} л."


    def refuel(car):
        car["reserve"] = car["tank_volume"]


    def get_mileage(car):
        return f"Пробег {car['mileage']} км."


    def get_reserve(car):
        return f"Запас топлива {car['reserve']} л."


    car_1 = create_car(color="black", consumption=10, tank_volume=55)

    print(start_engine(car_1))
    print(drive(car_1, 100))
    print(drive(car_1, 100))
    print(drive(car_1, 100))
    print(drive(car_1, 300))
    print(get_mileage(car_1))
    print(get_reserve(car_1))
    print(stop_engine(car_1))
    print(drive(car_1, 100))

Вывод программы:

    Двигатель запущен.
    Проехали 100 км. Остаток топлива: 45.0 л.
    Проехали 100 км. Остаток топлива: 35.0 л.
    Проехали 100 км. Остаток топлива: 25.0 л.
    Малый запас топлива.
    Пробег 300 км.
    Запас топлива 25.0 л.
    Двигатель остановлен.
    Двигатель не запущен.

Мы описали все действия над объектом с помощью функций. 

Такой подход в программировании называется процедурным и долго время был популярным. 

Он позволяет эффективно решать простые задачи. 

Однако при усложнении задачи и появлении новых объектов процедурный подход приводит к дублированию и ухудшению читаемости кода.

# Объектно-ориентированное программирование (ООП)

Объектно-ориентированное программирование (ООП) позволяет устранить недостатки процедурного подхода. 

Язык программирования Python является объектно-ориентированным. 

Это означает, что каждая сущность (переменная, функция и так далее) в этом языке является объектом определенного класса. 

Ранее мы говорили, что, например, целое число является в Python типом данных int. 

На самом деле есть класс целых чисел int.

Убедимся в этом, написав простую программу:

    print(type(1))

Вывод программы:

    <class 'int'>

Синтаксис создания класса в Python выглядит следующим образом:

    class <ИмяКласса>:
        <описание класса>

Имя класса по стандарту PEP8 записывается в стиле CapWords (каждое слово с прописной буквы).

Давайте перепишем пример про автомобили с использованием ООП. 

Создадим класс Car и пока оставим в нём инструкцию-заглушку pass:

    class Car:
        pass

В классах описываются свойства объектов и действия объектов или совершаемые действия над ними.

Свойства объектов называются атрибутами. 

По сути атрибуты — переменные, в значениях которых хранятся свойства объекта. 

Для создания или изменения значения атрибута необходимо использовать следующий синтаксис:

    <имя_объекта>.<имя_атрибута> = <значение>

Действия объектов называются методами. 

Методы очень похожи на функции, в них можно передавать аргументы и возвращать значения с помощью оператора return, но вызываются методы после указания конкретного объекта. 

Для создания метода используется следующий синтаксис:

    def <имя_метода>(self, <аргументы>):
        <тело метода>

# self 

В методах первым аргументом всегда идёт объект self. 

Он является объектом, для которого вызван метод. 

self позволяет использовать внутри описания класса атрибуты объекта в методах и вызывать сами методы.

Во всех классах Python есть специальный метод \_\_init()__, который вызывается при создании объекта. 

В этом методе происходит инициализация всех атрибутов класса. 

В методы можно передавать аргументы. 

Вернёмся к нашему примеру и создадим в классе метод \_\_init()__, который будет при создании автомобиля принимать его свойства как аргументы:

    class Car:

        def __init__(self, color, consumption, tank_volume, mileage=0):
            self.color = color
            self.consumption = consumption
            self.tank_volume = tank_volume
            self.reserve = tank_volume
            self.mileage = mileage
            self.engine_on = False

Итак, мы создали класс автомобилей и описали метод \_\_init__() для инициализации его объектов. Для создания объекта класса нужно использовать следующий синтаксис:

    <имя_объекта> = <ИмяКласса>(<аргументы метода __init__>)

Создадим в программе автомобиль класса Car. 

Для этого добавим следующую строку в основной код программы после описания класса, отделив от класса согласно PEP8 двумя пустыми строками:

    car_1 = Car(color="black", consumption=10, tank_volume=55)

Обратите внимание: наш код стало легче читать, потому что мы видим, что создаётся объект определённого класса, а не просто вызывается функция, из которой возвращается значение-словарь.

Опишем с помощью методов какие действия могут совершать объекты класса Car. 

По PEP8 между объявлением методов нужно поставить одну пустую строку.

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


    car_1 = Car(color="black", consumption=10, tank_volume=55)
    print(car_1.start_engine())
    print(car_1.drive(100))
    print(car_1.drive(100))
    print(car_1.drive(100))
    print(car_1.drive(300))
    print(f"Пробег {car_1.get_mileage()} км.")
    print(f"Запас топлива {car_1.get_reserve()} л.")
    print(car_1.stop_engine())
    print(car_1.drive(100))

Вывод программы:

    Двигатель запущен.
    Проехали 100 км. Остаток топлива: 45.0 л.
    Проехали 100 км. Остаток топлива: 35.0 л.
    Проехали 100 км. Остаток топлива: 25.0 л.
    Малый запас топлива.
    Пробег 300 км.
    Запас топлива 25.0 л.
    Двигатель остановлен.
    Двигатель не запущен.

Обратите внимание: взаимодействие с объектом класса вне описания класса осуществляется только с помощью методов и прямого доступа к атрибутам не происходит. 

Этот принцип ООП называется инкапсуляцией.

# Инкапсуляция 

Инкапсуляция заключается в сокрытии внутреннего устройства класса за интерфейсом, состоящим из методов класса. 

Это необходимо, чтобы не нарушать логику работы методов внутри класса. 

Если не следовать принципу инкапсуляции и попытаться взаимодействовать с атрибутами напрямую, то могут происходить изменения, которые приведут к ошибкам. 

Например, если в нашем примере попытаться изменить пробег напрямую, а не с помощью метода drive(), то автомобиль проедет указанный путь даже с пустым баком и без расхода топлива:

    car_1 = Car(color="black", consumption=10, tank_volume=55)
    car_1.mileage = 1000
    print(f"Пробег {car_1.get_mileage()} км.")
    print(f"Запас топлива {car_1.get_reserve()} л.")

Вывод программы:

    Пробег 1000 км.
    Запас топлива 55 л.

Давайте напишем ещё один класс для электромобилей. Их отличие будет заключаться в замене топливного бака на заряд аккумуляторной батареи:

    class ElectricCar:

        def __init__(self, color, consumption, bat_capacity, mileage=0):
            self.color = color
            self.consumption = consumption
            self.bat_capacity = bat_capacity
            self.reserve = bat_capacity
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
                return "Малый заряд батареи."
            self.mileage += distance
            self.reserve -= distance / 100 * self.consumption
            return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

        def recharge(self):
            self.reserve = self.bat_capacity

        def get_mileage(self):
            return self.mileage

        def get_reserve(self):
            return self.reserve

# Полиморфизм

Напишем функцию range_reserve(), которая будет определять для автомобилей классов Car и ElectricCar запас хода в километрах. 

Функции, которые могут работать с объектами разных классов, называются полиморфными. 

А сам принцип ООП называется полиморфизмом.

Чтобы функция работала для объектов обоих классов, необходимо предусмотреть одинаковый интерфейс в классах. 

Это означает, что методы классов, используемые в функции, должны называться одинаково, принимать одинаковые аргументы и возвращать значения одного типа данных.

Запас хода в километрах можно вычислить, разделив запас топлива (или заряд батареи) на расход и умножив результат на 100. 

Определить запас топлива или заряд батареи можно с помощью метода get_reserve(). 

Для соблюдения принципа инкапсуляции добавим метод get_consumption() в оба класса для получения значения атрибута consumption. 

Тогда полиморфная функция запишется так:

    def range_reserve(car):
        return car.get_reserve() / car.get_consumption() * 100

Полностью программа с классами, полиморфной функцией и пример их использования представлена ниже:

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


    class ElectricCar:

        def __init__(self, color, consumption, bat_capacity, mileage=0):
            self.color = color
            self.consumption = consumption
            self.bat_capacity = bat_capacity
            self.reserve = bat_capacity
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
                return "Малый заряд батареи."
            self.mileage += distance
            self.reserve -= distance / 100 * self.consumption
            return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

        def recharge(self):
            self.reserve = self.bat_capacity

        def get_mileage(self):
            return self.mileage

        def get_reserve(self):
            return self.reserve

        def get_consumption(self):
            return self.consumption


    def range_reserve(car):
        return car.get_reserve() / car.get_consumption() * 100


    car_1 = Car(color="black", consumption=10, tank_volume=55)
    car_2 = ElectricCar(color="white", consumption=15, bat_capacity=90)
    print(f"Запас хода: {range_reserve(car_1)} км.")
    print(f"Запас хода: {range_reserve(car_2)} км.")

Вывод программы:

    Запас хода: 550.0 км.
    Запас хода: 600.0 км.

В нашей программе можно заметить, что классы Car и ElectricCar имеют много общих атрибутов и методов. Это привело к дублированию кода. В следующей главе мы познакомимся с наследованием — принципом ООП, позволяющим устранить подобную избыточность кода.