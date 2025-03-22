lst = [11, 4, 7, 14, 28, 28, 9, 4, 4, 7]

"""
Homework:
1. count how many duplicates there are in the list
2. find all duplicates and how many times each number is duplicated
"""



lst2 = lst[2:6] # [7, 17, 28, 18]

# x = 4
# if x in lst:
#    lst2 = lst.copy()
#    lst2.remove(x)
# print(lst2)
# print(lst)

# flag = False
# for i in range(len(lst)):
#     lst2 = lst.copy()
#     lst2.remove(lst[i])
    
#     if lst[i] in lst2:
#         print("yes")
#         flag = True

# for j in range(len(lst2)):
#     if lst[i] == lst2[j]:
#         return True

# if flag == False:
#     print("no")

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            print("yes")


# solution using slicing
for i in range(len(lst)):
    if lst[i] in lst[i+1:]:
        print("yes")


# range(x, y): x -> y - 1
# range(5, 10): [5, 6, 7, 8, 9]

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
    
# greatest = 0
# greatest_idx = 0
# greatest2 = 0

# for i in range(len(lst)): # for x in lst
#     if greatest < lst[i]: # if greatest < x
#         greatest2 = greatest
#         greatest = lst[i]
#         greatest_idx = i
#     elif greatest2 < lst[i]:
#         greatest2 = lst[i]

#       1 2 3 4 7 6
# g1:   1 2 3 4 7 7
# g2:   0 1 2 3 4 6

# print("Second greatest number is:", greatest2)

#print("Found the greatest number", greatest, "at index", greatest_idx + 1)