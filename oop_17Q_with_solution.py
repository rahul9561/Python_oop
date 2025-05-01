
# 1. Car class with attributes
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)


# 2. BankAccount with encapsulation
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# 3. Inheritance: Animal, Dog, Cat
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"


# 4. Polymorphism: make_sound()
def make_sound(animal):
    print(animal.sound())

make_sound(Dog())
make_sound(Cat())


# 5. Abstraction using abstract class Shape
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# 6. Employee class with display_details()
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")


# 7. Method overriding: Vehicle, Bike
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def move(self):
        print("Bike is moving fast")


# 8. Class vs Instance variables
class Student:
    count = 0  # class variable

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 9. Calculator with static methods
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y if y != 0 else "Division by zero"


# 10. Product with class method from_string()
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, product_str):
        name, price = product_str.split(",")
        return cls(name, float(price))


# 11. Person with __str__ and __repr__
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person(name={self.name}) - user friendly"

    def __repr__(self):
        return f"Person('{self.name}') - debugging view"


# 12. Multiple inheritance
class Writer:
    def write(self):
        print("Writing...")

class Singer:
    def sing(self):
        print("Singing...")

class Personality(Writer, Singer):
    pass


# 13. Property decorator: Temperature
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9


# 14. Singleton class using metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Instance created")


# 15. Using super() to access parent methods
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")


# 16. Order class with getters/setters
class Order:
    def __init__(self, order_id, amount):
        self.__order_id = order_id
        self.__amount = amount

    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount


# 17. Library class to manage books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
        else:
            print("Book not found")

    def list_books(self):
        for book in self.books:
            print(book)
