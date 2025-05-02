# Inheritance
# Definition: The process of inheriting the properties from one class to another is called inheritance.
# In python, there are five types of inheritance:
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance
# 4. Hierarchical inheritance
# 5. Hybrid inheritance

# 1. Single inheritance
# Definition: When a child class inherits only a single parent class is known as single inheritance.
# Example:
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in child class.")

object = Child()
object.func1()
object.func2()

# 2. Multiple inheritance
# Definition: When a child class inherits from more than one parent class is called multiple inheritance.
# Example:
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

# 3. Multilevel inheritance
# Definition: In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and grandfather.
# Example:
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


        
        