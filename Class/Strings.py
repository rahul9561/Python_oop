# Data Types

# Mutable - List, Dictionary, Set [We can change the values in these data types:CRUD Operations]

# Immutable - String, Integers, Floats, Tuples, FrozenSet [We can not change the values in these data types]


# String DataType
# String is a sequence of characters. It is immutable.

s = 'hello'
print(id(s))
s = 'helloWorld'
print(id(s))

# The id of the string changes when we change the value of the string.
# This is because strings are immutable in Python. When we change the value of the string, a new string object is created in memory.

print()
# print(dir(str))
'''
capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
'''

print()
# print(help(str))
print('hi'*5)

# Converting Numeric String to Integer or Float
print(int('12'))
print(float('12'))

'''
Accessing Characters from Strings
 1. Using Index (index())
 2. Using Slice
'''
st1 = 'ESSPL Product Intern Profile'

print(st1[-1:-3:-1])
print(st1[: :-1])

print(f'Length of \'{st1}\' = {len(st1)}')

print(f'Index of \'P\' in \'{st1}\' = {st1.index("P")}')
print()

print('hello world'.capitalize())  # Capitalizes the first character of the string
print()

print(f'Number of Occurrences of \'P\' in \'{st1}\': {st1.count('P')}')  # Counts the number of occurrences of 'P' in the string
print()

print(st1.center(len(st1)+10, '*'))  # Centers the string with '*' on both sides
print()


print(st1.find('P', 4, len(st1)))  # Returns the index of the first occurrence of 'Pl' in the string
print()

print(st1.index('P', 4, len(st1)))  # Returns the index of the first occurrence of 'Pl' in the string
print()

print(st1.rfind('P'))  # Returns the index of the first occurrence of 'Pl' in the string from right side
print()

print(st1.title())  # Converts the first character of each word in the string to uppercase
print()


print(st1.upper())  # Converts the string to uppercase
print()

print(st1.lower())  # Converts the string to lowercase
print()


print(st1.replace('Product', 'Software', 1))  # Replaces 'Product' with 'Software' in the string : 1 is for how many occurrences to replace
print()

print(st1.split(' '))  # Splits the string into a list of words
print()


st1 = 'Hello world \t Python\tprogramming'
print(st1.expandtabs(15))  # Expands the tabs in the string to 15 spaces
print()

print(st1.swapcase())  # Swaps the case of the string
print()

print('    Hello    World'.strip())  # Removes the leading and trailing spaces from the string
print()

print('    Hello    World  .  '.lstrip())  # Removes the leading spaces from the left side of the string
print()

print('.........@  Hello    World  !..............'.rstrip('.'))  # Removes the trailing '.' from the right side of the string
print()


print(', '.join(['Hello', 'World', 'Welcome', 'to', 'Python', 'Class']))  # Joins the list of strings with the string 'st1' in between
print()

print(', '.join('Hello'))
print()

print(st1.ljust(50, '*'))  # Left justifies the string with '*' on the right side
print()

print(st1.rjust(50, '*'))  # Right justifies the string with '*' on the left side
print()

print(st1.zfill(50))  # Pads the string with '0' on the left side to make it 50 characters long
print()



stq = 'Hello world.\n Python programming'

print(stq.split('o'))  # Splits the string into a list
print()

print(stq.splitlines())  # Splits the string into a list of lines
print()


# To check if the string starts with a particular character or not
print(stq.startswith('H'))
print()

# To check if the string ends with a particular character or not
print(stq.endswith('g'))
print()

# To check if the string is alphanumeric or not
print('isalnum() : ', 'Hello123'.isalnum())  # Returns True if all characters in the string are alphanumeric (letters and numbers) and there is at least one character, False otherwise
print()

# To check if the string is alphabetic or not
print('isalpha() : ', 'Hello'.isalpha())  # Returns True if all characters in the string are alphabetic (letters) and there is at least one character, False otherwise
print()

# To check if the string is numeric or not
print('isnumeric() : ', '123'.isnumeric())  
# Returns True if all characters in the string are numeric (numbers) and there is at least one character, False otherwise
print()

# To check if the string is a digit or not
print('isdigit() : ', '123'.isdigit())  # Returns True if all characters in the string are digits (numbers) and there is at least one character, False otherwise
print()

# To check if the string is a decimal or not
print('isdecimal() : ', '123.45'.isdecimal())  
# Returns True if all characters in the string are decimal characters and there is at least one character, False otherwise
print()

# To check if the string is a space or not
print('isspace() : ', ' H'.isspace())  # Returns True if all characters in the string are whitespace characters and there is at least one character, False otherwise
print()

# To check if the string is a title or not
print('istitle() : ', 'hello World'.istitle())  
# Returns True if the string is a titlecased string and there is at least one character, False otherwise
print()

# To check if the string is a lower case or not
print('islower() : ', 'Hello'.islower())
# Returns True if all characters in the string are lowercase and there is at least one character, False otherwise
print()

# To check if the string is a upper case or not
print('isupper() : ', 'HELLo'.isupper())
# Returns True if all characters in the string are uppercase and there is at least one character, False otherwise
print()

# To check if the string is a printable or not
print('if() : ', 'Hello & World'.isprintable())
# Returns True if all characters in the string are printable and there is at least one character, False otherwise
print()






