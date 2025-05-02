#  *** Dictionary ***
'''
 # Definition: A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed. No duplicate members. It's Mutable. It's represented by curly braces {}.  

 # Heterogeneous: Dictionaries can contain items of different data types, such as integers, strings, and other dictionaries.

 # Ordered: The order of the items in a dictionary is preserved, meaning you can access them using their keys.

 # Mutable: Dictionaries can be modified after creation, allowing you to add, remove, or change items.

 # Changeable: Dictionaries can be changed in place, meaning you can modify the contents of a dictionary without creating a new one.

 # Syntax: dict = {key1: value1, key2: value2, key3: value3}
 # Example: dict = {'name': 'John', 'age': 30, 'city': 'New York'}
 # Example: dict = {1: 'one', 2: 'two', 3: 'three'}
'''

# print(dir(dict)) # returns all the methods and attributes of the dict class
'''
'clear()', 'copy()', 'fromkeys()', 'get()', 'items()', 'keys()', 'pop()', 'popitem()', 'setdefault()', 'update()', 'values()'
'''
# print(help(dict)) # returns the documentation of the dict class

# CRUD Operations on dict
# Create: Creating a dict - setdefault(), fromkeys()
# Read: Accessing elements - get(), keys(), values(), items()
# Update: Modifying elements - update(), copy()
# Delete: Removing elements - pop(), popitem(), clear()

dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
print(dict1)
print(dict1['name']) # returns 'John'
print()
print()

# setdefault() - Returns the value of a key if it is in the dictionary. If not, inserts the key with a specified value and returns that value.
# Syntax: dict.setdefault(key, default_value)

print("setdefault()")
dict2 = {'name': 'Suraj', 'age': 30, 'city': 'New York', 1: 'one', 2: 'two', 3: 'three'}
print(dict2)
print(dict2.setdefault('name')) # returns 'Suraj'
print(dict2.setdefault('country', 'USA')) # returns 'USA' and adds the key-value pair to the dictionary
print(dict2.setdefault('name', 'ESSPL')) # Does Nothing
print(dict2)
print()

# fromkeys() - Creates a new dictionary from the given keys and a specified value.
# Syntax: dict.fromkeys(keys, value)
print("fromkeys()")
print({}.fromkeys(['name', 'age', 'city'], 8))
print({}.fromkeys(range(10)))
print({}.fromkeys(range(10), 'ESSPL'))
print()

# get() - Returns the value of a specified key. If the key does not exist, it returns None or a specified default value.
# Syntax: dict.get(key, default_value)
print("get()")
print(dict1.get('name')) # returns 'John'
print(dict1.get('country')) # returns None
print()

# items() - Returns a view object that displays a list of a dictionary's key-value tuple pairs.
# Syntax: dict.items()
print("items()")
print(dict1.items())

print(type(dict1.items())) # returns <class 'dict_items'>

print(list(dict1.items())) # returns [('name', 'John'), ('age', 30), ('city', 'New York')]

for i in dict1.items():
    print(i) # returns ('name', 'John') ('age', 30) ('city', 'New York')
print()


# values() - Returns a view object that displays a list of all the values in the dictionary.
# Syntax: dict.values()
print("values()")
print(dict1.values())

print(type(dict1.values())) # returns <class 'dict_values

for i in dict1.values():
    print(i) # returns John 30 New York
print()


# update() - Updates the dictionary with the specified key-value pairs.
# Syntax: dict.update(key_value_pairs)
print("update()")
print(dict1)
dict1.update({'name': 'Suraj', 'age': 35, 'country' : 'Nepal'}) 
print(dict1) # returns {'name': 'Suraj', 'age': 35, 'city': 'New York'}
print()


# copy() - Returns a shallow copy of the dictionary.
# Syntax: dict.copy()
print("copy()")
dict3 = dict1.copy()
print(dict3) # returns {'name': 'Suraj', 'age': 35, 'city': 'New York'}
print()



# pop() - Removes the specified key and returns its value. If the key does not exist, it raises a KeyError.
# Syntax: dict.pop(key, default_value)
print("pop()")
print(dict1)
print(dict1.pop('name')) # returns 'Suraj' and removes the key-value pair from the dictionary
print(dict1) # returns {'age': 35, 'city': 'New York'}
print()
print()


# popitem() - Removes the last inserted key-value pair and returns it as a tuple. If the dictionary is empty, it raises a KeyError.
# Syntax: dict.popitem()
print("popitem()")
print(dict1)
print(dict1.popitem()) # returns ('city', 'New York') and removes the key-value pair from the dictionary
print(dict1) # returns {'age': 35}
print()



# clear() - Removes all items from the dictionary.
# Syntax: dict.clear()
print("clear()")
print(dict1)
print(dict1.clear()) # returns None and removes all items from the dictionary
print(dict1) # returns {}