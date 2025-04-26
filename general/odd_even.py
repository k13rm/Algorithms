# x = 2

# x = 3 + 2
# y = 3 - 2
# z = 3 * 2
# w = 3 / 2
# # modulo operator / remainder operator
# x = int(input("Enter a number, I'll say if it's odd or even:"))

# if x % 2 == 0:
#     print("the number is even")
# if x % 2 != 0:
#     print("the number is odd")
# lst = [3, 5, 1, 4, 8, 2, 9, 11, 23, 22]
# even_count = 0
# odd_count = 0
# for x in lst:
#     if x % 2 == 1:
#         odd_count += 1
#     else:
#         even_count += 1
# print("There are", odd_count, "odd numbers,")
# print("and lastly there are", even_count, "even numbers.")    


# 
        

"""
Homework:

Given the list above, find the LARGEST ODD number in the list and lowest even number in the list.
the print the difference between
"""
"""
# lst = []

smallest_even = 999999
greatest_odd = 0
for x in lst:

    if x % 2 == 1 and greatest_odd < x:
        greatest_odd = x
    if x % 2 == 0 and smallest_even > x:
        smallest_even = x

"""
# print("The largest odd number is:", greatest_odd)
# print("The smallest even number is:", smallest_even)
# print("The difference in-between both are:", greatest_odd - smallest_even)


""""
Given the same list, print the sum of the even numbers, and the sum of the odd numbers.
"""

# odd_num = 0
# even_num = 0

# for x in lst:
#     if x % 2 == 1:
#         odd_num += x
#     if x % 2 == 0:
#         even_num += x

# print("The sum of all the odd numbers are:", odd_num)
# print("The sum of all the even numbers are:", even_num)

"""
In addition to the list above, I will give you a variable target. I want you to find
the closest odd number in the list to target, and the closest even number in the list to target.
"""

lst = [3, 5, 1, 4, 8, 2, 9, 11, 23, 22]


# x = target

# closest_y = 0
# smallest_distance = 99999999

# for y in lst:
#     distance = abs(y - x) 
#     if distance < smallest_distance:
#         smallest_distance = distance 
#         closest_y = y

# print("The closest number to the target in the list is:", closest_y)
# target = 14
# closest_odd = 0
# closest_even = 0
# smallest_distance_odd = 999999999
# smallest_distance_even = 999999999


# for i in lst:
#     distance = abs(i - target)
#     if i % 2 == 1 and distance < smallest_distance_odd: 
#         smallest_distance_odd = distance
#         closest_odd = i
#     if i % 2 == 0 and distance < smallest_distance_even:
#         smallest_distance_even = distance
#         closest_even = i

# print("The closest odd number to the target which is:", target, "is", closest_odd)
# print("The closest even number to the target is", closest_even)
        

"""
Given the list below, find the two numbers that have the greatest distance between them. Print the distance
and print the numbers that have the greatest distance between them.
"""


# lst = [3, 5, 1, 4, 8, 2, 9, 11, 23, 22]
# largest_number = 0
# smallest_number = 999999

# for k in lst:
#     if k > largest_number:
#         largest_number = k
#     if k < smallest_number:
#         smallest_number = k

# greatest_distance = largest_number - smallest_number

# print("The largest number in the list is:", largest_number, "and the smallest number is:", smallest_number,"\nthey have the greatest distance between them which is:", greatest_distance)


"""
Given a list, and a target variable, you need to find the upper bound and the lower bound of the given target variable in the list.
The upper bound is the smallest number greater than the target
The lower bound is the largest number smaller than the target.

NOTE: if the the number doesn't have an upper bound or lower bound, just say the number doesn't have any.
"""

lst = [3, 5, 1, 4, 8, 2, 9, 11, 23, 22] # sort the numbers: [1, 2, 3, 4, 5, 8, 9, 11, 22, 23]

# lst1 = [1,2,3,4,5]
# lst2 = [8,9,11,22,23]

target = 7
ub_target = 
lb_target = 

# |-23| = +23
# |23| = +23

# y1 = 5, x = 4
# y2 = 1, x = 4
# y1 - x = 5 - 4 = |1| = 1
# y2 - x = 1 - 4 = |-3| = 3

