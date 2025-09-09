
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

floors = 1000

for k in range(floors):
    for j in range(0, k):
      print("*", end="")
    print("\n")

# print a christmas tree way:
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************

levels = 10