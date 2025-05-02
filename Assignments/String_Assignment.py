# 1. Write a program to reverse a string in Python.  
def qn1(st):
    return st[::-1]



# 2. Write a program to count vowels and consonants in a string.  
def qn2(st):
    vowels = 0
    consonants = 0
    st = st.lower()
    for i in st:
        if i >= 'a' and i <= 'z':
            if i in 'aeiou':
                vowels+=1
            else:
                consonants+=1
                
    return f"Vowels : {vowels} \nConsonants : {consonants}"



# 3. Write a program to remove duplicates in a string.  
def qn3(st):
    st = list(st)
    result = set(st)
    ans = ''.join(result)
    return ans



# 4. Write a program to count the number of letters in a word.  
def qn4(st):
    count = 0
    for i in st:
        if i.isalpha():
            count+=1
    return count



# 5. Write a Python program to count the occurrence of each character in a word.  
def qn5(st):
    count = {} # Using disctionary
    for i in st:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    
    # To display the occurrences character-wise
    for i in count:
        print(f'{i} : {count[i]}')
    return 'Done'



# 6. Write a Python program to convert lower letters to upper and upper letters to lower in a string.  
def qn6(st):
    if st.islower():
        return st.upper()
    elif st.isupper():
        return st.lower()
    else:
        for i in range(len(st)):
            if st[i].isupper():
                st = st[:i] + st[i].lower() + st[i+1:]
            elif st[i].islower():
                st = st[:i] + st[i].upper() + st[i+1:]
    return st

# Without using isupper() and islower() explicitly
st='hello'
newStr = ""
for char in st:
    if 'a' <= char <= 'z':
        newStr += chr(ord(char) - 32)  # Convert lowercase to uppercase
    elif 'A' <= char <= 'Z':
        newStr += chr(ord(char) + 32)  # Convert uppercase to lowercase
    else:
        newStr += char
print(f"Converted case string (without isupper() and islower()): {newStr}")


# 7. Write a Python program to search for a specific word in a string.  
def qn7(st):
    word = input("Enter word to search : ")
    
    if word in st:
        return f'{word} is present in {st} at index {st.index(word)}' 
    else:
        return f'{word} is not present in {st}' 



# 8. Write a Python program to sort letters of a word by lower to upper case format.  
def qn8(st):
    lower = ''
    upper = ''
    for i in st:
        if i.islower():
            lower+=i
        else:
            upper+=i
                
    return lower + upper


# Using built-in sorted() directly by case
sorted_st = ''.join(sorted(st, key=str.islower))
print(f"Sorted letters (using sorted() and key=str.islower): {sorted_st}")


# 9. Write a program in Python to count lower, upper, numeric, and special characters in a string.  
def qn9(st):
    lower = 0
    upper = 0
    numeric = 0
    special = 0
    
    for i in st:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
        elif i.isnumeric():
            numeric+=1
        else:
            special+=1
    
    return f"Lower : {lower} \nUpper : {upper} \nNumeric : {numeric} \nSpecial : {special}"
        
# Using list comprehension
lower = len([c for c in st if c.islower()])
upper = len([c for c in st if c.isupper()])
numeric = len([c for c in st if c.isnumeric()])
special = len([c for c in st if not c.isalnum()])
print(f"Lower: {lower}, Upper: {upper}, Numeric: {numeric}, Special: {special}")

# Using built-in sum() for each type
lower = sum(1 for c in st if c.islower())
upper = sum(1 for c in st if c.isupper())
numeric = sum(1 for c in st if c.isnumeric())
special = sum(1 for c in st if not c.isalnum())
print(f"Lower: {lower}, Upper: {upper}, Numeric: {numeric}, Special: {special}")



# 10. Write a program in Python to remove an empty character from a list sequence.  
def qn10(lst):
    newList = []
    for i in lst:
        if i ==' ':
            lst.remove(i)

    return lst
    

# Using list comprehension
newList = [item for item in lst if item != ' ']
print(f"List without empty spaces (using list comprehension): {newList}")

# Using built-in filter()
newList = list(filter(lambda x: x != ' ', lst))
print(f"List without empty spaces (using filter()): {newList}")





# 11. Write a program to make a new string with all the consonants deleted from the string "Hello, have a good day".
def qn11(st):
    newSt = ''
    
    for i in st:
        if i.isalpha():
            if i in 'aeiouAEIOU':
                newSt+=i
        else:
            newSt+=i
    return newSt

# Using list comprehension
newSt = ''.join([char for char in st if char.lower() in 'aeiou' or not char.isalpha()])
print(f"String with consonants deleted (using list comprehension): {newSt}")

# Using built-in string join() and filtering consonants
newSt = ''.join(c for c in st if c.lower() in 'aeiou' or not c.isalpha())
print(f"String with consonants deleted (using join()): {newSt}")





# To test all the Functions
st = input("Enter a String : ")
print('\n')
print('QN-1')
print(f'Reverse of "{st}" is :', qn1(st))
print('\n')

print('QN-2')
print(st, '\n' , qn2(st))
print('\n')

print('QN-3')
print(qn3(st))
print('\n')

print('QN-4')
print(f'No. of letters in "{st}" is : ', qn4(st))
print('\n')

print('QN-5')
print(qn5(st))
print('\n')

print('QN-6')
print(qn6(st))
print('\n')

print('QN-7')
# print(qn7(st))
print('\n')

print('QN-8')
print(qn8(st))
print('\n')

print('QN-9')
print(qn9(st))
print('\n')


print('QN-10')
lst = ['hello', 'world', ' ', 'this', 'is', ' ', 'python', 'class']
print('Original List :', lst)
print('\nList after removing empty spaces:')
print(qn10(lst))
print('\n')

print('QN-11')
strData = "Hello, have a good day"
print(qn11(strData))
print('\n')


print('Thank You!')