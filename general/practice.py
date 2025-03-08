lst = [1, 4, 7, 17, 28, 18, 9, 1, 2]

#      0  1  2   3   4  5   6  7  8
# i from 0 to len(lst) - 1
# # range(x): 0 -> x - 1
# sum = 0
# # range(10): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(lst)):
#     sum = sum + lst[i]
# print(sum)

# # first parameter: a newly created variable
# # second parameter: a list or "anything similar" (e.g. tuple, string, iterable)
# (3,4,5)
# for x in lst:
#     sum = sum + x
# print(sum)

# print(sum(lst))
"""
greatest = 0
for x in lst:
    if greatest < x:
        greatest = x
least = greatest
for x in lst:
    if least > x:
        least = x
print(least)
"""

# least = 100
# for x in lst:
#     if least > x:
#         least = x
# print(least)
    
greatest = 0
greatest_idx = 0
greatest2 = 0

for i in range(len(lst)): # for x in lst
    if greatest < lst[i]: # if greatest < x
        greatest = lst[i]
        greatest_idx = i
    elif  greatest2 < greatest and greatest2 > lst[i]:
        greatest2 = i
print("Second greatest number is:", greatest2)

#print("Found the greatest number", greatest, "at index", greatest_idx + 1)