
"""....3) Set in Python...."""

#  - A set is a built-in data structure in Python used to store 
#    multiple items in a single variable, but:

#       - Order is NOT guaranteed.
#       - Duplicate values are NOT allowed.


"""....Properties of a Set...."""

# 1) Unordered  -  No fixed index / arrangement
# 2) Unindexed	- Cannot access values by index
# 3) No duplicates - Automatically removes repeated values
# 4) Mutable - You can add or remove elements
# 5) Mixed data allowed	- Integers, strings, floats, etc.


"""....Example...."""

# s = {10, 20, 30, 20, 30}
# print(s)

#....output.....
# {10, 20, 30}

#   - Duplicates are automatically removed.


"""....Creating a Set...."""

# s = {1, 2, 3}

# #.....Empty set : 

# s = set()      # correct
# s = {}         # ❌ creates dictionary, not set


"""....Set Traversing...."""

#   - Traverse on the basis of values - it will run on the basis 
#       of hash values.
#   - unordered traversing always. 
#   - No index values so no traversing on the basis of index.


"""....Set Methods...."""

""".....Adding and Removing Elements....."""

# s = {10,20,30,40}

# s.add(50)  # Add an element
# s.update([60, 70, 80])   # Add multiple elements
# s.remove(20)   # Remove an element (error if element doesn't exist)
# s.discard(20)  # Remove safely (no error if element not present)
# s.pop()        # Remove random element
# s.clear()      # Clear entire set 


""".....Set Operations....."""

# 1) Union        -  A | B    or     A.intersection(B)
# 2) Intersection -  A & B    or     A.intersection(B)
# 3) Difference   -  A - B    or     A.difference(B)
# 4) Symmetric    -  A ^ B    or     A.symmetric_difference(B)
#    Difference


#....Example....

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union
print(A & B)   # Intersection
print(A - B)   # Difference
print(A ^ B)   # Symmetric Difference

#....Output....

# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {1, 2}
# {1, 2, 5, 6}


""" 
Note: Many more methods are available for sets. 
To view all built-in set methods, use the help(set) function.
"""


"""....4) Dictionary in Python...."""
#   A dictionary is a collection of key–value pairs.

#   Syntax :
#       dict_name = {key: value, key: value, ...}

#.....Example : 

# student = {
#     "name": "Pruthviraj",
#     "age": 22,
#     "course": "Python"
# }


"""....Properties of a Dictionary...."""

# 1) Ordered  -  Yes (Python 3.7+)
# 2) Mutable	- Yes
# 3) Duplicate keys allowed - No
# 4) Indexing - Based on keys
# 5) Heterogeneous values	- Allowed


"""....Creating a Dictionary...."""

# d1 = {}                                      # empty
# d2 = {"a": 1, "b": 2, "c": 3}                 # with values
# d3 = dict(name="Alex", age=30)               # using dict()
# d4 = dict([("x", 10), ("y", 20)])            # from list of tuples


"""....Adding / Updating Elements...."""

# student = {
#     "name": "Pruthviraj",
#     "age": 22,
#     "course": "Python"
# }

# student["age"] = 23       # update
# student["city"] = "Pune"  # add

# print(student)
# {'name': 'Pruthviraj', 'age': 23, 'course': 'Python', 'city': 'Pune'}


"""....Removing Elements (Function and Their Usage)...."""

# pop(key)      - Removes & returns value
# popitem()     - Removes last inserted key–value pair
# del dict[key] - Deletes key
# clear()       - Removes all items


#.....Example :

# student = {
#     "name": "Pruthviraj",
#     "age": 22,
#     "course": "Python"
# }

# student.pop("age") 
# student.popitem()            
# del student["name"]
# student.clear()


"""....Looping in Dictionary...."""

#.....Example :

# student = {
#     "name": "Pruthviraj",
#     "age": 22,
#     "course": "Python"
# }

# for key in student:
#     print(key) # print keys only.

# for value in student.values():
#     print(value) # print values only.

# for k, v in student.items():
#     print(k, v) # print keys and values.


"""....Dictionary Useful Methods...."""

# keys()    - returns all keys
# values()  - returns all values
# items()   - returns key–value pairs
# update()  - merges 2 dictionaries
# copy()    - creates shallow copy
# setdefault() - returns value of key, if not present inserts it


"""....Nested Dictionary...."""

# students = {
#     1: {"name": "Pruthviraj", "age": 21},
#     2: {"name": "Rohan", "age": 22}
# }
# print(students[1]["name"])  # Pruthviraj


"""....Convert Between Dictionary & Other Data Types...."""

# Tuple of tuples → dict
# dict(((1, "A"), (2, "B")))

# # List of tuples → dict
# dict([(1, "A"), (2, "B")])


"""....Copy vs Deep Copy...."""

import copy
d1 = {"a": 1, "b": [10, 20]}

d2 = d1.copy()            # shallow
d3 = copy.deepcopy(d1)    # deep


