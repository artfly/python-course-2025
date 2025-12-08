# Создать класс для собак и для кошек
# Сделать для них базовый класс

# - общий вид классов
# - инфа про конструктор
# - описание: каждый раз новая псина (какие-то коробки с данными?)
# - операции + данные = класс
# - загадка с self (передаем в странном синтаксисе)
# - порядок исполнения программы
# - статические функции (например, отряд собак)
# - базовый класс, поиск методов

# Класс - набор атрибутов
# Атрибуты:
# - поля
# - методы (функции)
# class Some_Name:
#     print('какой-то код...')
#
#     def foo():
#         print("fdfsdfs")

class Animal:
    def say(self):
        print("Животное непонятно как говорит....")

class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f'{self.name}: Meow!')

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def say(self):
        print(f'{self.name}: Woof!')

class Fox(Animal):
    pass

    # Dog.order() -> вызывается order() (без @staticmethod)
    # sobaka1.order() -> вызывается Dog.order(sobaka1) -> перед тем, как вызваться, работает декоратор @staticmethod
    @staticmethod
    def order():
        print("Carnivora!")



f = Fox()
f.say()
sobaka1 = Dog('Шарик', 'дворняжка')
sobaka1.say()

#
# sobaka1 = Dog('Шарик', 'дворняжка')
# sobaka2 = Dog('Бонк', 'типа немецкая овчарка, но так-то дворянин')

# print(sobaka1.name)
# print(sobaka2.name)
# sobaka1.name = "Эдуард"
# print(sobaka1.name)
# print(sobaka2.name)

# Dog.say(sobaka1)
#
# Dog.order()
# sobaka1.say()
#
# sobaka1.order()
#
# cat1 = Cat("Маруся", 0.45)
# cat2 = Cat("Персик", 8)
#
# print(cat1.name)
# cat2.say()

