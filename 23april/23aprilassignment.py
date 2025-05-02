name = input("enter the string: ")
print(name[::-1])
#....................................
#q2
vcount = 0
ccount = 0
vowels = ['a','e','i','o','u']
for i in name:
    for j in i:
        if j in vowels:
            vcount+=1
        else:
            ccount+=1
print("q2 - ",end=" ")
print("vowels are : ",vcount)
print("consonents are : ",ccount)
#...........................................
#q3)
newlist = []
for i in name:
    for j in i:
        if j not in newlist:
            newlist+=j
        elif j==' ':
            newlist+=j
        else:
            continue
newstring = ""
for j in newlist:
    newstring+=j
print("q3 - after removing duplicates : ",newstring)
#...............................................
#q4

# word = input("enter the word: ")
wordCount = 0
for i in name:
    if i==' ':
        continue
    else:    
        wordCount+=1
print("q4 - total word count : ",wordCount)
#.................................................
#q5)
char_counts = {}
for char in name:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
print("q5 - occurences :  ",char_counts)
#..............................................
#q6)
newstr = ""
for j in name:
    if j==" ":
        newstr+=j
        continue
    if 'a' <= j <= 'z':
        newchar = ord(j) - 32
        newstr += chr(newchar)
    elif 'A' <= j <= 'Z':
        newchar = ord(j) + 32
        newstr += chr(newchar)
        


print("q6 - after case conversion: ", newstr)
#.............................................
#q7)
search = input("q7 - search for the word : ")
if(name.find(search)==-1):
    print("word not found")
else:
    print("word found")

#..........................................
#q8)
newstr1=""
newstr2=""
finalstr=""
for j in name:
    if j==" ":
        newstr1+=j
        continue
    if ord(j)>=97:
        newstr1+=j
    else:
        newstr2+=j
for i in newstr1:
    finalstr+=i
for i in newstr2:
    finalstr+=i
print("q8 - final string after upper and lowercase sorting : ",finalstr)

#.............................................
#q9)
lower_count = 0
upper_count = 0
numeric_count = 0
special_count = 0

for i in name:
    if 'a' <= i <= 'z':
        lower_count += 1
    elif 'A' <= i <= 'Z':
        upper_count += 1
    elif '0' <= i <= '9':
        numeric_count += 1
    else:
        special_count += 1

print(f"q9 - lower char - {lower_count}, upper char - {upper_count}, numeric count: {numeric_count}, special count - {special_count}")

#........................................
#q10) - 
newlist2 = ['12','','33',"skaldhf"]
for i in newlist2:
    if len(i)==0:
        newlist2.remove(i)
print("q10 - after deletion all the blank items from the list ",newlist2)
#............................................
#q11)-
before = "Hello, have a good day"
afterDeletion = ""
for i in name:
    if i in vowels:
        afterDeletion+=i
    else:
        continue
print("q11- after deletion of all the consonants: ",afterDeletion)