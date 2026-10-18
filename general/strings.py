# Strings are simply lists of characters.

word = "Good Morning"

# Characters within a string can be accessed using indexing. Indexing starts at 0.

# print(word[0]) # Output: G
# print(word[1]) # Output: o
# print(word[2]) # Output: o
# print(word[3]) # Output: d

# Strings can also be sliced to extract a part of the string.

# print(word[0:4]) # Output: Good [0,1,2,3]
# print(word[5:12]) # Output: Morning [5,6,7,8,9,10,11]

# We can also check if a certain character or substring exists within a string using the 'in' keyword in python.

# if "Good" in word:
#     print("The word 'Good' is present in the string.")
# else:
#     print("The word 'Good' is not present in the string.")


# We can use a for loop to iterate through each character in the string.
# There are two ways to do so: using a for loop with the string directly, or using the loop with the range function and indexing.

# Type 1: Using a for loop with the string directly

# for ch in word:
#     print(ch)

# Type 2: Using a for loop with the range function and indexing
"""
for i in range(len(word)): # [0 -> len(word) - 1]
    print(word[i])
"""

# Exercise 1:
# Given a string, write a code that counts how many vowels are in the string.

# word = "Good Morning"

# vowels = "a", "e", "i", "o", "u"
# count = 0

# for ch in word:
#     if ch in vowels:
#         count += 1
#         print(ch)

# print("there are", count, "vowels")

# Exercise 2: 
# Given a string, find the first non-repeating character in the string.
# Examples:
# "aaaabbbbc" -> c
# "swiss" -> w
# "aabbcc" -> None
# "racecars" -> e
# {'r': 2, 'a': 2, 'c': 2, 'e': 1, 's': 1}

word = "aabbcc"
lettercount = {}

for ch in word:
    if ch not in lettercount:
        lettercount[ch] = 1
    else:
        lettercount[ch] += 1

for ch in word:
    if lettercount[ch] == 1:
        print(ch)
        break
    