# n = 10

# for i in range(n+6):
#     print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


#type1
# n = 10
# for i in range(n):
#     print(i)


#type 2
# for k in range(5, 25): # [5, 6, 7, ..., 24]
#     print(i)

# for k in range(20): [0, 1, 2, ..., 19]

#type 3
# for h in range(2, 100, 2): # [2, 4, 6, 8, 10, 12, ..., 98]
#     print(h)
# Type 1: for i in range(n): [0, 1, 2, 3, ..., n-1], increases by 1 every time
# Type 2: for i in range(a,b): the for loop starts at a, ends at b-1, increases by 1 every time. So the total number or rounds is (b - a)
# Type 3: for i in range(a,b,c):

# Exercise: print all the odd numbers between 33 and 200


# for k in range(33, 200, 2):
#     print(k)

#### While Loop
# booleans are variables that can be either True or False, and are often used on if-statements

# a = 10
# b = 20

# while a < b:
#     print("Hello World")
#     # do something
#     b = b - 2

# an Infinite Loop

# n = 10
# for i in range(n):
#     print(i)

# i = 0
# while i < n:
#     print(i)
#     i = i + 1

# i = 0

# for i in range(20):
#     print(i)


# while i < 20:
#     print(i)
#     i = i + 1

# i = 5

# for i in range(5, 20):
#     print(i)

# while i < 20:
#     print(i)
#     i = i + 1


# for i in range(10, 50, 5):
#     print(i)

# i = 10

# while i < 50:
#     print(i)
#     i = i + 5

# Exercise: Use a for loop or a while loop to print the numbers from 20 to 5 backwards

# k = 20

# while k > 5:
#     print(k)
#     k = k-1

# for k in range(20, 5, -1):
#     print(k)

# 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49: Arithmetic Series/Sequence/Progression
# base = 4, initial = 1

# Arithmetic series, that initial = 3, base of 7, print all numbers in this series up to 61

# for k in range(3, 61, 7):
#     print(k)

# complete the following series up to a 100
# 1, 2, 4, 7, 11, 16, 22, 29, 37, ....,
# k = 1
# h = 1 # this is the number that you add to k each time
# while k < 100:
#     print(k)
#     k = h + k
#     h = h + 1

# divide them into rounds
# round 1: k=1,h=1    -> k = k + h = 1 + 1 = 2
# round 2: k=2,h=2    -> k = k + h = 2 + 2 = 4
# round 3: k=4,h=3    -> k = k + h = 4 + 3 = 7
# round 4: k=7,h=4    -> k = k + h = 7 + 4 = 11


# New similar exercise:
# complete the following series up to 200
# 1, 2, 4, 8, 16, 32, 64, .....
"""
x= 0
while 2**x < 200:
    print(2**x)
    x+=1
# let's say we have two variables, a,b:
# we can write a to the power b in python as a**b
"""

# New similar exercise:

# 5, 6, 4, 7, 3, 8, 2, 9, 1, 10, ...
# i = 1
# y = 5
# while i < 20:
#     print(y)
#     y += i
#     i+=1
#     print(y)
#     y -= i
#     i+=1

# another way:

# i = 1
# y = 5
# while i < 20:
#     print(y)
#     if i % 2 == 0:
#         y -= i
#     else:
#         y += i
#     i += 1


# count how many numbers between 1 and 100 that are divisible by 3.
# divisible = 0

# z = 1
# while z < 100:
#     if z % 3 == 0:
#         divisible += 1
#     z += 1
# print("From 1-100 there are", divisible, "numbers that can be divided by 3.")



"""
a = 64
b = 90
v = 15

if a + v > b:
    print("Person A has a greater loss of points than 15 compared to person B")
if a + v < b:
    print("Person A has a lesser loss of points than 15 compared to person B")    
if a + v == b:
    print("Person A has a loss of 15 points compared to person B")
"""
# you have two cups of water of different sizes
# cup A can hold 2 liters of water
# cup B can hold 5 liters of water
# let's we want to bring a cup C, such that the amount of water in both cups A and C is equal to that of B.
# what is the size of the cup C?
# C = B - A
# if we take B - A + 1, this is equal to the numbers of numbers between A and B

# ask the user for two numbers a and b, and then print the sum of all numbers between a and b (inclusive)



# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# x = 0

# a = 2, b = 5
# start with x = 2
# if x != 5 -> if 2 != 5 -> x += 1 -> x = 2 + 1 = 3
# if x != 5 -> if 3 != 5 -> x += 1 -> x = 3 + 1 = 4


# how many numbers are between a and b ?


# while a <= b:
#     x += a
#     a += 1
#     print("Current a:", a, "Current x:", x)
    
# print(x)


# New Problem: 
# ask the user for two numbers a and b, and the print the product of all the odd numbers between a and b (inclusive)
# example, if a = 2, b = 5
# the odd numbers between 2 and 5 are [3,5], their product is 15

# a = int(input("Put the first number in: "))
# b = int(input("Put the second number in: "))

# x = 1

# x = 3 * 5
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ....
#             b  

# while a <= b:
#     if a % 2 == 1:
#         x = a * x 
#     a += 1

    
# print(x)
    

# New Problem: 
# ask the user for 2 numbers, a and b, and then print the sum of every other number between a and b, starting from
# example:
# a = 2, b= 5
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ...
#    a        b
# x = 2 + 4 = 6
# a = 5, b = 12
# x = 5 + 7 + 9 + 11 = 32


# x = 0

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while a <= b:
#     x += a # line q
#     a += 2 # line p
            
# print(x)

# at first,      x=0, a=2, b=5 up to line 265
# round 1: at p: x=0, a=4, b=5
# round 1: at q: x=4, a=4, b=5
# round 2: at p: x=4, a=6, b=5
# round 2: at q: x=10, a=6, b=5

# New Problem:
# ask the user for a single number n, and then print the factorial of n.
# what is the factorial of n?
# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120

# n = int(input("Enter a number: "))

# j = n

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...
# F, F  T  T  T  T  T  T  T  T   T 
# F  F  t  t  t  t  t  t  t  t   t

# j >= 2 is equivalent to j > 1

# while j > 1:
#     j -= 1
#     n *= j

# print(n)

# New Problem:
# Fibonacci Numbers
# It is a sequence of numbers, where each number is the sum of the two previous numbers.
# The first two 1, 2,numbers in the sequence are always 0 and 1.
# Fib: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# idx: 0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11, 12, .....
#  
# Problem statement: The user will give you a single number n, and you have to print the nth fibonacci number.
# if n = 5, the output is 5
# if n = 10, the output is 55
# if n = 7, the output is 13.
# t=0
# prev = 1
# before_prev = 0
# k = 1
# # 0, 1

# n = int(input("Enter a number:"))

# for i in range(n-1):
#     k = before_prev+prev
#     before_prev = prev
#     prev = k

# 0   , 1  , 1  , 2  , 3  , 5  , 8
#                bpr , pr , k=pr+bpr

# for i in range(n-1):
#     k +

# a = 2
# b = 5 # b = 2
# c = 8 # c = 5

# before we do anything we have
# a=2,b=5,c=8

# c = b
# b = a

# a = c, # a=8,b=5,c=8
# b = a, # a=8,b=8,c=8
# c = b, # a=8,b=8,c=8

# move whatever is in a to b, and move whatever is in b to c

# # swap and b
# # b = 2, a = 5
# t = a # put a on the table
# a = b # copy b and paste it in a
# b = t # b picks up old a from the table§
# print(k)


# New Problem:
# ask the user for two numbers a and b, and then print the three numbers in the middle between a and b
# example:
# a = 1, b=7
# 1, 2, 3, 4, 5, 6, 7
# a = 2, b = 9
# 2, 3, 4, 5, 6, 7, 8, 9


a = int(input("First number:"))
b = int(input("Second number:"))


c = 0
midnum = 0


distance_between_a_b = b - a

half_distance_between_a_b = distance_between_a_b//2

middle_number = a + half_distance_between_a_b
middle_number = b - half_distance_between_a_b

midnum = c + midnum_clas # b-a + (b-a)//2 = 3*(b-a)//2 # 1 + 1/2

midnum1 = midnum + 1
midnumminus1 = midnum - 1

print(midnumminus1, midnum, midnum1)



# -------- ---------------------------  ---------------------------
# 1 2 3 4  5 6 7 8 9 10 11 12 13 14 15  16 17 18 19 20 21 22 23 24