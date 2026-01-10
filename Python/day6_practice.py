"""Set Practice Set"""

""".....1) Create a set with 10 elements."""

# s = {10,20,30,40,50,60,70,80,90,100}
# print(s)


""".....2) Add 2 new elements to an existing set."""

# s = {10,20,30,40,50,60,70,80,90,100}
# s.update([25,35])
# print(s)


""".....3) Remove an element from a set using remove()."""

# s = {10,20,30,40,50,60,70,80,90,100}
# s.remove(40)
# print(s)


""".....4) Remove an element from a set using discard()."""

# s = {10,20,30,40,50,60,70,80,90,100}
# s.discard(50)
# print(s)


""".....5) Check whether a given element exists in a set or not."""

# s = {10,20,30,40,50,60,70,80,90,100}
# search = 30

# if search in s:
#     print("This element exists in the set")
# else:
#     print("This element does not exist in the set")


""".....6) Convert a list with duplicate values into a set."""

# s = [1,1,2,3,4,2,3,2,5]
# s = set(s)
# print(s)


""".....7) Find the length of a set."""

# s = {10,20,30,40}
# print(len(s))


""".....8) Find the union of two sets."""

# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a.union(b))


""".....9) Find the intersection of two sets."""

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a.intersection(b))


""".....10) Find the difference of two sets (A - B)."""

# A = {1,2,3,4}
# B = {3,4,5,6}

# print(A - B)


""".....11) Find the symmetric difference of two sets."""

# A = {1,2,3,4}
# B = {3,4,5,6}

# print(A ^ B)


""".....12) Check if one set is a subset of another."""

# A = {1,2,3,4}
# B = {3,4}

# if A.issubset(B): 
#     print("A is subset of B")

# elif B.issubset(A): 
#     print("B is subset of A")

# else: 
#     print("Both are different")


""".....13) Check if one set is a superset of another."""

# A = {1,2,3,4}
# B = {3,4}

# if A.issuperset(B): 
#     print("A is superset of B")

# elif B.issuperset(A): 
#     print("B is superset of A")

# else: 
#     print("Both are different")



""".....14) Check if two sets are equal."""

# A = {1,2,3,4}
# B = {1,2,3,4}

# if A == B: 
#     print("Both are equal")
# else: 
#     print("Both are not equal")


""".....15) Remove duplicates from a list without using loops (only set)."""

# s = [1,1,2,2,3,4,3,2,5]
# s = set(s)
# print(s)


""".....16) Given two sets, keep only the elements that are 
unique to both (no common element)."""

# a = {10, 20, 30, 40}
# b = {40, 50, 60, 70}

# result = a ^ b     
# print(result)


""".....17) Print the maximum and minimum element of a numeric set."""

# a = {10, 20, 30, 40, 5, 98, 73}
# print(f"Maximum : {max(a)}")
# print(f"Minimum : {min(a)}")


""".....18) Count how many vowels are present in a set of characters."""

# s = {10, "pruthviraj", 30, 34.45, True}
# count = 0

# for item in s:
#     if isinstance(item, str):        
#         for ch in item:
#             if ch in "aeiouAEIOU":
#                 count += 1

# print(count)


""".....19) Write a program to print elements present 
in Set A but not in Set B AND Set B but not in Set A (double difference)."""

# A = {1,2,3,4,5,6}
# B = {5,6,7,8,9,10}

# print("Elements only in A:", A - B)
# print("Elements only in B:", B - A)



""".....20) Convert a set of mixed values into a sorted list."""

a = {10, "apple", 5, "cat"}
result = sorted(a, key=str)
print(result)




"""Dictionary Practice Set"""

#...Hashing....

#.....1) Print Unique elements in list.....
"""
    display all distinct elements present in the given list.
"""

# a = [1,1,1,2,2,2,3,3,3,3,3,4,4,4,5,5,6,6,6,6,7,7]

# d = {}

# for i in a: 
#     if i in d.keys(): 
#         d[i] +=1
#     else: 
#         d[i] = 1

# print(d.keys())


#.....2) Count Frequency of Array elements.....
"""
    count how many times each element appers using
    a dictionary or hash map.
"""

# a = {1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,6,6,6,7}

# d = {}

