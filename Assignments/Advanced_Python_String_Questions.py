'''1. How do you use regular expressions with strings in Python?
Ans: Regular expressions (regex) allow you to match patterns in text. Python provides the 're' module to work with regex.
You can use functions like re.search(), re.match(), re.findall(), re.sub(), etc.
'''

import re

text = "My phone number is 987-654-3210"
pattern = r"\d{3}-\d{3}-\d{4}"

match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())  # Phone number found: 987-654-3210



'''2. What is the difference between mutable and immutable objects, and why are strings immutable?
Ans: 
Mutable objects can be changed after creation (e.g., lists), while immutable objects cannot (e.g., strings, tuples).
Strings are immutable to improve performance and security, especially since they're used heavily in keys, caching, etc.

Example:'''
s = "hello"
# s[0] = "H"   # Error: 'str' object does not support item assignment



'''3. What is the use of the translate() and maketrans() methods?
Ans: maketrans() creates a translation table, and translate() applies it to a string.
Useful for character replacements or deletions.
'''
txt = "hello world"
trans_table = str.maketrans("aeiou", "12345")
print(txt.translate(trans_table))  # h2ll4 w4rld



'''4. How can you efficiently concatenate a large number of strings?
Ans: Use ''.join(list_of_strings) instead of + in loops.
+ creates a new string each time, which is inefficient for large numbers.
'''
words = ["This", "is", "faster", "with", "join"]
print(" ".join(words))  # This is faster with join



'''5. What is the difference between repr() and str() for strings?
Ans: str() is for readable display, repr() is for debugging — it shows how Python would represent the object.
'''
s = "Hello\nWorld"
print(str(s))   # Hello (newline) World
print(repr(s))  # 'Hello\nWorld'



'''6. How can you format strings using the % operator?
Ans: The % operator is an old-style way of formatting strings.
You use format specifiers like %s for string, %d for integers, etc.
'''
name = "Alice"
age = 25
print("My name is %s and I am %d years old." % (name, age))  # My name is Alice and I am 25 years old.



'''7. How does the format() method compare to f-strings?
Ans: Both are used for string formatting.
- format() works in older versions (Python 2.7+)
- f-strings are cleaner and faster (introduced in Python 3.6)
'''
name = "Bob"
print("Hello, {}".format(name))   # using format()
print(f"Hello, {name}")           # using f-string



'''8. How do Unicode and encoding affect strings in Python?
Ans: Python 3 strings are Unicode by default, which means they support multiple languages.
Encoding is how strings are stored/converted (e.g., UTF-8).
You can encode() a string to bytes and decode() bytes back to string.
'''
s = "café"
encoded = s.encode("utf-8")
print(encoded)  # b'caf\xc3\xa9'
print(encoded.decode("utf-8"))  # café



'''9. How do you check if a string is a palindrome?
Ans: A palindrome reads the same forwards and backwards.
You can use slicing or reversed().
'''
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False



'''10. How do you remove punctuation from a string?
Ans: Use string.punctuation and a generator expression or regex.
'''
import string
s = "Hello, world! How are you?"
cleaned = "".join(c for c in s if c not in string.punctuation)
print(cleaned)  # Hello world How are you



'''11. How can you count the frequency of each character in a string?
Ans: Use collections.Counter
'''
from collections import Counter
s = "banana"
freq = Counter(s)
print(freq)  # Counter({'a': 3, 'n': 2, 'b': 1})



'''12. How do you use the zfill() method in strings?
Ans: zfill() pads the string on the left with zeros until it reaches the specified length.
'''
s = "42"
print(s.zfill(5))  # 00042



'''13. What is the difference between rfind() and find()?
Ans: find() returns the first index of the substring. rfind() returns the last occurrence.
If not found, both return -1.
'''
s = "banana"
print(s.find("a"))   # 1
print(s.rfind("a"))  # 5



'''14. What are some common security issues with string input (e.g., code injection)?
Ans: If you take user input and evaluate it or use it in queries without sanitizing, it can lead to security issues:
- Code injection (e.g., eval(input()))
- SQL injection
Always sanitize and validate input.
Example:'''
# Never do this:
# user_input = input("Enter code: ")
# eval(user_input)  # Dangerous

# Instead, use safe parsing, strict typing, and validation.



'''15. What is the use of casefold() and how is it different from lower()?
Ans: casefold() is stronger than lower() — it's meant for caseless matching (international/Unicode text).
Useful for comparing text in different languages or cases.
'''
print("ß".lower())     # ß
print("ß".casefold())  # ss

# Good for: "Straße".casefold() == "strasse".casefold()
