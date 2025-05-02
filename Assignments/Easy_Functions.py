# Q-1
def check_odd_even(num):
    if num%2==0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
        
        
# Q-2
def check_vowels(st):
    vowwels = 'aeiouAEIOU'
    for i in st:
        if i in vowwels:
            return True
    return False



# Q-3
def squares_of_keys():
    result = {}
    for i in range(1, 21):
        result[i] = i**2
    return result
    
    
# Q-4
def print_keys():
    result = {}
    for i in range(1, 21):
        result[i] = i**2
    
    print("Keys are : ")
    for i in result.keys():
        print(i, sep = ', ', end = ' ')


# Q-5
def print_tuple():
    tup = (i**2 for i in range(1, 21))
    
    print("Tuple elements are : ")
    for i in tup:
        print(i, sep = ', ', end = ' ')


# Q-6
def count_upper_and_lower_case(st):
    lower = 0
    upper = 0
    
    for i in st:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    
    return [lower, upper]



# ----------------------------------------------------------------------
 
# Driver Code 
print("\n\nQ-1")
check_odd_even(5)


print("\n\nQ-2")
# st=input("Enter a string: ")
st = 'hi'
if check_vowels(st):
    print("The given string contains vowels.")
else:
    print("The given string does not contain any vowel.")

    
print("\n\nQ-3")
res = squares_of_keys()
print(res)



print("\n\nQ-4")
print_keys()


print("\n\nQ-5")
print_tuple()


print("\n\nQ-6")
st = "Hello World"
result  = count_upper_and_lower_case(st)

print(f"The given string is '{st}'")
print(f"Lowercase : {result[0]} and Uppercase : {result[1]}")