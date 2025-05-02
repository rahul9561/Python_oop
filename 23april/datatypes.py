# immutable and mutable datatypes
l =[1,2,3,4]
print(l)
print(id(l))
l[1]='hello'
print(l)

print(id(l))

# string datatype

s = "python,is good"
print(s[-1::-1])
print(len(dir(str)))

another = "aassaaee"
print(another.count('a'))
# center is used to add padding - min should be atleast greater thean len of string
print(another.find('a',1))
# in above case the second parameter is what index onwards we are to search
print(another.rfind('b'))
# difference bewteen find and index is that if a char is not found then index would raise an exception whereas find would give -1 as a result and we have rfind which woud search from the back
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('p','ch'))
# replace takes another parameter that would require us to tell how many occurences it should change
# explandtabs()
an = "*****a     w\te\te"
print(an.expandtabs(12))
# swap case - upper case to lower case and vice versa
# join is used to join multiple string using some delimeter
print(s.join('*'))
# strip function rmeove some chars both the sides by default it considers blank space- doesnt delete from between the string
print(an.strip('*'))
print(an.split('*'))
# print(len(splitlines(' ')))
print(len(an.splitlines(' ')))
message = "python *is *a good language"
print(message.split('*'))
print(message.splitlines('*')) #it breaks taking reference of the presence of \n new line chars
# split and splitline returns list;
name = 'utkarsh'
print(f"my name is {name} ")