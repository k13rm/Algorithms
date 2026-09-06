# Data Structures: ways to store and organize data in the computer.
# a variable is the simplest data structure. It can store one value at a time.
# x = 5
# print(x)
# name = "Alice"
# print(name)
# How can I store a collection of values? I can use a list.
# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# names = ["Alice", "Bob", "Charlie", "David"]
# to retrieve a value from a list, we need to use the index of the value.
# print(lst[3])
# print(names[0])

# What if I want to retrieve the index by giving the name as input? Using a list will be slow.
# Instead a Dictionary provides a solution.

# Hash Table: sha256("password122") = 0x3bc51062973c458d5ddf4e5b9c1f0a2f

# A dictionary is a data structure that stores key-value pairs. It allows us to retrieve the value associated with a key in a very efficient way.

d = {} # curly brackets are used to create an empty dictionary
d["Alice"] = 25 # Alice is called the key, and 25 is called the value. We can use any data type for the key.
d["Alice"] = 30 # this would overwrite the previous value
d["Bob"] = 30
d["Charlie"] = 35
d["David"] = 40
d[12312] = "Whatever"
d['a'] = 2312

# print(d["Alice"])
# print(d["David"])

surnames = {
    "Alice": "Davis",
    "Bob": "Johnson",
    "Charlie": "Williams",
    "David": "Brown"
}

# Tuple: it is a data structure that is similar to a list, but it is immutable. It means that we cannot change the values in a tuple after it is created. We can use it as a key in a dictionary, but we cannot use a list as a key in a dictionary.
# [] square brackets denote a list
# () round brackets denote a tuple
# {} curly brackets denote a dictionary

surnames[("Alice", "August,2000")]  = "Davis"
surnames["Alice"] = ["Smith", "Davis"]


# how to delete
del surnames["Bob"]
# print(surnames)

# how to overwrite
surnames["Alice"] = "Davis"

# how to check if a key is in the dictionary
# print(surnames["Kerem"]) this would cause an error because "Kerem" is not a key in the dictionary.
# Therefore, it would be better to check if the key is in the dictionary before trying to retrieve its value.

# surnames["Kerem"] = "Duruk"
if "Kerem" in surnames:
     print("Kerem's surname is:", surnames["Kerem"])
else:
     print("Kerem is not in the dictionary.")


# What if we want to do a for loop over the dictionary? There are multiple ways.

# first type:
for key, value in surnames.items():
    print(key,":", value) 

# second type: go over the keys only, and then retrieve the value using the key.
for key in surnames:
    print(key, ":", surnames[key])
# a second way to go over the keys only:
for key in surnames.keys():
    print(key, ":", surnames[key])

print("Printing Values only:")
for value in surnames.values():
     print(value)


# Now, let's see how to solve some problems with dictionaries.

# Problem 1: (easy) Given a list of student names, and a list of numbers in two separate lists,
# create a dictionary that maps the student names to their corresponding numbers. For example, if the list of names is ["Alice", "Bob", "Charlie", "David"] and the list of numbers is [25, 30, 35, 40], then the output should be: 
# {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}

names = ["Alice", "Bob", "Charlie", "David"]
numbers = [25, 30, 35, 40]
k = 0
dict1 = {}
for k in range(len(numbers)):
    dict1[names[k]]=numbers[k]
print(dict1)