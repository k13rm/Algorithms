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
divisible = 0

z = 1
while z < 100:
    if z % 3 == 0:
        divisible += 1
    z += 1
print("From 1-100 there are", divisible, "numbers that can be divided by 3.")


# ask the user for two numbers a and b, and then print the sum of all numbers between a and b (inclusive)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
x = 0
while a <= b:
    if x  != a + 1:
        x + (a +1)
    
print(a+b)