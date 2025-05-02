# *** List ***
'''
 Definition: A list is a collection of items that are ordered and changeable. Allows duplicate members. It's Mutable. It's represented by square brackets [].

#  Heterogeneous: Lists can contain items of different data types, such as integers, strings, and other lists.
 
#  Ordered: The order of the items in a list is preserved, meaning you can access them using their index positions.

#  Mutable: Lists can be modified after creation, allowing you to add, remove, or change items.

#  Changeable: Lists can be changed in place, meaning you can modify the contents of a list without creating a new one.

# Syntax: list = [item1, item2, item3]
'''
# Example: list = [1, 2, 3, 4, 5]
# Example: list = ["apple", "banana", "cherry"]
# Example: list = [1, "apple", 3.14, True]

# Access the elements of a list
# Syntax: list[index]
# Example: list[0] # returns the first element of the list
lst = [1, 2.4, 'hi', 1, True, [1, 2, 3], (1, 2), {1: 'one', 2: 'two'}, None]
print(lst)
print(type(lst)) # returns <class 'list'>


# Length of the list - len() function
print("Length : ", len(lst)) # returns length of the list
print(lst[0]) # returns 1
print(lst[-4]) 
print()
print()
print()


# Slicing works with lists too
print(lst[1:4]) # returns [2.4, 'hi', 1]

# print(dir(list)) # returns all the methods and attributes of the list class
# print(help(list)) # returns the documentation of the list class

## CRUD Operations on list
# Create: Creating a list - append(), extend(), insert()
# Read: Accessing elements - index(), count()
# Update: Modifying elements - copy(), reverse(), sort()
# Delete: Removing elements - remove(), pop(), clear()

lst1 = [1, 2.4, 'hi', 1, True, [1, 3], (1, 2), {1: 'one', 2: 'two'}, None]
print(lst1)

# append() - Adds an item to the end of the list
lst1.append(100)
print(lst1)

# extend() - Adds multiple items to the end of the list
lst1.extend([200, 300])
print(lst1)

# insert(position, value) - Adds an item at a specified index
lst1.insert(2, 1000) # adds 1000 at index 2
print(lst1)
print()
print()

# count(item) - Returns the number of occurrences of a specified item in the list
print(lst1.count(1)) # returns 2

# index(item) - Returns the index of the first occurrence of a specified item in the list
print(lst1.index(1)) # returns 0
print()
print()

# reverse() - Reverses the order of the list
print('reverse()')
lst1.reverse() # reverses the list
print(lst1)
print()

lst1 = [1, 2, 30, 4, 5, 6, 7, 8, 9, 1000]
# sort() - Sorts the list in ascending order
print("Sorting the Data")
print('sort()')
lst1.sort() # sorts the list in ascending order
print(lst1)
lst1.sort(reverse = True) # sorts the list in descending order
print(lst1)
print()

# copy() - Returns a shallow copy of the list
print('copy()')
lst2 = lst1.copy() # creates a copy of the list
print(lst2)
print(id(lst1), id(lst2)) # returns the memory address of the list
print()


print('pop()')
# pop() - Removes the last item from the list and returns it
lst1.pop(2) # removes the item at index 2
lst1.pop() # removes the last item from the list
print(lst1)
print()


# remove(item) - Removes the first occurrence of a specified item from the list
print('remove()')
lst1.remove(1000) # removes 1000 from the list
print(lst1)
print()

# clear() - Removes all items from the list
print('clear()')
lst1.clear() # removes all items from the list
print(lst1) # returns []
print()



# List Comprehension - A concise way to create lists using a single line of code
# Syntax: [expression for item in iterable if condition]
# Example: squares = [x**2 for x in range(10)] # creates a list of squares of numbers from 0 to 9

# Without List Comprehension
sq = []
for i in range(1, 11):
    if i%2 == 0:
        sq.append(i**2)
print(sq)

# With List Comprehension
sq = [i**2 for i in range(1, 11)]
print(sq)

# Squares of even numbers from 1 to 10
sq = [i**2 for i in range(1, 11) if i%2==0]
print(sq)

# multiple conditions in list comprehension
sq = [i**2 for i in range(1, 11) if i%2==0 if i%3==0]
print(sq)
# multiple conditions in list comprehension with if-else
sq = [i**2 if i%2==0 else i for i in range(1, 11)]
print(sq)

# --------------------------------------------------------
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output : [4, 8, 12, 16, .......]

b = []
for i in a:
    b.append(i*4)
print(b)

# Separate Odd and Even Numbers from the given list
odd = []
even = []
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
print("Odd numbers are: ", odd)
print("Even numbers are: ", even)