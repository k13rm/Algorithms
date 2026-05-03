# Problem 1: Given a list of numbers, find the maximum and minimum values in the list.
# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# maximum_value = -999999
# minimum_value= 999999
# for k in range(0, len(lst)):
#     if lst[k] > maximum_value:
#         maximum_value = lst[k]
#     if lst[k] < minimum_value:
#         minimum_value = lst[k]

# print("the maximum value is:", maximum_value)
# print("the minimum value is:", minimum_value)

# maximum_value = max(lst)
# minimum_value = min(lst)


# Problem 2: Given a list of numbers, find the sum of the odd numbers in the list.
# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sumofodd = 0
# for k in range(0, len(lst)):
#     if lst[k] % 2 == 1:
#         sumofodd = sumofodd + lst[k]

# print("the sum of all the odd numbers are:", sumofodd)

# sum_of_all = sum(lst)
# sum_of_even = sum_of_all - sumofodd
# print("the sum of all the even numbers are:", sum_of_even)

# Problem 3 (slightly harder): Given a list of numbers, find the largest odd number and the smallest even number in the list and print both of them.

"""
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest_odd_number = -99999
smallest_even_number = 99999
for k in range(len(lst)):
    if lst[k] > largest_odd_number and lst[k] % 2 == 1:
        largest_odd_number = lst[k]
    if lst[k] < smallest_even_number and lst[k] % 2 == 0:
        smallest_even_number = lst[k]

print("The smallest even number in the provided list is:\n", smallest_even_number,"\nThe largest odd number in the provided list is:\n", largest_odd_number)
"""

# Problem 4: Given a list of numbers, find the number of times each number is duplicated in the list. For example, if the list is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], then the output should be:
# 3 is duplicated 2 times
# 1 is duplicated 2 times
# 4 is duplicated 1 times
# 5 is duplicated 3 times
# 9 is duplicated 1 times
# 2 is duplicated 1 times
# 6 is duplicated 1 times

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] # [1, 10000000]
x = max(lst) + 1
counter = [0] * x

# [0, 2, 0, 1, 1, 0, 0, 0, 0, 0]
#  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# dummy_lst = []
# dummy_lst[5] = dummy_lst[5] + 1

for k in lst:
    counter[k] = counter[k] + 1

for i in range(x):
    if counter[i] > 0:
        print(i, "is duplicated", counter[i], "times")
    