#  OOPs Questions

# 1. Create a class `Car` with attributes `brand`, `model`, and `year`. Instantiate two car objects.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

car1.display_info()
print()
car2.display_info()
print('\n')

# --------------------------------------------------------------------------------------


# 2. Write a class `BankAccount` that encapsulates balance and provides methods `deposit()` and `withdraw()`. Use private attributes.
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if self.__balance>=amount:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds.")
            
    def display_balance(self):
        print(f"Current Balance: ${self.__balance}")

account = BankAccount(1000)

account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()
print('\n')

# --------------------------------------------------------------------------------------


# 3. Demonstrate inheritance by creating a base class `Animal` and two subclasses `Dog` and `Cat` with their own `sound()` method.
class Animal:
    def sound(self):
        return "Unknown sound."

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())
print('\n')

# --------------------------------------------------------------------------------------


# 4. Illustrate polymorphism using a method `make_sound()` called on different animal objects.
class Animal:
    def make_sound(self):
        return "Unknown sound."


class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Polymorphic usage: calling make_sound() on different animal objects
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.make_sound())
print('\n')

# --------------------------------------------------------------------------------------


# 5. Use abstraction by defining an abstract class `Shape` with an abstract method `area()` and implement it in `Circle` and `Rectangle` classes.
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(Self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Area of Circle = ", circle.area())
print("Area of Recttangle = ", rectangle.area())
print('\n')

# --------------------------------------------------------------------------------------


# 6. Create a class `Employee` with a constructor and a method `display_details()`. Use `__init__` to initialize values.
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        
emp = Employee('E-1', 'Suraj', 10000)
emp.display_details()
print('\n')

# --------------------------------------------------------------------------------------


# 7. Write a program to demonstrate method overriding with a parent class `Vehicle` and a child class `Bike` that overrides the `move()` method.
class Vehicle:
    def move(self):
        print("Moving...")
        
class Bike(Vehicle):
    def move(self):
        print("Riding bike...")
        
vehicle = Vehicle()
bike = Bike()

vehicle.move() # Calling the move() method of parent class
bike.move() # Overriding the move() method of parent class with its own implementation
print('\n')

# --------------------------------------------------------------------------------------


# 8. Differentiate between class variables and instance variables using a class `Student` with a counter to track the number of students created.
class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1
        
        
student1 = Student("Suraj")
student2 = Student("Sunil")

print(Student.student_count) # Accessing class variable through class name
print(student1.student_count) # Accessing class variable through object
print(student1.name) # Accessing instance variable through object
print('\n')

# --------------------------------------------------------------------------------------


# 9. Implement a `Calculator` class with static methods for add, subtract, multiply, and divide.
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
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."
        
# Accessing static methods without instantiating the class
print("Addition : ", Calculator.add(5, 3))
print("Substraction : ", Calculator.subtract(5, 3))
print("Mulliplication : ", Calculator.multiply(5, 3))
print("Division : ", Calculator.divide(5, 3))
print('\n')

# --------------------------------------------------------------------------------------


# 10. Use class methods in a class `Product` to create objects using alternate constructors like `from_string()`.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    # Class Method as Alternate Constructor
    @classmethod
    def from_string(cls, product_str):
        name, price = product_str.split(" ")
        return cls(name, float(price))
    
    def display_product(self):
        print(f"Product Name: {self.name}, Price: ${self.price}")

# Object creation using alternate constructor
product_str = "Laptop 999.99"
product = Product.from_string(product_str)
product.display_product()
print('\n')

# --------------------------------------------------------------------------------------


# 11. Create a class `Person` with `__str__` and `__repr__` methods. Show how they differ when printing and debugging.
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person(name={self.name}) - user friendly"

    def __repr__(self):
        return f"Person('{self.name}') - debugging view"

person = Person("Suraj")
print(str(person)) # Using str() function
print(repr(person)) # Using repr() function
print('\n')

# --------------------------------------------------------------------------------------


# 12. Demonstrate multiple inheritance with a class `Writer`, `Singer`, and a class `Personality` inheriting both.
class Writer:
    def write(self):
        print("Writing Insightful contents")
    def skill(self):
        print("Skill is writing")
        
class Singer:
    def sing(self):
        print("Singing melodious songs")
    def skill(self):
        print("Skill is singing")
        
class Personality(Writer, Singer):
    def introduce(self):
        print("Hello, I am a personality class!")
        self.skill() # To call the skill method of first inherited class(following MRO: Left-Right)
        
personality = Personality()
personality.write()
personality.sing()
personality.introduce()
print('\n')

# --------------------------------------------------------------------------------------


# 13. Create a property decorator in a class `Temperature` that gets and sets temperature in Celsius and Fahrenheit.
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    # Property Decorator
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation"""
        if value < -273.15:
            return "Temperature below absolute zero is not possible."
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit by converting to Celsius"""
        celsius = (value - 32) * 5/9
        if celsius < -273.15:
            return "Temperature below absolute zero is not possible."
        self._celsius = celsius

    def __repr__(self):
        return f"Temperature(celsius={self._celsius})"
    
temp = Temperature(2)
temp.celsius = 30
print(temp.celsius)
temp.fahrenheit = 96
print(temp.fahrenheit)
print(temp)
print('\n')    
    
# --------------------------------------------------------------------------------------


# 14. Create a singleton class using a metaclass in Python.
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Instance created")
        
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)
print('\n')

# --------------------------------------------------------------------------------------


# 15. Show how to use `super()` to access methods from the parent class in a child class.
class Parent:
    def greet(self):
        print("Hello from Parent")

class IntermediateParent(Parent):
    def greet(self):
        print("Intermediate Parent Greeting")
class Child(IntermediateParent):
    def greet(self):
        super().greet()
        print("Hello from Child")
        
child = Child()
child.greet()
print('\n')

# --------------------------------------------------------------------------------------


# 16. Create a class `Order` with private attributes and use getter and setter methods to modify them.
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

    def __repr__(self):
        return f"Order(order_id={self.__order_id}, amount={self.__amount})"
    
    def display_order(self):
        print(f"Order ID: {self.__order_id}, Amount: ${self.__amount}")

odr = Order(1, 100)
print(odr.get_order_id())
odr.set_order_id(2)
print(odr.get_order_id())

print(odr.get_amount())
odr.set_amount(200)
print(odr.get_amount())

print(odr)
print('\n')
    
# --------------------------------------------------------------------------------------


# 17. Design a class `Library` to manage books. Add methods to `add_book()`, `remove_book()`, and `list_books()`.
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
            
lib = Library()
lib.add_book("Book1")
lib.add_book("Book2")
lib.list_books()
lib.remove_book("Book1")
lib.list_books()
print('\n')

# --------------------------------------------------------------------------------------
