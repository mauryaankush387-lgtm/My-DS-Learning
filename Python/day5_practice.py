
"""List Practice Set"""

#.....1) Sum and average of list.....
"""
    create a list of numbers, then calculate and print 
    the total sum and average.
"""

# a = [10,20,30,40]
# total_sum = 0
# for i in a: 
#     total_sum = total_sum + i

# print(f"Total sum is {total_sum} and their average is {total_sum/len(a)}")



#.....2) Maximum element with index.....
"""
    find the largest element in the list along with 
    it's position (index).
"""

# a = [1,4,2,4,56,7,46,9,90]
# largest = a[0]
# index = 0

# for i in range(len(a)): 
#     if a[i] > largest: 
#         largest = a[i]
#         index = i
# print(f"Your Maximum element is {largest} at index {index}")



#.....3) Second Greatest element.....
"""
    identify the second-largest element in the list 
    without sorting directly.
"""

# a = [3,2,43,56,75,46,90,89]

# max = a[0]
# max2 = a[0]
# index = 0
# index2 = 0

# for i in range(len(a)): 
#     if a[i] > max: 
#         max2 = max
#         index2 = index
#         max = a[i]
#         index = i

#     elif a[i] > max2: 
#         max2 = a[i]
#         index2 = i

# print(f"Your maximum number is {max} at {index}")
# print(f"Your Second maximum number is {max2} at {index2}")



#.....4) Check if list is sorted (increasing).....
"""
    verify whether the list elements are in ascending order.
"""

# a = [1,2,3,4,5,6]

# for i in range(len(a)-1): 
#     if a[i] < a[i+1]: 
#         continue
#     else: 
#         print("This number is not sorted")
#         break
# else: 
#     print("Your list is sorted")



#.....5) Left Rotation By 1 .....
"""
    shift all elements one position to the left, with the first element 
    moving to the end.
"""

# a = [10,20,30,40,50]

# for i in range(len(a)-1): 
#     a[i],a[i+1] = a[i+1],a[i]
# print(a)



#.....6) Right Rotation By 1 .....
"""
    shift all elements one position to the right, with the last element 
    moving to the first.
"""

# a = [10,20,30,40,50]

# for i in range(len(a)-1,0,-1): 
#     a[i],a[i-1] = a[i-1],a[i]
# print(a)



#.....7) Left Rotation By k .....
"""
    generalize the previous problem: 
    rotate the list by k time to the left.
"""

# k = int(input("How many times you want to rotate : "))
# a = [10,20,30,40,50]

# for i in range(k): 
#     for i in range(len(a)-1): 
#         a[i], a[i+1] = a[i+1], a[i]

# print(a)



#.....8) Reverse List (In-Place ).....
"""
    reverse the entire list without using extra space
    [i.e., swap elements.]
"""

a = [10,20,30,40,50]
b = len(a) - 1

