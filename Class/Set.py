#  *** Set ***
# Definition: A set is a collection of distinct objects, considered as an object in its own right.

# Sets are unordered, unindexed, and do not allow duplicate members. It's Mutable(Partially Immutable, partially mutable). It's represented by curly braces {} or the set() function.

# Insertion order is not preserved, meaning the order of items in a set is not guaranteed to be the same as the order in which they were added.

# Indexing and slicing are not supported in sets, meaning you cannot access items using their index positions.

# Unordered: The order of the items in a set is not preserved, meaning you cannot access them using their index positions. Unordered, unindexed, and does not allow duplicate members. It's Mutable. 

# Heterogeneous: Sets can contain items of different data types, such as integers, strings, and other sets.

# It's represented by curly braces {} or the set() function.

# Syntax: set = {item1, item2, item3}
# Example: set = {1, 2, 3, 4, 5}
# Example: set = {1, "apple", 3.14, True} # Heterogeneous elements

st = {1, 'Hi', (3, '120'), 4, 5.7}
print(st)
print(type(st))

# print(dir(set))
'''
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
'''
# CRUD Operations on set
# Create: Creating a set - add()
# Read: Accessing elements
# Update: Modifying elements - update(), copy()
# Delete: Removing elements - clear(), discard(), pop(), remove()
print('\n')

# add() - Adds an item to the set
print("add()")
st.add(100)
st.add((10, 20))
print(st)
print('\n')

# update() - Adds multiple items to the set
print("update()")
st.update([-10, -20])
st.update({-15, 3})
print(st)
print('\n')


# copy() - Returns a shallow copy of the set
print("copy()")
st1 = st.copy()
print(st1)
print(st1 is st) # returns False
print('\n')


# remove() - Removes an element from the set. Raises KeyError if the element is not found.
print("remove()")
st.remove(100)
print(st)
print('\n')

# discard() - Removes an element from the set. Does not raise an error if the element is not found.
print("discard()")
st.discard(100) # Does Nothing
print(st)
print('\n')

# pop() - Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
print("pop()")
st.pop()
print(st)
print('\n')

# clear() - Removes all elements from the set
print("clear()")
st.clear()
print(st)
print('\n')

# -------------------------------------------------------
print("-------------------------------------------------------")
print("Set Operations")
# Set Operations

# Union: Combines two sets and returns a new set with all unique elements from both sets.
print("Union")

st1 = {1, 2, 3, 4}
st2 = {3, 4, 5}
st3 = st1.union(st2)
print(st3)
print(st1 | st2) # Using the | operator
print('\n')

# Intersection: Returns a new set with elements that are common to both sets.
print("Intersection")
st4 = st1.intersection(st2)
print(st4)
print(st1 & st2) # Using the & operator
print('\n')

# Difference: Returns a new set with elements that are in the first set but not in the second set.
print("Difference")
print(st1.difference(st2))
print(st1 - st2) # Using the - operator
print(st2.difference(st1))
print(st2 - st1) # Using the - operator
print('\n')

# Symmetric Difference: Returns a new set with elements that are in either of the sets, but not in both.
print("Symmetric Difference")
st6 = st1.symmetric_difference(st2)
print(st6)
print(st1 ^ st2) # Using the ^ operator
print('\n')

# issubset(): Checks if all elements of one set are present in another set.
print("issubset()")
st7 = {1, 2}
print(st7.issubset(st1))
print(st1.issubset(st7)) # returns False
print('\n')

# issuperset(): Checks if all elements of another set are present in the first set.

print("issuperset()")
print(st1.issuperset(st7)) # returns True
print(st7.issuperset(st1)) # returns False
print('\n')

# isdisjoint(): Checks if two sets have any common elements.
print("isdisjoint()")
st8 = {5, 6, 7}
print(st1.isdisjoint(st8)) # returns True
print(st1.isdisjoint(st2)) # returns False
print('\n')

# -------------------------------------------------------
print("-------------------------------------------------------")
