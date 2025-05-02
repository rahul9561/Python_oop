# 1.Write a Python program to sum all the items
print('\nQN-1')
lst = [1, 2, 3, 4, 5]
sum = 0
for i in lst:
    sum +=i
print("Sum of all items in the list:", sum)




# 2. Write a Python program to multiply all the items in a list
print('\nQN-2')
lst = [1, 2, 3, 4, 5]
product = 1
for i in lst:
    product *= i
print("Product of all items in the list:", product)




# 3.Write a Python program to get the largest number from a list
print('\nQN-3')
lst = [1, 2, 3, 4, 5]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print("Largest number in the list:", largest)




# 4. Write a Python program to get the smallest number from a list
print('\nQN-4')
lst = [1, 2, 3, 4, 5]
smallest = lst[0]
for i in lst:
    if i<smallest:
        smallest = i
print("Smallest number in the list:", smallest)




# 5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
print('\nQN-5')
lst = ['a', 'ab', 'abcs', 'xyz', 'aba', '1221']

new_lst = []
for i in lst:
    if len(i) >= 2 and i[0] == i[-1]:
        new_lst.append(i)
print("Strings with length 2 or more and first and last character are same:", new_lst)

# Using List Comprehension
nlst = [ i for i in lst if len(i)>=2 and i[0] == i[-1]]
print("Strings with length 2 or more and first and last character are same:", new_lst)




# 6.Write a Python program to remove duplicates from a list
print('\nQN-6')
lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print("List before removing duplicates:", lst)

new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print("List after removing duplicates:", new_lst)




# 7.Write a Python program to find the list of words that are longer than n from a given list of words
print('\nQN-7')
lst = ['a', 'ab', 'abcs', 'hello', 'xyz', 'aba', 'world', '1221']
n = 4
new_lst = [i for i in lst if len(i) > n]
print("Words longer than", n, ":", new_lst)




# 8.Write a Program that get two lists as input and check if they have at least one common member
print('\nQN-8')
lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 56, 7, 44, 9]
common = False
for i in lst1:
    for j in lst2:
        if i==j:
            common = True
            break
if common:
    print("Lists have at least one common member")
else:
    print("Lists do not have any common members")
    
    
for i in lst1:
    if i not in lst2:
        continue
    else:
        print("Lists have at least one common member")
        break
        
    
# Using List Comprehension
common = [i for i in lst1 if i in lst2]
if common:
    print("Lists have at least one common member")
else:
    print("Lists do not have any common members")




# 9.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
print('\nQN-9')
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List before removing elements:", lst)
lst.remove(lst[0])
lst.remove(lst[4])
lst.remove(lst[5])
print("List after removing elements:", lst)
print('\n')



# 10.Write a Python program to find the second smallest number in a list
print('\nQN-10')
lst = [1, 2, 10, 2, 3, 4, 5, 5, 6]

# Using Set and Sorting
print("Original List: ", lst)
newlst = list(set(lst))
newlst.sort()
print("Second Smallest Number: ", newlst[1])



smallest = second_smallest = float('inf')
for i in lst:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i
if second_smallest == float('inf'):
    print("No second smallest number found")
else:
    print("Second smallest number in the list:", second_smallest)
print('\n')
    



# 11. Write a Python program to find the second largest number in a list
print('\nQN-11')

# Using Set and Sorting
print("Original List: ", lst)
newlst = list(set(lst))
newlst.sort(reverse=True)
print("Second Largest Number: ", newlst[1])


largest = second_largest = float('-inf')
for i in lst:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
if second_largest == float('inf'):
    print("No second Largest number found")
else:
    print("Second Largest number in the list:", second_largest)
print('\n')
    




# 12. Write a Python program to check if the list contains three consecutive common numbers in Python
print('\nQN-12')
lst = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(lst) - 2):
    if lst[i] == lst[i+1] == lst[i+2]:
        print("List contains three consecutive common numbers : ", lst[i])
        break
else:
    print("List does not contain three consecutive common numbers")
print('\n')




# 14. Take form user string data calculate how many vowels avilable count each word wise?
print('\nQN-14')
string = input("Enter a string: ")

vowels = 'aeiouAEIOU'
lst = string.split()
print(lst)

for i in lst:
    count = 0
    for j in i:
        if j in vowels:
            count += 1
    print(f"Number of vowels in  '{i}' : {count}")

