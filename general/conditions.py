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


x = 1
y = 2

z = (x > y) # False
z = False

z = (x > y)

# if z: # sth has to be a boolean, whether a boolean variable or a boolean statement

"""
You can combine boolean statements using the following operators:
1. and: both statements must be true
2. or: at least one statement must be true
3. not: reverses the boolean statement
"""

if (x > y):
    if (y > z):
        print("x is greater than y") 

if (x > y) and (y > z):
    print("x is greater than y and y is greater than z")

if (x > y) or (y > z):

if not (x > y):
    print("x is not greater than y")


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



