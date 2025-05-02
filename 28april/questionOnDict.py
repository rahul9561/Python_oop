
def q1():
    data = {'a': {'b': {'c': 42}}}
    print(data['a'])
    print(data['a']['b'])
    print(data['a']['b']['c'])

def q2():
    dict1 = {1:2,2:4,5:6,7:6}
    dict2 = {11:"utkarsh",22:"values",55:"key",77:67}
    dict1 = dict1 | dict2
    print(dict1)

def q3():
    dict3 = {1: 2, 2: 4, 5: 6, 7: 6}
    new_dict = {}

    for i in dict3:
        value = dict3[i]
        new_dict[value] = i

    print(new_dict)

def q4():
    dict3 = {1: 2, 2: 4, 5: 6, 7: 6,8:"123"}
    maxi = float('-inf')
    for i in dict3:
        if isinstance(dict3[i],str) and dict3[i].isdigit():
            maxi = max(int(dict3[i]),maxi)
        elif isinstance(dict3[i],int):
            maxi = max(dict3[i],maxi)
        else:
            continue
    print(maxi)

def q5():
    lst = ["amul","anmol","vaibhav","vinit","utkarsh","utkal"]
    new_dict = {}
    for i in lst:
        if i[0] in new_dict:
            new_dict[i[0]].append(i)
        else:
            new_dict[i[0]] = [i]
    print(new_dict)

def q6():
    lst = [1,2,3,4,3,2,3,3,4,5,44,5,5,4,3,565,54,43,33,22,33,454,55,66]
    new_dict = {}
    for i in lst:
        if i in new_dict:
            new_dict[i]+=1
        else:
            new_dict[i] = 1
    print(new_dict)

def q7():
    new_dict = {i:i*i for i in range(1,6)}
    print(new_dict)


q1()
q2()
q3()
q4()
q5()
q6()
q7()



