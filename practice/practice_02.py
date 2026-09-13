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

# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] # [1, 10000000]
# x = max(lst) + 1
# counter = [0] * x counter[3] = counter[3] + 1

# [0, 2, 0, 1, 1, 0, 0, 0, 0, 0]
#  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# dummy_lst = []
# dummy_lst[5] = dummy_lst[5] + 1

# for k in lst:
#     counter[k] = counter[k] + 1

# for i in range(x):
#     if counter[i] > 0:
#         print(i, "is duplicated", counter[i], "times")


# Problem 5: Given a list of numbers, find the second largest and second smallest numbers in the list and print both of them.

# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# l1:  3  3  4  4  5, 9, 9, 9, 9, 9, 9
# l2:  0  1  3  3  4, 5, 5, 6, 6, 6, 6

# if the new number is larger than l1, then l2 becomes l1 and l1 becomes the new number
# if the new number is smaller than l1 but larger than l2, then l2 becomes the new number
# otherwise, we do nothing

# l1 = 0
# l2 = 0
# s1 = 9999999
# s2 = 9999999

# largest = 0
# second_largest = 0

# for k in range(len(lst)): k: [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for k in lst: k: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# for k in lst:
#     if k > l1:
#         l2 = l1
#         l1 = k
#     elif k < l1 and k > l2:
#         l2 = k
#     if k < s1:
#         s2 = s1
#         s1 = k
#     elif k > s1 and k < s2:
#         s2 = k
# print("The largest number in the list is:\n", l1, "\nThe second largest number in the list is:\n", l2)    

# print("The smallest number in this list is:\n", s1, "\nThe second smallest number in this list is:\n", s2)        

# print("\n\nThe second largest number is:\n", l2, "\nThe second smallest number is:\n", s2)


# Problem 6 (slightly harder): Given a list of numbers, find the unique numbers in the list and print their count. For example if the list is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], then the output should be:
# There are 7 unique numbers in the list, which are 1, 2, 3, 4, 5, 6, 9

# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# duplicates = 0
# x = max(lst) + 1
# counter = [0] * x
# for k in lst:
#     counter[k] = counter[k] + 1

# unique_numbers = []
# for i in range(x):
#      if counter[i] > 0:
#           unique_numbers.append(i)
        
# print("There are", len(unique_numbers), "unique numbers in the list, which would be", unique_numbers)


# Problem 7: (even harder) Given a list of numbers, and a target number k, find if it is possible to choose two numbers from the list, such that their sum is equal to k. For example, if the list is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] and k = 8, then the output should be True, because we can choose 3 and 5 from the list, and their sum is 8. If k = 20, then the output should be False, because there are no two numbers in the list that can sum up to 20.

# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# # #         i  j                                                                               
# k = 14 
# pair = 0 # flag variable technique

# # nested for loops technique
# for i in range(len(lst)): # [0 -> len(lst) - 1]
#     for j in range(i + 1, len(lst)): # [i + 1 -> len(lst) - 1]
#         if lst[i] + lst[j] == k:
#             pair = 1
#             break
            
# if pair == 1:
#     print("True")
# else:
#     print("False")

# given a list, print all pairs of numbers in the list, where each pair is printed on a separate line.

# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         print(lst[i], lst[j])

# Problem 8: (that uses the similar concepts to problem 7) Given a list of numbers, and a target number k, 
# find if it is possible to choose three numbers from the list, such that their sum 
# is equal to k. For example, if the list is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] and k = 12, then the output 
# should be True, because we can choose 3, 4, and 5 from the list, and their sum is 12. If 
# k = 30, then the output should be False, because there are no three numbers in the list that can sum up up to 30.

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
n = 30
sumofthree = 0
for k in range(len(lst)):
    for l in range(k+1, len(lst)):
        for m in range(l+1, len(lst)):
            if lst[k] + lst[l] + lst[m] == n:
                sumofthree = 1
                
if sumofthree == 1:
    print("True")
else:
    print("False")
