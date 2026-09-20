# Problem 1: Create a dictionary that has 4 types of fruits as keys, and for for every fruit, the value is the color of that fruit. 

# Then, print the dictionary.

fruits = {
    "banana": "yellow",
    "kiwi": "green",
    "strawberry": "red",
    "apple": "green",


}

# print(fruits)

# Problem 2: Add two more fruits to the previous dictionary, and print the dictionary again.


fruits["mandarin"] = "orange"
fruits["blueberry"] = "blue"

# print(fruits)

# Problem 3: Update the color of apple to red, and print the dictionary again.

fruits["apple"] = "red"

#print(fruits)

# Problem 4: Delete the entry for banana, and print the dictionary again.

del fruits["banana"]

#print(fruits)

# Problem 5: Check if "kiwi" is in the dictionary, and if it is there, print its color. If it is not there, print "kiwi is not in the
#  dictionary."

# del fruits["kiwi"]
# if "kiwi" in fruits: 
#   print(fruits["kiwi"])
# else: 
#   print("kiwi does not exist in the dictionary.")

# Problem 6: Print all the fruits in the dictionary. (without the colors)

# print(fruits.keys())

# for key in fruits.keys():
#     print(key)

# what does iterable mean? An iterable object is a variable that has a collection of variables, and we can iterate over it.

# Problem 7: Print all the fruits whose color is red.
"""
for name, color in fruits.items():
    if color == "orange":
        print(name)
"""

# Problem 8: Count how many fruits in the dictionary have the color red.
"""
count = 0


for name, color in fruits.items():
    if color == "red":
        count += 1
        
print(count)

"""

# Problem 9: Count how many fruits in the dictionary contain the letter "a" in their name.

# count = 0

# for name in fruits.keys():
#     if "a" in name:
#         count += 1

# print(count)

# HW complete

# previous problems have been difficulty level 1. So now let's move to difficulty level 2.
# Problem 10: (level 2) Create a dictionary that has 4 types of fruits as keys, and for every fruit, 
# the value is a list of colors that the fruit can be. Then, print the dictionary.

fruits = {
    "apple": ["red", "green"],
    "orange": ["orange", "red"],
    "banana": ["green", "yellow"],
    "mandarin": ["orange"],
}

# print(fruits)


# Problem 11: (level 2) Scientists were able using genetic engineering to create a new color for oranges, which is blue. Update the dictionary by adding this new color to the oranges.

#my internet went out im trying to reconnect to the meet
# no worries

# lst = ["red", "blue"]
# lst.append("orange")

fruits["orange"].append("blue")

# print(fruits["orange"])


# Problem 12: (level 2) Given the dictionary below, print the key whose list has the largest number of elements.
#  For example, in the dictionary below, the key "d" has the largest list of elements, so you should just print "d".

numbers = {
    "a": [1, 2, 3],
    "b": [5, 1, 2],
    "c": [2, 2, 3, 9],
    "d": [1, 1, 1, 1, 1, 1]
}

# max_value = 0
# max_values_key = 0

# for key, value in numbers.items():
#     if len(value) > max_value:
#         max_value = len(value)
#         max_values_key = key

# print(max_values_key)


# Problem 13 (level 2) [Homework] Given the same dictionary above, find the key whose list has the largest 
# sum of numbers. For example, in the dictionary above, they key "c" has the largest sum, so you should just print c

# maxsum = 0
# max_sumkey = 0

# for key, value in numbers.items():
#     if sum(value) > maxsum:
#         maxsum = sum(value)
#         max_sumkey = key

# print(max_sumkey) 
# 


# Problem 14 (level 2) Given the same dictionary above, for each list in the dictionary, find the average of the 
# numbers in that list, and create a new dictionary with the same keys, but the values are the averages of the lists.
# Your output should be a new dictionary that looks like this: {"a": 2.0, "b": 2.666, "c": 4.0, "d": 1.0} 
# sumofvalues = 0
# average = 0
# average_values = {}



# for key, value in numbers.items():
#   sumofvalues = sum(value)
#   average = sumofvalues / len(value)
#   average_values[key] = average

# print(average_values)

# Problem 15 (level 3) Given the list below, create a dictionary that has a count of how many times each string appears in the list:

lst = ["ada", "bob", "lolo", "ada", "sana", "sana", "sana", "emilio", "bob", "sana", "lolo", "amit", "enas"]
namecount = {}
count = 0

for name in lst:
    if name not in namecount:
        namecount[name] = 1
    else:
        namecount[name] += 1
        


print(namecount)

"""


    for name in lst:
        if name == "ada":
            count += 1

    print(count)


    names = {
        "ada": "S",
        "bob": "A",
        "lolo": "B",
    }

    if "ada" in names:
        print("Exists")
    else:
        print("Does not exist")
"""

# Problem 16 (level 3) Given the same list above, create a dictionary that counts how many times each letter appears among all the names in the list. For example, if the letter a appears 10 times, and the letter b appears 5 times, your output should be a dictionary that looks like this: {"a": 10, "b": 5, ...}

