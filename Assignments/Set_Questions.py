
# 1. Create a set with some elements and print all items.
def qn_1():
    print('QN-1')
    my_set = {1, 2, 3, 4, 5}
    print("Set :", my_set)
    print("Set elements:")
    for item in my_set:
        print(item)
    print('\n')




# 2. Add an element to a set using add().
def qn_2():
    set2 = {1, 2, 3}
    print("Set before adding element:", set2)
    set2.add(4)
    print("Set after adding element:", set2)
    



# 3. Given two sets, perform union, intersection, difference, and symmetric difference.
def qn_3():
    setA = {1, 2, 3, 4}
    setB = {3, 4, 5, 6}
    print("Set A:", setA)
    print("Set B:", setB)
    print("Union:", setA.union(setB))
    print("Intersection:", setA.intersection(setB))
    print("Difference (A - B):", setA.difference(setB))
    print("Difference (B - A):", setB.difference(setA))
    print("Symmetric Difference:", setA.symmetric_difference(setB))




# 4. Write a program to remove duplicates from a list using a set.
def qn_4():
    lst = [1, 2, 3, 4, 5, 1, 2]
    print("List with duplicates:", lst)
    lst = list(set(lst))  # Convert to set to remove duplicates, then back to list
    print("List without duplicates:", lst)




# 5. Write a program to count the number of unique characters in a string using a set.
def qn_5():
    str1 = "hello world"
    print("String:", str1)
    unique_chars = set(str1)  # Convert string to set to get unique characters
    print("Unique characters:", unique_chars)
    print("Number of unique characters:", len(unique_chars))




# 6. Write a function to find common elements in three sets.
def qn_6():
    setA = {1, 2, 3, 4}
    setB = {2, 3, 4, 5, 6}
    setC = {2, 4, 5, 6, 7}
    print("Set A:", setA)
    print("Set B:", setB)
    print("Set C:", setC)
    commonElements = setA.intersection(setB, setC)
    print("Common elements:", commonElements) # OR: setA.intersection(setB).intersection(setC)

    
    

# 7. Given a sentence, find all unique words using a set.
def qn_7():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    uniqueWords = set(words)
    print("Sentence:", sentence)
    print("Unique words:", uniqueWords)
    print("Number of unique words:", len(uniqueWords))




# 8. Given two lists, use sets to find elements that are only in the first list but not in the second.
def qn_8():
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [3, 4, 5, 6, 7]
    print("List 1:", lst1)
    print("List 2:", lst2)
    # Using set operation(difference() method)
    set1 = set(lst1).difference(set(lst2))
    print("Elements only in List 1:", list(set1))
    
    # Using Loop
    newLst = []
    for i in lst1:
        if i not in lst2:
            newLst.append(i)
    print("Elements only in List 1:", newLst)




# 9. Write a function to remove all elements from one set that are present in another set.
def qn_9():
    setA = {1, 2, 3, 4, 5}
    setB = {3, 4, 5, 6, 7}
    print("Set A:", setA)
    print("Set B:", setB)

    newSet = setA.difference(setA.intersection(setB))
    print("Set A after removing common elements:", newSet)
    
    
            

# 10. Given a dictionary of users and their favorite fruits, use sets to find the common fruits liked by all users.
def qn_10():
    dict1 = {
        'user1': {'apple', 'banana'},
        'user2': {'banana', 'orange'},
        'user3': {'grape', 'kiwi', 'banana'}
    }

    common = set(dict1['user1'])
    for i in dict1.items():
        # print(list(i)[1])
        common.intersection_update(list(i)[1])

    # Checking if there is any fruits common among all users or not
    if len(common):
        print("Common fruits liked by all users:", common)
    else:
        print("No common fruits found.")
        



# 11. Create a function that returns True if two strings share any common characters (use sets).
def qn_11():
    str1 = 'Hello World'
    str2 = 'Python Class'
    print("String 1:", str1)
    print("String 2:", str2)
    set1 = set(str1)
    set2 = set(str2)
    if set1.intersection(set2):
        return True
    else:
        return False
    



# 12. Write a function that returns the set of vowels used in a given sentence.
def qn_12():
    sentence = 'This is our Python Class'
    print("Sentence:", sentence)
    vowels = set('aeiouAEIOU')
    vowelsInSentence = set(sentence).intersection(vowels)
    print("Vowels in Sentence:", vowelsInSentence)
    
    
    

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Driver Code

print('QN-1')
qn_1()
print('\n')


print('QN-2')
qn_2()
print('\n')


print('QN-3')
qn_3()
print('\n')


print('QN-4')
qn_4()
print('\n')


print('QN-5')
qn_5()
print('\n')


print('QN-6')
qn_6()
print('\n')


print('QN-7')
qn_7()
print('\n')


print('QN-8')
qn_8()
print('\n')


print('QN-9')
qn_9()
print('\n')


print('QN-10')
qn_10()
print('\n')


print('QN-11')
if qn_11():
    print("\"True\", Common Characters Found!")
else:
    print("\"False\", No Common Characters Found!")
print('\n')


print('QN-12')
qn_12()
print('\n')