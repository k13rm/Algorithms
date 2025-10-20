
# Standard for loop example

# num = 10
# for i in range(num): #[0, num-1]
#     print("Hi !")


# A for loop that does not start from 0
# instead of from 0 to num-1, I want it to go from 5 to num-1


# for i in range(0, num):
#     print(i)

# this is exactly equivalent to the example above
"""
num = 10
for i in range(5, num):
    print(i)
"""
# write a code that prints all the even numbers less than num


# betternum = 0
num = 20
# for k in range(num):
  
#   if k % 2 == 0:

#     num = k
#     print(k)

# another way to write the same code.

# for i in range(0, num, 5): #
#     print(i) 

# task: write a code that prints all the multiples of 4 between 8 and 80

# for k in range(8, 80, 4):
#  print(k)


# can you print a ladder of asteriks that looks like this:
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# ********** 10 lines

# floors = 10

# for k in range(floors):
#     for j in range(0, k):
#       print("*", end="")
#     print("")

# print a christmas tree way:
# 10 levels:
#          * # k=0 : 10 space, 1 asteriks 
#         *** # k=1: 9 space, 3 asteriks
#        ***** # k=2: 8 space, 5 asteriks
#       ******* # k=3: 7 space, 7 asteriks
#      ********* # k=4: 6 space, 9 asteriks
#     *********** # k=5: 5 space, 11 asteriks
#    *************
#   ***************
#  *****************
# *******************
# number of spaces = levels - k
#  = 10 - 6 = 4
# 5 levels:
#     *, k=0, 5 space, 1 asteriks
#    *** , k=1, 4 space, 3 asteriks
#   ***** , k=2, 3 space, 5 asteriks
#  *******
# *********


# k = 0, * = 1
# k = 1, * = 3
# k = 2, * = 5
# k = 3, * = 7
# k = 4, * = 9
# k = 5, * = 11
# k = 6, * = 13
# k = 7, * = 15


# number of asteriks = 

# levels = 100

# for k in range(levels):

#   number_of_spaces = levels - k
#   for s in range(number_of_spaces):
#     print(" ", end="")

#   number_of_asteriks = k * 2 + 1

#   for j in range(number_of_asteriks):
#     print("*", end= "")
  
#   print("")




## New Problem:
# Write a code that prints the following pattern which looks like a symmetric diamond:

#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# ******************* levels: 10
#  *****************  # k=0, : 17 asterisks     | 2 spaces
#   ***************   # k=1, : 15 asterisks     | 3 spaces
#    *************    # k=2, : 13 asterisks     | 4 spaces
#     ***********     # k=3, : 11 asterisks     | 5 spaces
#      *********      # k=4, : 9 asterisks      | 6 spaces
#       *******       # k=5, : 7 asterisks      | 7 spaces
#        *****        # k=6, : 5 asterisks      | 8 spaces
#         ***         # k=7, : 3 asterisks      | 9 spaces
#          *          # k=8, : 1 asterisks     | 10 spaces

# we said before that the number of asteriks is equal to 2 * k + 1
# first, when k is 0 : asteriks = 2 * levels - 3 - (2 * k)
# second, when k is 1: asteriks = 2 * levels - 3 - (2 * k)
# third, when k is 2 : asteriks = 2 * levels - 3 - (2 * k)

# k + 3 = x
# same as asteriks = k + 3
# x = 10 - k


# levels = 20
# for k in range(levels):
#   number_of_spaces = levels - k
#   for s in range(number_of_spaces):
#     print(" ", end="")

#   number_of_asterisks = k * 2 + 1

#   for j in range(number_of_asterisks):
#     print("*", end= "")

#   print("")

# # the second triangle starts below:

# for k in range(levels):
#   number_of_spaces2 = k + 2
#   for s in range(number_of_spaces2):
#     print(" ", end="")

#   number_of_asterisks2 = 2 * levels - 3 - (2 * k)
#   for j in range(number_of_asterisks2):
#     print("*", end= "")

#   print("")


# New problem: give two numbers, height an width, draw a parallelogram of asteriks of the given height and width
# height = 5
# width = 10

# **********
#  *        *
#   *        *
#    **********

# h = 10
# w = 20
#  ********************
#   *                  * # i=0, 1 space, (i + 1)
#    *                  * # i=1, 2 spaces
#     *                  * # i=2, 3 spaces
#      *                  *
#       *                  *
#        *                  *
#         *                  *
#          *                  *
#           ********************
number_of_spaces = 0
h = 100
w = 200
spaces_in_between = 0

for k in range(w):
    print("*", end="")
print("")


# for i in range(n): [0, 1, 2, 3, ..., n-1], increases by 1 every time
# for i in range(a,b):
# for i in range(a,b,c):

for i in range(h - 2): # [0, h - 3]
    print(i) 
    # print the spaces first
    number_of_spaces = i + 1
    for s in range(number_of_spaces):
        print(" ", end="")
    print("*", end="")
    spaces_in_between = w - 2
    for n in range(spaces_in_between):
        print(" ", end="")

    print("*")

for f in range(h - 1):
    print(" ", end="")
for l in range(w):
    print("*", end="")
print("")   



########################
print("A", end="")
print("B")