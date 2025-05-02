# Questions on Dictionary

# 1. Access Nested Dictionary :- Given data = {'a': {'b': {'c': 42}}}
print("\n\nQuestion-1")
dict1 = {'a': {'b': {'c': 42}}}
print("dict1['a']['b']['c'] : ", dict1['a']['b']['c'])




# 2. Merge Two Dictionaries
print("\n\nQuestion-2")
dict2 = {'a': 1, 'b': 2}
dict3 = {'b':0, 'c': 3, 'd': 4}
merged_dict = dict2.copy()
merged_dict.update(dict3)
print("Merged Dictionary : ", merged_dict)

# Other Way
merged_dict1 = dict2 | dict3
print("Merged Dictionary : ", merged_dict1)




# 3. Invert a Dictionary
print("\n\nQuestion-3")
original_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

newDict = {}
for key, value in original_dict.items():
    newDict[value] = key
print("Inverted Dictionary : ", newDict)

# Using Dictionary comprehension
inverted_dict = {value: key for key, value in original_dict.items()}
print("Inverted Dictionary : ", inverted_dict)




# 4. Find Key with Maximum Value
# In a dictionary of numbers, find the key that has the maximum value.
print("\n\nQuestion-4")
dict4 = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
print("Dictionary : ", dict4)

max_value = dict4['a']
key_with_max_value = None

for key, value in dict4.items():
    if value > max_value:
        max_value = value
        key_with_max_value = key
        
print(f"The key '{key_with_max_value}' has the maximum value '{max_value}'.")




# 5. Group Items by First Letter
# Given a list of words, group them in a dictionary by their first letter.
print("\n\nQuestion-5")
lst = ['apple', 'banana', 'bull', 'cherry', 'date', 'elderberry']
grouped_dict = {}
for word in lst:
    first_letter = word[0]
    if first_letter not in grouped_dict:
        grouped_dict[first_letter] = word
    else:
        grouped_dict.update(dict({first_letter:[word]}))
        
print("Grouped Dictionary : ", grouped_dict)




# 6. Count Frequency of Elements
# Write a program to count how many times each element appears in a list using a dictionary.
print("\n\nQuestion-6")
lst = [1, 2, 3, 1, 1, 4,  6, 4, 3, 5, 3, 4, 5]

count_dict = {}
unique_lst = set(lst)

for i in unique_lst:
    count = 0
    for j in lst:
        if i == j:
            count += 1
    count_dict[i] = count

print("Count Dictionary : ", count_dict)




# 7. Dictionary Comprehension Challenge
# Create a dictionary where the keys are numbers from 1 to 5 and the values are their cubes.
print("\n\nQuestion-7")
cube_dict = { i:i**3 for i in range(1, 6)}
print("Cube Dictionary (key:value^3) : ", cube_dict)


