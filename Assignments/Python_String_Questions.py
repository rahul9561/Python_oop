'''1. What is a string in Python?
Ans: A string is a sequence of characters used to store text. Strings are immutable, meaning you can’t change them once created.
Example: 'Hello', "World", etc'''



'''2. How do you create a string in Python? 
Ans: You create a string by putting characters inside single (' ') or double (" ") quotes.
Example: 'hello', "world".'''



'''3. What is the difference between single and double quotes in strings? 
Ans: There’s no difference in functionality. Use single quotes if the string contains double quotes and vice versa, to avoid using escape characters.'''



'''4. How can you access characters in a string? 
Ans: Access characters using zero-based indexing in square brackets [].
Example'''
s = "hello"
s[0]    # 'h'
s[-1]   # 'o'



'''5. What is string slicing in Python?
Ans: String slicing extracts substrings using [start:end:step].
Example:''' 
s = "hello"
s[1:4]    # 'ell'
s[:3]     # 'hel'
s[::-1] # 'olleh' (reverses the string)



'''6. How do you find the length of a string? 
Ans: Find the length of a string using the len() function.
Example:'''
print(len("hello")) # returns 5



'''7. What is string concatenation? 
Ans: String concatenation in Python is the process of combining two or more strings into a single string. The most common way to achieve this is by using the + operator. 
Example:'''
print("Hello" + " " + "World")   # 'Hello World'



'''8. How do you convert a string to uppercase or lowercase? 
Ans: Use .upper() for uppercase and .lower() for lowercase.
Example:''' 
print("Python".upper()) # "PYTHON"
print("PYTHON".lower()) # "python"



'''9. What is the purpose of the strip() method? 
Ans: It removes spaces (or other characters) from the beginning and end of a string.

 - strip() removes both ends
 - lstrip() removes from the left
 - rstrip() removes from the right'''
str1 = "  hello  "
print(str1.strip())   # 'hello'
print(str1.lstrip())  # 'hello  '
print(str1.rstrip())  # '  hello'



'''10. How do you replace a substring in a string?
Ans: To replace a substring within a string in Python, Use .replace(old, new) to replace part of a string.'''
str1 = "Hello World"
print(str1.replace("World", "Python")) # "Hello Python".



'''11. What is the difference between find() and index() methods? 
Ans: find() returns the first index of a substring or '-1' if not found. 
index() does the same but raises a 'ValueError' if not found.'''
print("abc".find("b")) # 1
print("abc".find("x")) # -1
print("abc".index("b")) # 1
# print("abc".index("x")) # ValueError



'''12. How can you check if a string contains a specific substring? 
Ans: You can check if a string contains a specific substring in Python using the 'in' keyword. 
'''
print("Python" in "Hello Python") # True



'''13. What is string formatting in Python? 
Ans: String formatting in Python is the process of embedding expressions inside string literals. You can use %, .format(), or f-strings.'''
name = "Ram"
print("Hello, {}".format(name))     # 'Hello, Ram'
 


'''14. What are f-strings in Python? 
Ans: F-strings are the modern and clean way to format strings using {}''' 
name= 'Ram'
age=22
print(f"{name} is {age} years old.") # 'Ram is 22 years old.'



'''15. How do you split a string into a list? 
Ans: You can split a string into a list of substrings in Python using the .split() method. By default, if you don't provide any arguments, the split() method splits the string at whitespace characters (spaces, tabs, newlines). 
However, you can also specify a delimiter as an argument, and the string will be split at each occurrence of that delimiter.'''
print("a,b,c".split(",")) # ['a', 'b', 'c']



'''16. How do you join a list of strings into a single string? 
Ans: To join a list of strings into a single string in Python, you use the .join() method. This method is called on a string that will act as the separator between the elements of the list.'''
print(", ".join(['a', 'b', 'c'])) # "a, b, c"



'''17. What is the difference between isdigit(), isnumeric(), and isdecimal()? 
Ans: 
isdigit() checks digits (0-9)

isnumeric() checks all numeric characters, even other symbols like fractions

isdecimal() is strict, like isdigit(), but mostly used in Unicode'''
print("123".isdigit()) # True
print("123".isnumeric()) # True
print("123".isdecimal()) # True



'''18. How can you reverse a string in Python? 
Ans: You can reverse a string in Python using slicing with a step of -1.
Syntax: string[::-1]''' 
print("hello"[::-1]) # 'olleh'



'''19. How do you remove whitespace from a string? 
Ans: You can remove whitespace from a string in Python using the strip(), lstrip(), and rstrip() methods..

strip() - removes from both ends
lstrip() - from the left
rstrip() - from the right
''' 
str1 = "  hello  "
print(str1.strip())   # 'hello'
print(str1.lstrip())  # 'hello  '
print(str1.rstrip())  # '  hello'



'''20. What are raw strings and why are they used?
Ans: Raw strings treat backslashes (\) as normal characters, useful in regular expressions or file paths. Add an r before the string.
'''
print(r"C:\Users\Suraj") # C:\Users\Suraj