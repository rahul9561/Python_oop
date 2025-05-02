# In Python, a string is a data structure that represents a sequence of characters. It is an immutable sequence, meaning once a string is created, it cannot be changed.
#.......................................................
#q2)- 
s = "Hello, world!"  # Using double quotes
s = 'Hello, world!'  # Using single quotes

#.......................................................
#q3)- 
#  Double quotes are often used when the string contains single quotes, and vice versa.

#.......................................................
#q4)- 
s = "Python"
print(s[0])  # Output: 'P'
print(s[-1]) # Output: 'n'

#.......................................................
#q5)-
# Extracting a portion of the string:
s = "Python"
print(s[1:4])  

#.......................................................
#q6)-
len("Python")
length = 0
for i in s:
    length+=1
print("length of the string through loop is : ",length)  

#.......................................................
#q7)-
a = "Hello"
b = "World"
print(a + " " + b)

#.......................................................
#q8)-
s = "Hello"
print(s.upper()) 
print(s.lower())  

#.......................................................
#q9)- purpose of the strip method is to strip off the blank or white spaces from left and right of the string
s = "  Hello  "
print(s.strip())  

#.......................................................
#q10)-
# we replace a substring in python using replace string method that replaces the given substring with desired substring
s = "I like Python"
print(s.replace("like", "love")) 

#.......................................................
#q11)-Both return the index of the first occurrence of a substring. But find() returns -1 if not found, while index() raises a ValueError.
s = "hello"
s.find("e")   
s.index("e")  
s.find("z")   

#.......................................................
#q12)-
# method 1
"Python" in "I love Python" 

#.......................................................
#q13)-
#string formatting is the process of Injecting values into a string
name = "Alice"
print("Hello, {}!".format(name))  
print(f"hello, {name}")

#.......................................................
#q14)-
# Formatted string literals 
print(f"Hello, {name}!")  

#.......................................................
#q15)-
s = "a,b,c"
print(s.split(","))  

#.......................................................
#q16)-
lst = ['a', 'b', 'c']
print(",".join(lst))  
newstring = ""
for i in lst:
    newstring+=i
    newstring+=','
print(newstring)

#.......................................................
#q17)-
# isdigit() checks for digits (0–9 and superscripts/subscripts).

# isnumeric() checks for all numeric characters (including fractions, roman numerals).

# isdecimal() is the most strict — only decimal characters (0–9).
print("123".isdigit())
print("123.45".isnumeric())
print("123".isdecimal())

#.......................................................
#q18)-
s = "hello"
print(s[::-1])

for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
print("\n")

#.......................................................
#q19)-
s = "  Hello World  "
print(s.strip())
print(s.replace(" ", ""))  

#.......................................................
#q20)-
# Raw strings treat backslashes (\) as literal characters. Useful in regular expressions and file paths.
print("C:\\new\\folder")


