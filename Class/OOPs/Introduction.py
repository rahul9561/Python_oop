# Object Oriented Programming (OOP) in Python
'''
    # Definition: OOP is a programming paradigm that uses objects and classes to design applications.

    # Object-oriented programming (OOP) is a computer programming model that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.
'''

# Class and Objects in Python
# Definition : A class is a blueprint for the object.
class Student:
    pass
obj = Student()
print(type(obj))
print(id(obj))
print(Student.__doc__)


# Types of Variables
# 1. Static/Class level variables: Variables which are declared inside the class but outside the methods are called static/class level variables.
# They can be accessed by all the instances of that class.

# 2. Instance/Object Level Variables: These are those variables which are declared inside any method but outside constructor.
# They can only be accessed by using an instance/object of that class.

# 3. Local Variables: These are those variables which are declared inside any function/method.
# They can only be accessed within that particular function/method.

# Example to show all 3 types of variables:

class Car:
    # 🔹 Class/Static Variable (shared across all instances)
    wheels = 4

    def __init__(self, brand, model):
        # 🟡 Instance Variables (unique for each object)
        self.brand = brand
        self.model = model

    def show_details(self):
        # Instance method using instance variables
        print(f"Car: {self.brand} {self.model}, Wheels: {Car.wheels}")

    @classmethod
    def update_wheels(cls, new_wheel_count):
        # Class method to modify static/class variable
        cls.wheels = new_wheel_count


# Create two instances
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Show instance variables
car1.show_details()  # Toyota Corolla, Wheels: 4
car2.show_details()  # Honda Civic, Wheels: 4

# ✅ Accessing and modifying static variable via class
Car.update_wheels(5)

# Now both cars have updated wheel count
car1.show_details()  # Toyota Corolla, Wheels: 5
car2.show_details()  # Honda Civic, Wheels: 5

# You can access static variable directly using class name
print(Car.wheels)     # 5
print('\n')
# --------------------------------------------------------------------------

# Class Methods
# Definition: A class method is a method which is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
# It can modify a class state that would apply across all the instances of the class.

# Example:
class Circle:
    pi = 3.14
    wheel = 4

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def change_pi(cls, new_pi):
        cls.pi = new_pi

    @classmethod
    def wheel():
        return Circle.wheel

    def calculate_area(self):
        return Circle.pi * self.radius ** 2


# Create a Circle instance
circle1 = Circle(5)
print(Circle.wheel())
print()

