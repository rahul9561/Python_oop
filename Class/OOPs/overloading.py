# Function Overloading
# Definition : When we have multiple functions with same name but different parameters, then such type of function is called overloaded function.


# Example : 

def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c


print(add(10, 20))
print(add(10, 20, 30))