# # regex
import re
# Basic Syntax:
# Literal characters: Match exactly as they are.

# Example: r"abc" matches the string "abc".

# . (Dot): Matches any single character except newline (\n).

# Example: r"a.b" matches "acb", "axb", but not "ab".

# ^ (Caret): Matches the beginning of the string.

# Example: r"^abc" matches "abc" only if it's at the start.

# $ (Dollar): Matches the end of the string.

# Example: r"abc$" matches "abc" only if it's at the end.

# * (Asterisk): Matches 0 or more repetitions of the preceding character or group.

# Example: r"ab*c" matches "ac", "abc", "abbc", etc.

# + (Plus): Matches 1 or more repetitions of the preceding character or group.

# Example: r"ab+c" matches "abc", "abbc", but not "ac".

# ? (Question mark): Matches 0 or 1 repetition of the preceding character or group.

# Example: r"ab?c" matches "abc" and "ac".

# {n,m}: Matches between n and m repetitions of the preceding character or group.

# Example: r"ab{2,4}c" matches "abbc", "abbc", "abbbc", but not "abc".

# [] (Square brackets): Matches any one character from a set.

# Example: r"[aeiou]" matches any vowel.

# | (Pipe): Logical OR. Matches either the expression before or the expression after the pipe.

# Example: r"abc|def" matches "abc" or "def".

# () (Parentheses): Groups expressions together.

# Example: r"(abc)+" matches one or more repetitions of "abc".

value = re.findall(r"[0-9]{5,6}[a-z]*","324234khg")
print(value)

# Metacharacters and Special Sequences:
# \d: Matches any digit (equivalent to [0-9]).

# Example: r"\d" matches "1", "9", but not "a".

# \D: Matches any non-digit.

# Example: r"\D" matches "a", "b", but not "1".

# \w: Matches any word character (letters, digits, and underscores).

# Example: r"\w" matches "a", "A", "1", "_".

# \W: Matches any non-word character.

# Example: r"\W" matches "!", " ", "#".

# \s: Matches any whitespace character (spaces, tabs, newlines).

# Example: r"\s" matches " ", "\t", "\n".

# \S: Matches any non-whitespace character.

# Example: r"\S" matches "a", "1", "b" but not " ".


# complex data types 
a = 1+4j
print(type(a))
# float to binary

# float to hex
num = 10.75
hex_rep = num.hex() 
print(hex_rep)  
# int to bin
num = 10
binary_rep = bin(num)  
print(binary_rep)  



# bin to int

binary_str = '1010'
int_rep = int(binary_str, 2)
print(int_rep)

# int to oct

num = 10
octal_rep = oct(num)
print(octal_rep)

# oct to int

octal_str = '12'
int_rep = int(octal_str, 8)
print(int_rep)

# int to hex

num = 10
hex_rep = hex(num)
print(hex_rep)

# hex to int

hex_str = 'a'
int_rep = int(hex_str, 16)
print(int_rep)

# int to char

num = 65
char_rep = chr(num)
print(char_rep)

# char to int

char = 'A'
int_rep = ord(char)
print(int_rep)

# separator
print("Hello", "World", 123, sep="-")

# using end 
print("Hello", end=", ")
print("World")

#flush
print("Hello", flush=True)


print("Hello", "World", 123, sep="-", end="!", flush=True)

# what is d in python
# d is used to represent integer in python

# string.format     
name = "shukla"
age = 25

result1 = "{} is {} years old".format(name, age)
print(result1)

result2 = "{0} is {1} years old".format(name, age)
print(result2)

result3 = "{name} is {age} years old".format(name="Bob", age=30)
print(result3)

