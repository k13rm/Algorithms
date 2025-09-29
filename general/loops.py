
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
#  *****************  # k=0, 2 spaces: 17 asterisks
#   ***************   # k=1, 3 spaces: 15 asterisks
#    *************    # k=2, 4 spaces: 13 asterisks
#     ***********     # k=3, 5 spaces: 11 asterisks
#      *********      # k=4, 6 spaces: 9 asterisks
#       *******       # k=5, 7 spaces: 7 asterisks
#        *****        # k=6, 8 spaces: 5 asterisks
#         ***         # k=7, 9 spaces: 3 asterisks
#          *          # k=8, 10 spaces: 1 asterisks



levels = 5
for k in range(levels):
  number_of_spaces = levels - k
  for s in range(number_of_spaces):
    print(" ", end="")

  number_of_asterisks = k * 2 + 1

  for j in range(number_of_asterisks):
    print("*", end= "")

  print("")

# the second triangle starts below:

for k in range(levels - 1):
  number_of_spaces2 = k + 2
  for s in range(number_of_spaces2):
    print(" ", end="")

  number_of_asterisks2 = k//2 -1
  for j in range(number_of_asterisks2):
    print("*", end= "")

  print("")