# 1. write program where take input numbers of student and student name and percentage and print in dict 
print('QN-1')
n = int(input('Enter number of students : '))
stud_data = {}

i = 1
while i <= n:
    name = input(f'Enter name of student {i} : ')
    percentage = float(input(f'Enter percentage of student {i} : '))
    stud_data[name] = percentage
    i += 1
    
print('Student Data : ')
print(stud_data)
print('\n')




# 2. Write program to add all key and values of dict
print('QN-2')
n = int(input('Enter number of elements to add in dictionary : '))
dict1 = {}
i = 1
while i <= n:
    key = input(f'Enter key {i} : ')
    value = input(f'Enter value {i} : ')
    dict1[key] = value
    i += 1
print('Dictionary : ', dict1)

print('\n')

# 3. Write a Python program to add a key to a dictionary
print('QN-3')
n = int(input('Enter number of elements to add in dictionary : '))
i = 1
lst = []
while i <= n:
    val = input("Enter a value : ")
    lst.append(val)
    i += 1
print("List : ", lst)

key = [i for i in range(1, len(lst)+1)]
print("Keys : ", key)

newdict = {}
i=0
n = len(lst)
while i<n:
    newdict[key[i]] = lst[i]
    i +=1
    
print("New Dictionary : ", newdict)
print('\n')




# 4. Write a Python program to check whether a given key already exists in a dictionary
print('QN-4')
dict2 = {'a':1,'b':2, 'c':3}
print('Dictionary : ', dict2)

key = input('Enter key to check : ')
if key in dict2:
    print(f'Key {key} already exists in dictionary')
else:
    print(f'Key {key} does not exist in dictionary')
print('\n')

# Other Methods to check key in dictionary(Using loop)
for i in dict2.keys():
    if i == key:
        print(f'Key {key} already exists in dictionary')
        break
else:
    print(f'Key {key} does not exist in dictionary')
print('\n')




# 5. Write a Python program to iterate over dictionaries using for loops.
print('QN-5')
for i in dict2.keys():
    print(f'Key : {i} , Value : {dict2[i]}')
print('\n')

# Other methods to iterate over dictionary
for i in dict2.items():
    print(f'Key : {i[0]} , Value : {i[1]}')
print('\n')

# Using Key and Value in items()
for key, value in dict2.items():
    print(f'Key : {key} , Value : {value}')
print('\n')




# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
print('QN-6')
n = int(input('Enter a number : '))
dict3 = {}
for i in range(1, n+1):
    dict3[i] = i*i
print('Dictionary : ', dict3)
print('\n')

# Using Dict Comprehension to generate dictionary
dict4 = {i: i*i for i in range(1, n+1)}
print('Dictionary : ', dict4)
print('\n')




# 7. Write a Python script to merge two Python dictionaries
print('QN-7')
dict5 = {'a':1, 'b':2}
dict6 = {'c':3, 'd':4}
print('Dictionary 1 : ', dict5)
print('Dictionary 2 : ', dict6)
dict5.update(dict6)
print('Merged Dictionary : ', dict5)
print('\n')




# 8. Write a Python program to iterate over dictionaries using for loops
print('QN-8')
print('Dictionary : ', dict4)
for i in dict4:
    print(f'Key : {i} , Value : {dict4[i]}')
print('\n')

# Using items() to iterate over dictionary
for i in dict4.items():
    print(f'Key : {i[0]} , Value : {i[1]}')
print('\n')

# Using Key and Value in items()
for key, value in dict4.items():
    print(f'Key : {key} , Value : {value}')
print('\n')

# Using keys()
for i in dict4.keys():
    print(f'Key : {i} , Value : {dict4[i]}')
print('\n')




# 9. Write a Python program to sum all the items in a dictionary
print('QN-9')
print('Dictionary : ', dict4)
sum = 0
for i in dict4.values():
    sum += i
print('Sum of all items in dictionary : ', sum)
print('\n')




# 10. Drop empty Items from a given Dictionary
print('QN-10')
dict1 = {'a': 1, 'b': 0, 'c': 3, 'd': 0}
print('Dictionary before removing empty items : ', dict1)
newdict = {}
for i in dict1:
    if dict1[i] != 0:
        newdict[i] = dict1[i]
print('Dictionary after removing empty items : ', newdict)
print('\n')



# 11. Write a Python program to count number of items in a dictionary value that is a list
print('QN-11')
dict7 = {'a': [1, 2, 3], 'b':2, 'c': [4, 5], 'd':'Hello', 'e': [6, 7, 8, 9]}
print('Dictionary : ', dict7)
count = 0
for i in dict7.values():
    if isinstance(i, list):
        count += 1
print('Count of items in dictionary value that is a list : ', count)
print('\n')




# 12. Write a Python script to sort (ascending and descending) a dictionary by key.
print('QN-12')
dict8 = {'a': 1, 'b': 2, 'e':5,'c': 3, 'd': 4}
print('Dictionary : ', dict8)
print('Dictionary sorted in ascending order : ', dict(sorted(dict8.items())))
print('Dictionary sorted in descending order : ', dict(sorted(dict8.items(), reverse=True)))
print('\n')




# 13. Match key values in two dictionaries
print('QN-13')
dict9 = {'a': 1, 'b': 2, 'c': 3}
dict10 = {'a': 1, 'b': 2, 'c': 3, 'd':4}
print('Dictionary 1 : ', dict9)
print('Dictionary 2 : ', dict10)

if dict9 == dict10:
    print('Both dictionaries are same')
else:
    print('Both dictionaries are different')
print('\n')

# Other methods to match key values in two dictionaries
for i in dict9.keys():
    if i in dict10.keys():
        if dict9[i] == dict10[i]:
            print(f'Key : {i} , Value : {dict9[i]} is same in both dictionaries')
        else:
            print(f'Key : {i} , Value : {dict9[i]} is different in both dictionaries')
    else:
        print(f'Key : {i} does not exist in dictionary 2')
print('\n')
print('\n')




# 14. Access dictionary key’s element by index
print('QN-14')
dict14 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print('Dictionary : ', dict14)
print('Keys : ', dict14.keys())
print('Values : ', dict14.values())
print('Items : ', dict14.items())
print('First key : ', list(dict14.keys())[0])
print('First value : ', list(dict14.values())[0])
print('First item : ', list(dict14.items())[0])

# Using Loop to access dictionary key's element by index
print('Keys :')
dictList = list(dict14.keys())
for i in range(len(dictList)):
    print(dictList[i], end = " ")
print('\n')




# 15. Write a program to convert a list of dictionaries into a dictionary of lists.
print('QN-15')
dict15 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
print('List of dictionaries : ', dict15)
dict16 = {}

for i in dict15:
    if isinstance(i, dict):
        for key, value in i.items():
            if key not in dict16:
                dict16[key] = [value]
            else:
                dict16[key].append(value)
print('Dictionary of lists : ', dict16)
print('\n')
            