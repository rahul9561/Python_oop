
def q1():
    strr = input("enter the string you wantto check : ")
    i = 0
    j = len(strr)-1
    flag= 1
    while i<=j:
        if(strr[i]==strr[j]):
            i+=1
            j-=1
            continue
        else:
            print("false")
            flag = 0
            break
    if flag==1:
        print("true")


def q2():
    vowel = "aeiou"
    inp_str = input("enter the string you want to extract vowels from: ")
    st = set()
    for i in range(0,len(inp_str)):
        if inp_str[i] in vowel:
            st.add(inp_str[i])
    print("extracted vowels are: ",st)

def q3():
    strr = input("enter the string you want to delete duplicates for: ")
    new_Str = ""
    for i in range(0,len(strr)):
        if strr[i] in new_Str:
            continue
        else:
            new_Str+=strr[i]
    print(new_Str)

def q4():
    strr = input("enter the string for counting the occurences: ")
    strr = sorted(strr)
    new_Str = ""
    count=1
    for i in range(0,len(strr)-1):
        if(strr[i] == strr[i+1]):
            count+=1
        else:
            new_Str+=strr[i]
            new_Str += f"{count}"
            count=1
    new_Str+=strr[len(strr)-1]
    new_Str += f"{count}"
    print(new_Str)

def q5():
    text = input("enter the text for frequeny count: ")
    text = text.lower()
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    clean_text = ''
    for char in text:
        if char not in punctuation:
            clean_text += char
    words = clean_text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    for word in freq:
        print(f"{word}: {freq[word]}")


def q6():
    strr = input("enter the sentence : ")
    lst = strr.split()
    longest_word = ""
    for i in lst:
        longest_word = i if len(i) > len(longest_word) else longest_word
    print(longest_word)

def q7():
    strr1 = input("enter the first string: ")
    strr2 = input("enter the second string: ")
    strr1 = sorted(strr1)
    strr2 = sorted(strr2)
    flag = 1
    if(len(strr1)!=len(strr2)):
        print("false")
        return
    for i in range(0,len(strr1)):
        if(strr1[i]!=strr2[i]):
            flag=0
            print("false")
            return
        else:
            continue
    if flag==1:
        print("true")



q1()
q2()
q3()
q4()
q5()
q6()
q7()