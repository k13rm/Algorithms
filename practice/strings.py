# Problem 1: Given two strings, A and B, check if string B can be 
# built from string A by removing or rearranging characters. For example, if A = 
# "balloon", and B = "ball", the answer is yes. if A = "python", and B = "pony", 
# the answer is true. If A = "python", and B = "java", the answer is false.

"""
# Kerem's solution:
A = "python"
B = "nohtyp"
char_count_A = {}
char_count_B = {}
for char in A:
    if char not in char_count_A:
        char_count_A[char] = 1
    else:
        char_count_A[char] += 1

for char in B:
    if char not in char_count_B:
        char_count_B[char] = 1
    else:
        char_count_B[char] += 1

if len(char_count_A) < len(char_count_B):
    print("No")
    exit()

flag = True
for char in char_count_B:
    if char not in char_count_A or char_count_B[char] > char_count_A[char]:
        print("No")
        flag = False
        break

if flag == True:
    print("Yes")


# Nazir's solution:



"""
# A = XYYXYY
# B = XYXYXY
# build dictionary for A
# X: 0
# Y: 2
# Let's go over the characters of B:
# XYXYXY
# ++++-
# first we have X,    
    # if char not in char_count:
    #     char_count[char] = 1
    # else:
    #     char_count[char] += 1


# Palindrome: a word or string that reads the same forwards and backwards. 
#For example, "racecar" is a palindrome. Another word example is "level". Another word example is "deified".

# Problem 2: Given a string, check if it is a palindrome or not. For example, if the string input is "racecar", the output should be yes. If the string input is "hello", the output should be no.

s = "abababab"

# abcba
# 01234
# s at index k is equal to s at index -k
# k = 0 -> -1 =
# k = 1 -> -2 = -k-1
# k = 2 -> -3 =
# k = 3 -> -4 =

flag = False

for k in range(len(s)):
    if s[k] != s[-k-1]:
        flag = True

if flag == False:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")


#  Problem 3: Given a string as input, check if its characters can be rearranged to form a palindrome. 
#For example, if the input string is "carrace", the output should be yes. If the input string is "aabb", the answer should 
#be yes. If the input string is "abc", the answer should be no.



# carraceaae
# arcaeeacra
flag = False
chars_dict = {}
string = input("enter word to be rearranged")



for k in rearranged_string:
    if s[k] != s[-k-1]:
        flag = True
