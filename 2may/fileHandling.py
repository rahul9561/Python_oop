# file handling - open function then it takes mmode as params
# mode - r,w,a,r+,w+.....error file not found if not found
# w - overrides the already present data,creates new file if not found
# r - reads the data 
# a - appends the existing data, creates new file if not already present
# Writing with r+ overwrites starting from the beginning, without deleting the full file.
    # If you write fewer characters than were there originally, the rest will stay.
    # If you want to append to a file instead, use a or a+.
# w+ mode - 
# rb,wb,etc - for binary data - video image etc...
f = open("./text.txt",'w')
f.write("hello world")
f.close()
f = open('./text.txt','w')
# print(f.read())
print(f.name) #prints the name of the file
with open('./text.txt') as w:
    print(w.read())


#  we have read methods such as read , readline,readlines