for i in range(len(a)//2): 
    a[i],a[b] = a[b],a[i]
    b = b - 1
print(a)


"""List Practice Set-2"""

#.....1) Linear Search.....
"""
    search for a given element by checking each 
    element one by one.
"""

# a = [3,4,6,34,59,60,38,96]
# search = int(input("Tell your number: "))

# for i in range(len(a)): 
#     if a[i] == search: 
#         print(f"element found at index {i}")
#         break
# else: 
#     print("Sorry no such element exist")



#.....2) Binary Search.....
"""
    efficiently Search for an element in a sorted list using 
    the divide-and-conquer approach.
"""

# a = [12,14,16,23,25,34,37,45,48,59,68,70]

# search = 13

# start = 0
# last = len(a)-1
# mid = (start + last)//2

# while start <= last:
#     if a[mid] == search:
#         print(f"element found at index {mid}")
#         break
#     elif a[mid] < search:
#         start = mid + 1
#         mid = (start + last)//2
    
#     elif a[mid] > search:
#         last= mid -1
#         mid = (start + last)//2
# else:
#     print("sorry no such element exist")


#.....3) Bubble Sort.....
"""
    sort the list by repeatedly swapping adjacent elements
    if they are in the wrong order.
"""

# a = [56,234,23,24,46,6878,9,674,52,3,12,13,368]

# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]

# print(a)


#.....4) Selection Sort.....
"""
    sort the list by selecting the smallest element in each
    pass and placing it in the correct.
"""

a = [56,234,23,24,46,6878,9,674,52,3,12,13,368]

for i in range(len(a)-1):
    j = i+1
    min = i
    for k in range(j,len(a)):
        if a[k] <a[min]:
            min = k
    
    a[i],a[min] = a[min],a[i]

print(a)



"""Tuple Practice Set"""

""".....1) Create a tuple with five numbers and print it."""

# t = (10,20,30,40,50)
# print(t)


""".....2) Access the first and last element of a tuple."""

# t = (10,20,30,40,50)
# first_element = t[0]
# last_element = t[-1]
# print(f"first element : {first_element} and last element : {last_element}")


""".....3) Check whether an element exists in a tuple."""

# t = (10,23,45,3,5,35,34,78)
# a = 34

# for i in range(len(t)): 
#     if t[i] == a: 
#         print("this element exists in the tuple")
#         break
# else: 
#     print("this element does not exist in the tuple")


""".....4) Concatenate two tuples and print the result."""

# t1 = (10,20,30)
# t2 = (40,50,60)

# print(t1 + t2)


""".....5) Repeat a tuple 3 times using the * operator."""

# t = (10,20,30,40,50)
# print(t * 3)


""".....6) Find the maximum and minimum element in a tuple of numbers."""

# t = (10,45,67,34,75,79,30,90,42,53)
# print(f"maximum : {max(t)} and minimum : {min(t)}")


""".....7) Convert a tuple to a list, modify the list, and convert it back to a tuple."""

# t = (10,20,30,40)
# lst = list(t)
# lst.append(50)
# lst.append(60)
# lst.append(70)
# print(tuple(lst))


""".....8) Unpack a tuple of 4 values into 4 variables and print them."""

# t = (10,20,30,40)
# a,b,c,d = t
# print(a,b,c,d)


""".....9) Swap two tuples without using a third variable."""

# t1 = (10, 20, 30)
# t2 = (40, 50, 60)

# print("Before swapping:")
# print("t1 =", t1)
# print("t2 =", t2)

# t1, t2 = t2, t1  

# print("After swapping:")
# print("t1 =", t1)
# print("t2 =", t2)


""".....10) Check if two tuples are equal or not."""

# t1 = (10,20,30,40)
# t2 = (10,20,30,40)

# if t1 == t2: 
#     print("Both tuples are equal")
# else: 
#     print("Both tuples are not equal")


""".....11) Remove all duplicate elements from a tuple."""
# (Result must still be a tuple)

# t = (1,2,3,2,4,2,4,5)
# unique = []

# for i in t: 
#     if i not in unique: 
#         unique.append(i)
# print(tuple(unique))


""".....12) Find the sum and average of all elements in a tuple."""

# t = (10,20,30,40,50)
# sum = 0

# for i in range(len(t)): 
#     sum = sum + t[i]
# print(f"Sum : {sum} and Average : {sum/len(t)}")


""".....13) Check if all elements in a tuple are integers."""

# t = (10, 23.54, 45, 95, "Pruthviraj")

# all_integers = True

# for item in t:
#     if not isinstance(item, int):
#         all_integers = False
#         break

# if all_integers:
#     print("All elements are integers")
# else:
#     print("Not all elements are integers")



""".....14) Given a tuple of tuples, print all the elements individually."""
# ((1,2), (3,4), (5,6))

# t = ((1,2), (3,4), (5,6))
# for inner in t: 
#     for i in inner: 
#         print(i) 
    

""".....15) Find the element with the highest frequency in a tuple."""

t = (1,1,2,3,4,4,5,3,2,3,3,3,2)

max_count = 0
max_element = None

for x in t:
    c = t.count(x)
    if c > max_count:
        max_count = c
        max_element = x

print("Element with highest frequency:", max_element)
print("Frequency:", max_count)