lst = [11, 4, 7, 14, 28, 28, 9, 4, 4, 7]

"""
Homework:
1. count how many duplicates there are in the list
2. find all duplicates and how many times each number is duplicated
"""

c = {}
for x in lst:
    if x in c:
        c[x] = c[x]+1
    else:
        c[x] = 1

for key, value in c.items():
    print(key, "is duplicated", value, "times.")




# count = 0

# #1:
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             print("yes")
# #2:
# duplicates = 0
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             duplicates += 1
# print(duplicates)


# (key, value) pairs
# 
# d = {}

# mydictionary = {
#     "Mert": "The elegant Universe",
# }

# mydictionary["Ekin"] = "The essence of Calculus"
# mydictionary["Volkan"] = ["The art programming", "Leaders of Tomorrow"]
# mydictionary["Ekin"] = "The story of the three little pigs"

# # del mydictionary["Ekin"]

# print("Mert's favorite book is", mydictionary["Mert"])

# if "Selim" in mydictionary:
#     print("Selim's favorite book is", mydictionary["Selim"])
# else:
#     print("Selim is not in the dictionary")
"""

counter = {}

l = [3, 6, 1, 7, 2, 1]

for x in l:
    if x in counter:
        counter[x] = counter[x] + 1
    else:
        counter[x] = 1

print(counter)

# 1: go over the keys
for key in counter.keys():
    print(key, "is duplicated", counter[key], "times")

# 2: go over the values
for value in counter.values():
    print(value)

# 3: go over the key-value pairs
for key, value in counter.items():
    print(key, "is duplicated", value, "times")
"""
#if storage[1] == storage[len]

# lst2 = lst[2:6] # [7, 17, 28, 18]

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

# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             print("yes")


# # solution using slicing
# for i in range(len(lst)):
#     if lst[i] in lst[i+1:]:
#         print("yes")


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
# """
# greatest = 0
# for x in lst:
#     if greatest < x:
#         greatest = x
# least = greatest
# for x in lst:
#     if least > x:
#         least = x
# print(least)
# """

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