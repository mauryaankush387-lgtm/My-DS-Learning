"""....Data Structures...."""

#   - A data structure is a special way of storing
# and organizing data so that it can be used efficiently.

#   - You can think of data structures like containers:
#   - Some containers maintain order (List, Tuple)
#   - Some contain unique items (Set)
#   - Some store data as key–value pairs (Dictionary)

#   - Python gives us built-in data structures, meaning you do NOT need to import anything.
#   - The four main built-in data structures are:
#           1) List
#           2) Tuple
#           3) Set
#           4) Dictionary



"""....1) LIST in Python...."""
#       - A list is a mutable, ordered, and index-based collection of items.


# ....1) How to create a list : 
# my_list = [1, 2, 3, 4]


# ....2) List is Ordered : 
#          - The items inside a list have a fixed order.

# example : 
# fruits = ["apple", "banana", "mango"]



# ....3) List is Mutable (Can be changed) : 
#           - You can modify lists after creating them.

# example: 
# numbers = [10, 20, 30]
# numbers[1] = 200
# print(numbers)          # [10, 200, 30]



# ....4) List allows duplicate values :
#           - Duplicates are allowed.

# example: 
# a = [1, 2, 2, 3, 3, 3]



# ....5) List can store different data types :
#           - Python lists can contain anything.

# example: 
# mixed = [10, "hello", 3.14, True]



# ....6) Accessing elements (Indexing) :

# nums = [4, 5, 6]
# print(nums[0])  # 4
# print(nums[2])  # 6



# ....7) Slicing (Getting part of a list) :

# marks = [10, 20, 30, 40, 50]
# print(marks[1:4])               # [20, 30, 40]



"""....Iterating through a list...."""

#....1) Directly accessing values : 

# a = [10,20,30,40]
# for i in a: 
#     print(a)

#.....output.....
#       10
#       20
#       30
#       40


#....2) On the basis of index (using range function) : 

# a = [10,20,30,40]
# for i in range(len(a)): 
#     print(f"{i} : {a[i]}")

#.....output.....
#      0 : 10
#      1 : 20
#      2 : 30
#      3 : 40



"""....Methods in list...."""

a = [10,20,30,40]

# Append (add at end) :
a.append(50)       # [10,20,30,40,50]

# Insert (add at specific position): 
a.insert(2,25)     # [10,20,25,30,40] 

# Remove item : 
a.remove(40)       # [10,20,30]

# Pop (remove by index) :
a.pop(2)            # [10,20,40]

# Sort a list :
b = [10,4,3,50]
b.sort()
print(b)        [3,4,10,50]


""" 
Note: Many more methods are available for lists. 
To view all built-in list methods, use the help(list) function.
"""




"""....2) Tuple in Python...."""
#         - A tuple is a Python data structure used to store multiple items in a single variable.
#         - It is almost like a list, but with one big difference:
#             - Tuple is Immutable (You cannot change, add, remove, or modify items after creation.)

"""....How to Create Tuples...."""

#.....Normal tuple.....
# t = (1, 2, 3)


#.....Single-element tuple — must add comma!.....
# t = (5,)   # correct

# Without comma:
# t = (5)    # this is NOT a tuple, it's an integer


#.....Tuple without parentheses.....
# t = 10, 20, 30      # Tuple packing.




"""....Properties of Tuple...."""

#.....1) Ordered.....
#       - Items have fixed index positions.

# example:
# t = (1, 2, 3)
# index: 0 1 2



#.....2) Immutable (Cannot modify).....
#       - You cannot change any item.

# example:
# t = (10, 20, 30)
# t[1] = 200    # ❌ ERROR



#.....3) Allows duplicates.....

# example:
# t = (1, 1, 2, 2, 3)



#.....4) Can store different data types.....

# example:
# t = (10, "hello", 3.5, True)



#.....5) Supports indexing & slicing.....

# example:
# t = (10, 20, 30, 40)
# print(t[1])      # 20
# print(t[1:3])    # (20, 30)



"""....Unpacking a Tuple...."""

# t = (10, 20, 30)
# a, b, c = t
# print(a, b, c)

#....Output:...
# 10 20 30



"""....Tuple Traversing...."""

#....1) Directly accessing values : 

# a = (10,20,30,40)
# for i in a: 
#     print(a)

#.....output.....
#       10
#       20
#       30
#       40


#....2) On the basis of index (using range function) : 

# a = (10,20,30,40)
# for i in range(len(a)): 
#     print(f"{i} : {a[i]}")

#.....output.....
#      0 : 10
#      1 : 20
#      2 : 30
#      3 : 40


"""....Tuple Methods...."""

#....1) count() — count occurrences :
t = (1, 2, 2, 3)
print(t.count(2))     # 2


#....2) index() — find position of value :
print(t.index(3))     # 3rd index (0-based)