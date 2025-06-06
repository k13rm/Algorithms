# pseudo-code
# if sth is true:
#     do sth
# elif sth is true:
#     do sth
# elif sth else is true:
#     do sth else
# else:
#     do sth different

# user_input = input("what is a number between 20 and 30?")
# user_input = int(user_input)

# if user_input > 30: # a condition
#     print("the number is too high")
# elif user_input < 20:
#     print("the number is too low")
# elif user_input == 20:
#     print("the number is 20, just on the edge")
# elif user_input == 30:
#     print("the number is 30, just on the edge")
# else:
#     print("the number is between 20 and 30")


"""
A condition is a statement in python that can be true or false.
Another name for conditions is boolean statements.

A boolean variable is a variable that can be true or false.

Reminder:
Types of variables in python:
1. int: integer numbers, example: 1, 2, 3, 4, 5
2. float: decimal numbers, example: 1.0, 2.3, 4.5
3. str: string, example: "hello", "world"
4. list: a list of numbers, example: [1, 2, 3, 4, 5]

5. bool: boolean, example: True, False

1GB = 1024MB
1MB = 1024KB
1KB = 1024B
1B = 8 bits
1 bit = 0 or 1

comparison operators:
1. >  : greater than
2. <  : less than
3. >= : greater than or equal to
4. <= : less than or equal to
5. == : equal to
6. != : not equal to
"""


# x = 1
# y = 2

# z = (x > y) # False
# z = False

# z = (x > y)

# if z: # sth has to be a boolean, whether a boolean variable or a boolean statement

"""
You can combine boolean statements using the following operators:
1. and: both statements must be true
2. or: at least one statement must be true
3. not: reverses the boolean statement
"""

# if (x > y):
#     if (y > z):
#         print("x is greater than y") 

# if (x > y) and (y > z):
#     print("x is greater than y and y is greater than z")

# if (x > y) or (y > z):

# if not (x > y):
#     print("x is not greater than y")


"""
Problem: A user will give you their course grade which is between 0 and 100.

You need to give them their letter grade. The grade scale is as follows:
A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: 0 - 59
"""

#use input to determine grade accuracy



# print("Put your grade in for your class, the grade scale will determine wether you've gotten an A or B and etc.")
# grade = int(input("Enter grade here (ex: 90 or 76):"))
# if grade >= 90:
#     print("You got an 'A'")
# elif grade >= 80:
#     print("You got a 'B'")
# elif grade >= 70:
#     print("You got a 'C'")
# elif grade >= 60:
#     print("You got a 'D'")
# else:
#     print("You got a 'F'")


# """
# Given a list of numbers, if the list has the number 2 or 5, increase the counter by one
# for each number. If the list has the numbers 3 and 7, decrease the counter by one.
# """
# counter = 0
# lst = [1, 2, 3, 2, 4, 5, 7, 8 ,9]
# if 2 in lst:
#     counter += 1
# if 5 in lst:
#     counter += 1
# if 3 in lst:
#     counter -= 1
# if 7 in lst:
#     counter -= 1


"""
Problem: We have two friends, Jonathan and Rick. They want to go on a school trip. However, in order for their teacher to allow them to go to the trip, they must score high at the maths exam.
This means the sum of both of their scores needs to be over 70. If both of them score over 90, they will get free ice cream on the trip. You will take the scores of Jonathan and Rick as input,
and then first you need to tell them if they will go on the trip or not, and then you need to tell them if they will get ice cream or not.

"""

# Jscore = 0
# Rscore = 0

# Jscore = int(input("How much did Jonathan score? \ntype here:"))
# Rscore = int(input("How much did Rick score? \ntype here:"))

# if (Jscore + Rscore) / 2 > 69:
#   print("They will go on a trip.")
# else:
#   print("They both failed the exam so they won't be able to go on a trip.")
# if (Jscore + Rscore) / 2 > 89:
#   print("Also they will get free ice cream.")


"""
Homework Problem: We have two friends, Jonathan and Rick. They want to go on a school trip. However, in order for their teacher to allow them to go to the trip, they must score high at the maths exam.
This means the sum of both of their scores needs to be over 70. If both of 
them score over 90, they will get free ice cream on the trip. In addition, if either of them scores below 60, they can to the trip but whoever scored below 60 must pay a fine.

For example, if Jonathan scores 55 and Rick scores 90, they will both still go, but Jonathan will have to pay a fine because he scored less than 60

 You will take the scores of Jonathan and Rick as input,
and then first you need to tell them if they will go on the trip or not, and then you need to tell them if they will get ice cream or not. If someone will pay fine you should print a message specifying that.`

"""

Jscore = 0
Rscore = 0

Jscore = int(input("How much did Jonathan score? \ntype here:"))
Rscore = int(input("How much did Rick score? \ntype here:"))

if Jscore > 69 and Rscore > 69:
   print("They will go on a trip")
if Jscore > 69 and Rscore < 70:
   print("Jonathan will go on a trip, Rick still can go but has to pay.")
if Jscore < 70 and Rscore > 69:
   print("Rick will go on a trip, Jonathan still can go but has to pay.")   
if Jscore < 70 and Rscore < 70:   
   print("They both failed the exam but they can still pay to go on a trip.")
else:
   print("Error, calculate again.")