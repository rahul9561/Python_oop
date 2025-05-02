def q1(a):
    if a%2==1:
        print("odd")
    else:
        print("even")

def q2(strr):
    vowels = "aeiou"
    for i in strr:
        if i in vowels:
            print("contains vowels ")
            return
    print("does not contain vowels")

def q3():
    dictt = {i:i*i for i in range(1,21)}
    print(dictt)

def q4(dictt):
    for i in dictt:
        print(dictt[i],end=", ")

def q5():
    tupp = (i*i for i in range(1,21))
    print(tuple(tupp))

def q6(strr):
    upperCount = 0
    lowerCount = 0
    for i in strr:
        if i.isupper():
            upperCount+=1
        else:
            lowerCount +=1
    print("upper case count : ",upperCount)
    print("lower case count : ",lowerCount)

q1(10)
vowelContaining = input("enter the string you want to check for: ")
q2(vowelContaining)
q3()


dictt = {i:i*i for i in range(1,21)}
q4(dictt)
q5()
strr = input("enter the string: ")
q6(strr)


def fact(n,i,j):
    if(n<1):
        return
    k = i+j
    i=j
    j=k
    print(k)
    fact(n-1,i,j)

fact(10,0,1)