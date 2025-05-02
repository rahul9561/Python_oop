# 1. Write a program to reverse a string in Python.  
# Using slicing
st = input("Enter a string: ")
reversed_str = st[::-1]
print(f"Reversed string (using slicing): {reversed_str}")

# Using a loop (without slicing)
reversed_str = ""
for char in st:
    reversed_str = char + reversed_str
print(f"Reversed string (using loop): {reversed_str}")

# Using the built-in reversed() and join()
reversed_str = ''.join(reversed(st)) 
print(f"Reversed string (using reversed() and join()): {reversed_str}") 
print()




# 2. Write a program to count vowels and consonants in a string.  
# Using manual iteration and conditions
vowels = 0
consonants = 0
st = st.lower()
for i in st:
    if i >= 'a' and i <= 'z':
        if i in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")

# Using a simple loop and manual checking
vowels = "aeiou"
vowels_count = 0
consonants_count = 0
for i in st:
    if i.isalpha():
        if i in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")
print()




# 3. Write a program to remove duplicates in a string.  
# Without using set, by manually checking characters
result = ""
for char in st:
    if char not in result:
        result += char
print(f"String without duplicates (using loop): {result}")

# Using set (directly removing duplicates)
st = "hello"
result = ''.join(set(st))
print(f"String without duplicates (using set): {result}")

# Using set() and list() method directly on the string
st1 = list(st)
result = set(st1)
ans = ''.join(result)
print(f"String without duplicates (using set): {ans}")
print()





# 4. Write a program to count the number of letters in a word.  
# Using loop and checking with isalpha()
count = 0
for i in st:
    if i.isalpha():
        count += 1
print(f"Number of letters (using loop): {count}")

# Using Len() and isalpha()
count = len(st)
print(f"Number of letters (using len() function): {count}")
print()





# 5. Write a Python program to count the occurrence of each character in a word.  
# Using dictionary to track occurrences
count = {}
for i in st:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for i in count:
    print(f"{i} : {count[i]}")

# Normal way to count the occurrences of each character in a string(using loop and set)
count = 0
st='hello world'
unque = set(st)
for i in unque:
    for j in st:
        if i == j:
            count+=1
    print(f'{i} : {count}')
    count = 0
print()
    
    


# 6. Write a Python program to convert lower letters to upper and upper letters to lower in a string.  
# Using loop and checking case of each letter
st= "Hello World"
newStr = ""
for char in st:
    if char.isupper():
        newStr += char.lower()
    elif char.islower():
        newStr += char.upper()
    else:
        newStr += char
print(f"Converted case string (using loop): {newStr}")

# Using built-in swapcase() function
newStr = st.swapcase()
print(f"Converted case string (using swapcase()): {newStr}")
print()




# 7. Write a Python program to search for a specific word in a string.
# Using `in` keyword and `index()`
word = input("Enter word to search : ")
if word in st:
    print(f'{word} is present in {st} at index {st.index(word)}') 
else:
    print(f"{word} is not found.")

# Using `find()` metho input("Enter word to search: ")
index = st.find(word)
if index != -1:
    print(f"{word} is present at index {index}")
else:
    print(f"{word} is not found.")
print()




# 8. Write a Python program to sort letters of a word by lower to upper case format.  
# Using loop and manual sorting
lower = ''
upper = ''
for i in st:
    if i.islower():
        lower += i
    else:
        upper += i
print(f"Sorted letters (lowercase first, then uppercase): {lower + upper}")
print()




# 9. Write a program in Python to count lower, upper, numeric, and special characters in a string.  
# Using a loop and islower(), isupper(), isnumeric()
lower = 0
upper = 0
numeric = 0
special = 0
for i in st:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
    elif i.isnumeric():
        numeric += 1
    else:
        special += 1
print(f"Lower: {lower}, Upper: {upper}, Numeric: {numeric}, Special: {special}")
print()




# 10. Write a program in Python to remove an empty character from a list sequence.  
# Using loop and manual removal
lst = ['hello', 'world', ' ', 'this', 'is', ' ', 'python', 'class']
newList = []
for i in lst:
    if i != ' ':
        newList.append(i)
print(f"List without empty spaces (using loop): {newList}")

# Directly Removing empty spaces from the list using remove()
for i in lst:
        if i ==' ':
            lst.remove(i)
print(f"List without empty spaces (using remove()): {lst}")
print()




# 11. Write a program to make a new string with all the consonants deleted from the string "Hello, have a good day".
# Using loop and checking for vowels
newSt = ""
for i in st:
    if i.isalpha():
        if i in 'aeiouAEIOU':
            newSt += i
    else:
        newSt += i
print(f"String with consonants deleted (using loop): {newSt}")