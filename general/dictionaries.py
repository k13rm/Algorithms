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

# A dictionary is a data structure that stores key-value pairs. It allows us to retrieve the value associated with a key in a very efficient way.

d = {} # curly brackets are used to create an empty dictionary
d["Alice"] = 25 # Alice is called the key, and 25 is called the value. We can use any data type for the key.
d["Bob"] = 30
d["Charlie"] = 35
d["David"] = 40
d[12312] = "Whatever"
d['a'] = 2312

# print(d["Alice"])
# print(d["David"])

surnames = {
    "Alice": "Smith",
    "Alice": "Davis",
    "Bob": "Johnson",
    "Charlie": "Williams",
    "David": "Brown"
}

surnames[("Alice", "August,2000")]  = "Davis"
surnames["Alice"] = ["Smith", "Davis"]


# how to delete
# del surnames["Bob"]
# print(surnames)

# how to overwrite
# surnames["Alice"] = "Davis"

# how to check if a key is in the dictionary
# print(surnames["Kerem"]) this would cause an error because "Kerem" is not a key in the dictionary.
# Therefore, it would be better to check if the key is in the dictionary before trying to retrieve its value.

# surnames["Kerem"] = "Duruk"
# if "Kerem" in surnames:
#     print("Kerem's surname is:", surnames["Kerem"])
# else:
#     print("Kerem is not in the dictionary.")


# What if we want to do a for loop over the dictionary? There are multiple ways.

# first type:
for key, value in surnames.items():
    print(key,":", value) 

# second type: go over the keys only, and then retrieve the value using the key.
for key in surnames:
    print(key, ":", surnames[key])