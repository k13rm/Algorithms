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
count = 0


for name, color in fruits.items():
    if color == "red":
        count += 1
        
print(count)

# Probkem 9: Count how many fruits in the dictionary contain the letter "a" in their name.