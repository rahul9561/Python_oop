d = lambda a,b:print(a+b)
d(1,2)
c = lambda a:a%2==1

print(c(10))

# filter - 
# filter(function,Sequences)

lst = [1,2,3,4,5,6,7]
d = lambda a:a%2==0
l2 = list(filter(d,lst))
print(l2)
l2 = list(map(lambda i:i*i ,lst))
print(l2)


from functools import * 
result  = reduce(lambda x,y:x+y,lst)
print(result)

import functions
print("................................................")
print(functions.test())
