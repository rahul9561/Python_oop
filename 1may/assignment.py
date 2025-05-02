# 1. Create a class `Car` with attributes `brand`, `model`, and `year`. Instantiate two car objects.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

# Instantiate two car objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Tesla", "Model 3", 2023)

# Print their details
print(f"Car 1: {car1.brand} {car1.model} ({car1.year})")
print(f"Car 2: {car2.brand} {car2.model} ({car2.year})")

# 2. Write a class `BankAccount` that encapsulates balance and provides methods `deposit()` and `withdraw()`. Use private attributes.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Balance:", account.get_balance())  

#3

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        print(super().sound())
        return "Meow"

cat1 = Cat()
print(cat1.sound())


# 4. 

def make_sound(animal):
    print(animal.sound())

make_sound(Dog())   
make_sound(Cat())   

# 5. 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 6. Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")

# 7. Method Overriding
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def move(self):
        print("Bike is moving")

bike1 = Bike()
bike1.move()

# 8. Class vs Instance Variables
class Student:
    count = 0  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable
        Student.count += 1

Student1 = Student("utkarsh")
print(Student.count)
print(Student1.name)

# 9. Calculator with Static Methods
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b if b != 0 else 'Undefined'

print(Calculator.add(2,3))
print(Calculator.subtract(2,3))
print(Calculator.multiply(2,3))
print(Calculator.divide(2,3))

# 10. Product with Class Method
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.price = price

    @classmethod
    def from_string(cls, product_str):
        name, price = product_str.split(',')
        return cls(name.strip(), float(price.strip()))

    def get(self):
        return self.__name,self.price
    

obj11 = Product.from_string("utkarsh,12")
print(obj11.get())
# print(obj11.name)
# 11. __str__ vs __repr__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

# Usage
p = Person("Alice", 30)
print(str(p))    # Friendly
print(repr(p))   # Debugging

#12 - 


class Writer:
    def write(self):
        return "Writing..."

class Singer:
    def sing(self):
        return "Singing..."

class Personality(Writer, Singer):
    def show_talent(self):
        return f"{self.write()} and {self.sing()}"

man = Personality()
print(man.sing())
print(man.write())
print(man.show_talent())

# 13. Property Decorator
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

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

t1 = Temperature(50)
t1.celsius = 12
print(t1.celsius)

# 14. Singleton using Metaclass
class SingletonMeta(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 42

# 15. super() usage
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

# 16. Private Attributes with Getters and Setters
class Order:
    def __init__(self, item, quantity):
        self.__item = item
        self.__quantity = quantity

    def get_item(self):
        return self.__item

    def set_item(self, item):
        self.__item = item

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

# 17. Library Class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def list_books(self):
        return self.books
