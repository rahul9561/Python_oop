#q1.....................
n = int(input("enter the number of students: "))
dictt = {}
for i in range(0,n):
    temp = input("enter the name of student: ")
    temp2 = int(input("enter the percentage: "))
    dictt[temp] = temp2
print(dictt)
#q2........................................................
def sum_dict_keys_values(input_dict):
    if not isinstance(input_dict, dict):
        return "Error: Input is not a dictionary"

    if not input_dict:
        return 0

    total_sum = 0
    for key, value in input_dict.items():
        if isinstance(key, (int, float)):
            total_sum += key
        else:
            return None
        if isinstance(value, (int, float)):
            total_sum += value
        else:
            return None

    return total_sum

my_dict = {1: 10, 2: 20, 3: 30}
result = sum_dict_keys_values(my_dict)
print(f"Sum of keys and values: {result}")

#q3..............................................
n = int(input("enter the key you want to insert : "))
my_dict.setdefault(n,None)
print("after inserting a value to dict: ",my_dict)
#q4.....................................
target = eval(input("enter the target that you want to search in the dict: "))
flag = 0
for i in my_dict:
    if i == target:
        flag=1
        break
    
if flag:
    print("exist")
else:
    print("does not exist")

#Q5.........................................
for i in my_dict:
    print(i,end=" ")
    print(my_dict[i])

#q6.............................................
n = int(input("enter the range: "))
newDictt ={}
for i in range(1,n+1):
    newDictt[i] = i*i
print(newDictt)

#Q7
merged_dict = my_dict | newDictt
print(merged_dict)
againDicc = {}
for i in newDictt:
    againDicc[i] = newDictt[i]
print(againDicc)

#q8

for i in againDicc:
    print(i , " : ", againDicc[i])

def q9(my_dict):
    keysSum = 0
    valuesSum = 0
    
    for key, value in my_dict.items():
        if isinstance(key, (int, float)):
            keysSum += key
        if isinstance(value, (int, float)):
            valuesSum += value
    
    print("Keys sum:", keysSum)
    print("Values sum:", valuesSum)

my_dict = {1: 10, 2: 20, 3: 30,22:33,20:22,12:233}
q9(my_dict)



def q10(my_dict):
    for i in my_dict:
        if (my_dict[i]==None):
            my_dict.pop(i)

def q11(d):
    count = 0
    for value in d.values():
        if isinstance(value, list):  
            count += len(value)
    return count

data = {
    'fruits': ['apple', 'banana', 'cherry'],
    'numbers': [1, 2, 3, 4],
    'single_value': 'hello',
    'colors': ['red', 'blue']
}


def q12(my_dict):
    sorted_dict = sorted(my_dict.items(), reverse=True)
    print("after sorting : ", sorted_dict)
    
    sorted_dict = sorted(my_dict.items(), reverse=False)
    print("after sorting reverse : ", sorted_dict)


def q13(dict1, dict2):
    matched_items = {}
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            matched_items[key] = dict1[key]
    
    return matched_items

def q14(new_dictt):
    lstt= []
    for i in new_dictt:
        lstt.append(i)
    for i in lstt:
        print(i)

q9(my_dict)
q10(my_dict)
print("Total count:", q11(data))
q12(my_dict)
new_dictt= {1: 10, 2: 20, 3: 30, 22: 33}
print(q13(my_dict,new_dictt))
q14(new_dictt)


