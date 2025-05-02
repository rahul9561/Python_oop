# Questions on Advanced Strings

# 1. Check for Palindrome
# Write a function that checks if a given string is a palindrome (same forward and backward).
print('\n\nQuestion-1')
str1 = 'madam'
rev =''
for i in str1:
    rev = i+rev
if rev == str1:
    print(f'\'{str1}\' is a Palindrome')
else:
    print(f'\'{str1}\' is not a Palindrome')
    
# Using Slicing
if str1 == str1[::-1]:
    print(f'\'{str1}\' is a Palindrome')
else:
    print(f'\'{str1}\' is not a Palindrome')


 

# 2. Find All Vowels in String
# Extract and return all vowels from a given string.
print('\n\nQuestion-2')
str2 = 'hello world'
set_of_vowels = set()
vowels = 'aeiouAEIOU'
for i in str2:
    if i in vowels:
        set_of_vowels.add(i)
print(f"Vowels in string \'{str2}\' : ", set_of_vowels)




# 3. Remove All Duplicates from String
# Write a function that removes duplicate characters while maintaining the order.
print('\n\nQuestion-3')
str3 = 'hello world'
print('Before removing duplicates : ', str3)

new_str = ''
for i in str3:
    if i not in new_str:
        new_str += i
print('After removing duplicates : ', new_str)




# 4. String Compression
# Compress a string:
# Example: "aaabbc" → "a3b2c1"
print('\n\nQuestion-4')
str4 = 'aaabbccc'

new_str = ''
unique_str = set(str4)
for i in unique_str:
    new_str += i + str(str4.count(i))
print("Compressed String : ", new_str)




# 5. Count Word Frequencies
# Given a long string, count the frequency of each word (ignoring case and punctuation).
print('\n\nQuestion-5')
str5 = 'The quick brown fox jumps over the lazy dog. The dog barks loudly...'

# Cleaning the sentence by removing punctuations
cleaned = ''
for char in str5:
    if char.isalnum() or char.isspace():
        cleaned += char
    else:
        cleaned += ' '  # Replace punctuation with space

# Split into words
words = cleaned.split()

# Counting frequencies using a dictionary
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
    
print("Frequency of Words : ", freq)




# 6. Longest Word in a Sentence
# Write a function that returns the longest word from a given sentence.
print('\n\nQuestion-6')
str6 = 'This is a sample sentence.'
words = str6.split()
max_len = 0
current_word = None
for word in words:
    w_len = len(word)
    if w_len > max_len:
        max_len = w_len
        current_word = word

print("The longest word is : ", current_word)




# 7. Anagram Checker
# Write a program that checks if two strings are anagrams (same letters, different order).
print('\n\nQuestion-7')
str7 = 'hello'
str8 = 'olleh'

# Using sorted() method to sort both strings alphabetically
if sorted(str7) == sorted(str8):
    print(f'\'{str7}\' and \'{str8}\' are Anagrams')
else:
    print(f'\'{str7}\' and \'{str8}\' are NOT Anagrams')

# Other Way
flag = False
for i in str8:
    if i not in str7:
        flag = True
        break
if flag:
    print(f'\'{str7}\' and \'{str8}\' are NOT Anagrams')
else:
    print(f'\'{str7}\' and \'{str8}\' are Anagrams')
        