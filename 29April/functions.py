# two types of functions - user defined and built in functions
"""
# this is used for documentation or logic explaiination
"""
# we can acess the above doc using .__doc__
def test():
    '''example docstring'''
    print("test")
test()
print(test.__doc__)

# types of arguments
"""
default - NOTE- default not to be the first arg
positional - 
keyword 
arbitrary - *args and **kwargs
"""
#........................................default...........................................
def test1(a,b=10):
    print(a+b)
    return
test1(1)
test1(1,2)

#.........................................keyword............................................
def test2(a,b,c):
    print("a, ",a)
    print("b, ",b)
    print("c, ",c)
test2(b=10,a=15,c=12)

#.............................................arbitrary......................................
def test3(*args): #args is tuple 
    for i in args:
        print(i)
    print(type(args))
    print(sum(args))

test3(1,2,3,4)

def test4(**kwargs): #does not takes positional arguments ...also kwargs is dict type
    print(sum(kwargs))
test4(1,2,3,4,a=10)
