# Write a Python program to sum all the items
# 2. Write a Python program to multiply all the items in a list
# 3.Write a Python program to get the largest number from a list
# 4. Write a Python program to get the smallest number from a list
# 5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
# 6.Write a Python program to remove duplicates from a list
# 7.Write a Python program to find the list of words that are longer than n from a given list of words
# 8.Write a Program that get two lists as input and check if they have at least one common member
# 9.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
# 10.Write a Python program to find the second smallest number in a list
# 11. Write a Python program to find the second largest number in a list
# 12.Write a Python program to check if the list contains three consecutive common numbers in Python
# 13.Write a Python Program to Add Space between Potential Words
# 14-wrp take form user string data calculate how many vowels avilable count each word wise?


lst = [1,2,4,5,6,6,7,8,77,7]
sumi = 0
for i in lst:
    sumi+=i
print("q1 answer : sum of items in list: ",sumi)

#.........................................................
#q2
multi = 1
for i in lst:
    multi*=i
print("q2 answer : multiplication : ",multi)

#q3........................................................
maxi = float('-inf')
for i in lst:
    maxi = max(maxi,i)
print("q3 answer: largest value : ",maxi)

#q4...............................................
mini = float('+inf')
for i in lst:
    maxi = min(maxi,i)
print("q3 answer: smallest value : ",maxi)

#q5.........................................................
count = 0
words_list = ['abc', 123,'xyz', 'aba', '1221']
for word in words_list:
    if isinstance(word, str) and len(word) >= 2 and word[0] == word[-1]:
        count += 1
print("q4 answer : string with more than 2 len: ",count)

#q6.............................................................
unique = []
for item in lst:
    found = False
    for u in unique:
        if u == item:
            found = True
            break
    if not found:
        unique.append(item)
print("q6 answer : unique list : ",unique)

#q7.............................................................
n = int(input("enter the size of the word desired: "))
result = []
for word in words_list:
    if isinstance(word,str) and len(word) > n:
        result.append(word)
print("q7 answer : words longer than n : ",result)

#q8................................................................
def has_common(list1, list2):
    for item in list1:
        for elem in list2:
            if item == elem:
                return True
    return False

list1 = []
list2 = []
list1Size = int(input("enter the size for list 1: "))
for i in range(0,list1Size):
    temp = eval(input("enter the data for list 1: "))
    list1.append(temp)
list2Size = int(input("enter the size for list 2: "))
for i in range(0,list2Size):
    temp = eval(input("enter the data for list 2: "))
    list2.append(temp)
print("q8 answer : atlease one common member",has_common(list1, list2))

#q9..............................................................
def remove_elements(lst):
    result = []
    for i in range(len(lst)):
        if i != 0 and i != 4 and i != 5:
            result.append(lst[i])
    return result

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print("q9 answer: after removing 0th 4th and 5th: ",remove_elements(lst))

#q10................................................................
def second_smallest(lst):
    smallest = float('inf')
    second = float('inf')
    for num in lst:
        if num < smallest:
            second = smallest
            smallest = num
        elif num < second and num != smallest:
            second = num
    return second

lst = [5, 1, 8, 3, 2]
print("q10 second smallest number is : ",second_smallest(lst))

#q11............................................................
def second_largest(lst):
    largest = float('-inf')
    second = float('-inf')
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

lst = [5, 1, 8, 3, 2]
print("q11 answer: second largest number",second_largest(lst))

#q12.........................................................

def three_consecutive(lst):
    for i in range(len(lst) - 2):
        if lst[i] == lst[i+1] and lst[i+1] == lst[i+2]:
            return True
    return False

lst = [1, 2, 2, 2, 3, 4]
print("q12 answer: 3 consecutive common number: ",three_consecutive(lst))

#q13...........................................................
def add_spaces(s):
    result = ""
    for ch in s:
        if ch.isupper() and result:
            result += " "
        result += ch
    return result

s = input("Enter the string without spaces: ")
print("q13 answer: String with spaces:", add_spaces(s))
#q14...........................................................
def count_vowels_wordwise(s):
    vowels = 'aeiouAEIOU'
    words = s.split()
    for word in words:
        count = 0
        for ch in word:
            if ch in vowels:
                count += 1
        print("q14 answer: Word:", word, "Vowel Count:", count)

s = input("Enter a sentence: ")
count_vowels_wordwise(s)

