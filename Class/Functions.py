# Functions
'''
# Definition : A function is a block of code which only runs when it is called.
    # You can pass data, known as parameters, into a function.
    # A function can return data as a result.
    # In Python a function is defined using the 'def' keyword:

# Types of Functions:
    # 1. User Defined Function: A user-defined function is created by defining a function using the def keyword.
    
    # 2. Built-in Function: These are predefined functions in python. Examples: print(), len(), sum(), abs(), min(), max() etc.
    
    
# DocString : A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition.
    
Function Syntax :
    def function_name(parameters):
        """docstring"""
        statement(s)
        return expression
'''
def my_function():
    '''This is a docstring. I have created a function'''
    print("Hello from a function")

print(my_function.__doc__) # To print the docstring of a function(using 'dunder' methods: starts with '__')

# To call a function, use the function name followed by parenthesis
my_function()
print('\n')
# ----------------------------------------------------------------------
'''
# Arguments
    # Information can be passed into functions as arguments.
    # Arguments are specified after the function name, inside the parentheses.
    # You can add as many arguments as you want, just separate them with a comma.
    # The following example has a function with one argument (fname).
    # When the function is called, we pass along a first name, which is used inside the function to print the full name:

    # Parameters or Arguments?
    # The terms parameter and argument can be used for the same thing: information that are passed into a function.
'''
def my_function1(fname):
  print("First Name : " + fname)

my_function1("Suraj")
my_function1("Aditya")
my_function1("Abinash")
print('\n')
# ----------------------------------------------------------------------

# Multiple Arguments
def my_function2(fname, lname):
  print("Full Name : " + fname + " " + lname)

my_function2("Suraj", "Sah")
print('\n')
# ----------------------------------------------------------------------


# Types of Parameters/Arguments:
# 1. Position
# 2. Keyword
# 3. Default
# 4. Variable Length/Arbitrary Arguments(*args, **kwargs)

# 1. Positional Argument
# -> The order of passing the arguments matters here.
def my_function3(fname, lname):
  print("Full Name : " + fname + " " + lname)
  
my_function3("Suraj", "Sah")
print('\n')



# 2. Keyword Argument
# -> The order of passing the arguments does not matter here. 
def my_function4(fname, lname):
  print("Full Name : " + fname + " " + lname)
  
  my_function4(lname = "Sah", fname = "Suraj")
print('\n')



# 3. Default Argument
# -> If no value is provided for an argument during the function call, then default values will be taken.
def my_function5(fname, lname = "Sah"):
  print("Full Name : " + fname + " " + lname)
  
my_function5("Suraj")
print('\n')



# 4. Variable Length Argument
# -> We can define a function such that it takes variable number of arguments. This type of argument is also called Arbitrary Arguments.

def my_function6(fname, *lname):
  print("Full Name : " + fname + " " + lname[0] + " " + lname[1])

my_function6("Suraj", "Sah", "Kumar")
print('\n')

# ----------------------------------------------------------------------

# Test
def sum(*args):
    print(type(args))
    print(*args)
    
sum(1,2, 3, 4, 5)


def sum(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['c'])
    
sum(a=2, b=7, c=8)
print('\n\n')

# Mixed
def sum(a, b=10, *args, **kwargs):
    print(type(args), type(kwargs))
    print(a , b)
    print(args)
    print(kwargs)
    
sum(1, 2, 4, 3, d=9)
print('\n\n')

# ----------------------------------------------------------------------

def factorial(num):
    if num==0 or num ==1:
        return 1
    else:
        return num*factorial(num-1)

num = 5
print(f"Factorial of {num} is {factorial(num)}")
    
# ----------------------------------------------------------------------

# Lambda Function
# -> A lambda function is a small anonymous function.
# -> A lambda function can take any number of arguments, but can only have one expression.
# Syntax : lambda argument_list : expression
# Examples: x = lambda a : a + 10 # Returns 10 added to the number given as argument

x = lambda a : a + 10
print(x(5))
print('\n')

x = lambda a, b : a * b
print(x(5, 6))
print('\n')

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# ----------------------------------------------------------------------

# filter() function
# -> The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 
# Use filter() with sequence data types like list, tuple, string etc.

# Syntax: filter(function, iterable)
def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False
    
lst = [1, 2, 3, 4, 5]
even_lst = list(filter(isEven, lst))
print("Odd Numbers : ", even_lst)


# Using Lambda Function
oddlst = list(filter(lambda n:n%2!=0, lst))
print("Odd Numbers : ", oddlst)
print('\n\n')

# ----------------------------------------------------------------------

# map() function
# -> The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# Syntax: map(function, iterable)

l1 = [1, 2, 3, 4, 5]

# Find powers of 2
sq = list(map(lambda n:2**n, l1))

print("Original List : ", l1)
print("Powers of 2 : ", sq)
print('\n\n')

# ----------------------------------------------------------------------

# reduce() function
 # -> The Python reduce() function reduces the multiple arguments into a single value. This function returns an aggregated value by applying it to an iterable. 
 # This starts with the first pair of arguments, then uses the result with the next value.

# Syntax: reduce(func, iterable, initializer)
# It must be imported from 'functools' from functools import reduce | *

from functools import reduce
lst = [1, 2, 3, 4, 5]
allSum = reduce(lambda a, b: a+b, lst)
print(allSum)