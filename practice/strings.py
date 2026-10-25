# Problem 1: Given two strings, A and B, check if string B can be 
# built from string A by removing or rearranging characters. For example, if A = 
# "balloon", and B = "ball", the answer is yes. if A = "python", and B = "pony", 
# the answer is true. If A = "python", and B = "java", the answer is false.

A = "ballon"
B = "ball"
char_count = {}

for char in A:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

for char in B:
    if char not in char_count:
        print("False")
    
    # if char not in char_count:
    #     char_count[char] = 1
    # else:
    #     char_count[char] += 1