# for i in a: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1
# print(d)


#.....3) Leetcode 771 - jewels and stones.....
"""
    count how many stones are also jewels
    based on give strings.
"""

# jewels = "aA"
# stones = "aAAbbbb"
# d = {}

# for i in stones: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1

# count = 0

# for i in d.keys(): 
#     if i in jewels: 
#         count += d[i]
# print(count)


#.....4) Leetcode 1832 - pangram check.....
"""
    verify if a sentence contains every letters of the english 
    alphabet at least once.
"""

# sentence = "leetcode"
# d = {}

# for i in sentence: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1

# if len(d.keys()) == 26: 
#     print("True")
# else: 
#     print("False")



#.....5) Leetcode 2351 - first letter to appear twice.....
"""
    find the first character that appears twice in a string.
"""

# s = "abccbaacz"
# d = {}
# for i in s: 
#     if i in d.keys(): 
#         print(i)
#         break
#     else: 
#         d[i] = 1


#.....6) Leetcode 1748 - sum of unique elements.....
"""
    return the sum of elements that appear exactly
    once in the array.
"""

a = [1,2,3,2,4,5]
d = {}

for i in a: 
    if i in d.keys(): 
        d[i] += 1
    else: 
        d[i] = 1
sum = 0
for i in d: 
    if d[i] == 1: 
        sum += i
print(sum)




"""Dictionary Practice Set - 2"""

#.....1) Leetcode 2418 - sort the people.....
"""
    sort the name of the people based on their 
    heights in decreasing order
"""

# names = ["Mary", "Jhon", "Emma"]
# heights = [180, 165, 170]

# d = {}
# for i in range(len(names)): 
#     d[heights[i]] = names[i]
# d = sorted(d.items(), key=lambda x:x[0], reverse = True)

# for i in range(len(d)):
#     names[i] = d[i][1]
# print(names)


#.....2) Check if two strings have same frequency map.....
"""
    compare character frequencies of two strings and 
    check if they match.
"""

# s1 = "aabbcc"
# s2 = "baccab"

# if len(s1) == len(s2): 
#     d = {}

#     for i in s1:
#         if i in d.keys(): 
#             d[i] += 1
#         else: 
#             d[i] = 1

#     for i in s2: 
#         if i in d.keys(): 
#             d[i] -= 1
#         else: 
#             print("An extra element was found")

#     for i in d: 
#         if d[i] != 0:
#             print("your elements are not same") 
#             break
#     else: 
#         print("your strings are same")

# else: 
#     print("Strings are not same")



#.....3) Find duplicates in array using hashset.....
"""
    detect and print elements that appear more than once
    in the array.
"""  

# a = [1,1,3,3,3,5,5,6,6,6,3,5,3,2,3,4,6,7,8,8,0]
# d = {}

# for i in a: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1

# for i in d.keys():
#     if d[i] > 1: 
#         print(i) 
    


#.....4) Leetcode 2404 - Most frequenct even element.....
"""
    find the even number with the highest frequency, return 
    the smallest one if ties exist
"""  

# nums = [0,1,6,6,4,4]
# d = {}

# for i in nums: 
#     if i % 2 == 0: 
#         if i in d.keys(): 
#             d[i] += 1
#         else: 
#             d[i] = 1

# if not d: 
#     print(-1)

# max_f = max(d.values())

# cand = [num for num, freq in d.items() if freq == max_f]

# print(min(cand))



#.....5) Leetcode 2283 - check if number has equal digit count and digit value.....
"""
    determine if the count if each digit matches its value in the string.
"""  
# num = "1210"
# d = {}

# for i in num: 
#     if i in d.keys(): 
#         d[i] += 1
#     else: 
#         d[i] = 1

# for i in range(len(num)): 
#     if d.get(str(i), 0) == int(num[i]): 
#         continue
#     else: 
#         print("False")



#.....6) Intersection of two arrays.....
"""
    return all the unique elements that appear in both arrays.
""" 

a = [1,2,3,4,5]
b = [4,5,6,7,8]

j = []
d = {}
for i in a: 
    if i in d.keys(): 
        d[i] += 1
    else: 
        d[i] = 1

for i in d.keys(): 
    if i in b: 
        j.append(i)
print(j)