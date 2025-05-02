# Pattern Problems


'''
1. Square Star Pattern
Print the following pattern for a given n:

****  
****  
****  
****
'''
def square_star(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()


'''
2. Pyramid Star Pattern
Print the following pattern for a given n:

   *  
  **  
 ***
****
'''
def pyramid_right(n):
    # Printing the Spaces
    for i in range(n):
        for j in range(0, n-i-1, 1):
            print(' ', end=' ')
        # Printing the Stars
        for j in range(0, i+1, 1):
            print('*', end=' ')
        print()


'''
3. Print the following pattern for a given `n`:  
n=5

*  
* *  
*  
* *  
*  
'''
def alternate_star(n):
    for i in 


# To test the pattern functions
# if __name__ == "__main__":
n=int(input("Enter n : "))
print("Square Star Pattern")

square_star(n)
print()

pyramid_right(n)
print()