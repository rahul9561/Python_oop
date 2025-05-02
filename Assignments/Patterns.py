# Basic conditional flow

''' n=10
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''
def qn_1(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

   

''' n=10
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
'''
def qn_2(n):
    for i in range(n):
        for j in range(n):
            print(i+1, end=' ')
        print()
  
  

''' n=10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
'''
def qn_3(n):
    for i in range(n):
        for j in range(n):
            print(j+1, end=' ')
        print()
        


''' n=10
A A A A A A A A A A
B B B B B B B B B B
C C C C C C C C C C
D D D D D D D D D D
E E E E E E E E E E
F F F F F F F F F F
G G G G G G G G G G
H H H H H H H H H H
I I I I I I I I I I
J J J J J J J J J J
'''
def qn_4(n):
    for i in range(n):
        for j in range(n):
            print(chr(65+i), end=' ')
        print()
        

 
''' n=10
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
'''
def qn_5(n):
    for i in range(n):
        for j in range(n):
            print(chr(65+j), end=' ')
        print()
   


''' n=10
10 10 10 10 10 10 10 10 10 10
9 9 9 9 9 9 9 9 9 9
8 8 8 8 8 8 8 8 8 8
7 7 7 7 7 7 7 7 7 7
6 6 6 6 6 6 6 6 6 6
5 5 5 5 5 5 5 5 5 5
4 4 4 4 4 4 4 4 4 4
3 3 3 3 3 3 3 3 3 3
2 2 2 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1
'''
def qn_6(n):
    for i in range(n, 0, -1):
        for j in range(n):
            print(i, end=' ')
        print()



''' n=10
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
'''
def qn_7(n):
    for i in range(n):
        for j in range(n, 0, -1):
            print(j, end=' ')
        print()



''' n=10
J J J J J J J J J J
I I I I I I I I I I
H H H H H H H H H H
G G G G G G G G G G
F F F F F F F F F F
E E E E E E E E E E
D D D D D D D D D D
C C C C C C C C C C
B B B B B B B B B B
A A A A A A A A A A
'''
def qn_8(n):
    for i in range(n):
        for j in range(n):
            print(chr(65+n-i-1), end=' ')
        print()



''' n=10
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
'''
def qn_9(n):
    for i in range(n):
        for j in range(n):
            print(chr(65+n-j-1), end=' ')
        print()



''' n=10
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *
'''
def qn_10(n):
    for i in range(n):
        for j in range(0, i+1, 1):
            print('*', end=' ')
        print()



''' n=10
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
'''
def qn_11(n):
    for i in range(n):
        for j in range(0, i+1, 1):
            print(i+1, end=' ')
        print()



''' n=10
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 10
'''
def qn_12(n):
    for i in range(n):
        for j in range(0, i+1, 1):
            print(j+1, end=' ')
        print()



''' n=10
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G
H H H H H H H H
I I I I I I I I I
J J J J J J J J J J
'''
def qn_13(n):
    for i in range(n):
        for j in range(0, i+1, 1):
            print(chr(65+i), end=' ')
        print()



''' n=10
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H
A B C D E F G H I
A B C D E F G H I J
'''
def qn_14(n):
    for i in range(n):
        for j in range(0, i+1, 1):
            print(chr(65+j), end=' ')
        print()



''' n=10
* * * * * * * * * *
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''
def qn_15(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end=' ')
        print()

        

''' n=10
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3
4 4 4 4 4 4 4
5 5 5 5 5 5
6 6 6 6 6
7 7 7 7
8 8 8
9 9
10
'''
def qn_16(n):
    for i in range(n):
        for j in range(n-i):
            print(i+1, end=' ')
        print()



''' n=10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
def qn_17(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=' ')
        print()
        

        
''' n=10
A A A A A A A A A A
B B B B B B B B B
C C C C C C C C
D D D D D D D
E E E E E E
F F F F F
G G G G
H H H
I I
J
'''
def qn_18(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65+i), end=' ')
        print()

        
        
''' n=10
A B C D E F G H I J
A B C D E F G H I
A B C D E F G H
A B C D E F G
A B C D E F
A B C D E
A B C D
A B C
A B
A
'''
def qn_19(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65+j), end=' ')
        print()



''' n=10
10 10 10 10 10 10 10 10 10 10
9 9 9 9 9 9 9 9 9
8 8 8 8 8 8 8 8
7 7 7 7 7 7 7
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
def qn_20(n):
    for i in range(n):
        for j in range(n-i):
            print(n-i, end=' ')
        print()



# To Test the Functions
n = int(input("Enter n: "))
print()

print("QN-1")
qn_1(n)
print()

print("QN-2")
qn_2(n)
print()

print("QN-3")
qn_3(n)
print()

print("QN-4")
qn_4(n)
print()

print("QN-5")
qn_5(n)
print()

print("QN-6")
qn_6(n)
print()

print("QN-7")
qn_7(n)
print()

print("QN-8")
qn_8(n)
print()

print("QN-9")
qn_9(n)
print()

print("QN-10")
qn_10(n)
print()

print("QN-11")
qn_11(n)
print()

print("QN-12")
qn_12(n)
print()

print("QN-13")
qn_13(n)
print()

print("QN-14")
qn_14(n)
print()

print("QN-15")
qn_15(n)
print()

print("QN-16")
qn_16(n)
print()

print("QN-17")
qn_17(n)
print()

print("QN-18")
qn_18(n)
print()

print("QN-19")
qn_19(n)
print()

print("QN-20")
qn_20(n)
print()