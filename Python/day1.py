print("Hello World!")

# This is a single line comment 

""" This is a 
multiline Comment """


'''........................................................................'''

# Variables

a = 12
b = 67


# Naming Convensions (There Are 3 Cases)

# ....1) Camel Case....
pruthvirajChavan = 99

# ....2) Pascal Case....
PruthvirajChavan = 67  

# ....3) Snake Case....
pruthviraj_chavan = 45


'''........................................................................'''

""" Data Types (We store the data types in the variable) """

# There are 3 types

#.... 1) Number : int (1,2,-3,-7,0), float (12.34, 67.90), complex (2j, 3j)

a = 45            # data type is integer 
b = 23.42         # data type is float
c = 2j            # data type is complex


#....2) String : use to store anything in " " or ' '

a = 'Ankush Maurya'          # data type is string 
name = "Python"                  # data type is string 


#....3) Boolean : True, False

name = True              # data type is boolean
is_active = False        # data type is boolean

""".....String...."""


#...1) String Indexing...

# a) Positive Indexing

# a = "NATURE"
# print(a[3])                #output : U

# b) Negative Indexing

# b = "Ankush Maurya"
# print(b[-1])               #output : a



#...2) String Slicing...

# a = "Hello I Am Data Scientist"

# print(a[::])      #output : Hello I Am Data Scientist
# print(a[:5])      #output : Hello
# print(a[11:15])   #output : Data 
# print(a[16:])     ##output : Scientist


#...3) Immutable Nature...

# a = "hzllo"
# a[1] = 'e'    #show error because it is immutable



""".....Print Statement Ways...."""

#....1) Narmal Way....

# name = "Rohit Sharma"
# age = 38

# print("My name is",name,"and my age is",age)

#...output....
# My name is Rohit Sharma and my age is 38



#....2) Formatted String Way....

# name = "Ankush Maurya"
# age = 21

# print(f"My Name is {name} and my age is {age}")   

#...output....
# My Name is Ankush Maurya and my age is 21



""".....Type Conversion...."""

# a = "23"         # string
# a = int(a)       # convert Sring to int

# b = 56           # integer
# b = float(b)     # convert integer to float

# a = 0            # integer
# print(bool(a))   # convert interger to boolean


''' Truthy Values : almost everything 
    Falsy Values : 0, 0.0, False, "", [], {}, () '''



""".....Input Statement...."""

# name = input("Tell Your Name : ")
# age = int(input("Tell Your Age : "))
# print(f"My Name is {name} and My Age is {age}")


"""............. Arithmetic Operator ............"""

# num1 = 6
# num2 = 3

# print(f"Addition of {num1} + {num2} = {num1 + num2}")
# print(f"Substraction of {num1} - {num2} = {num1 - num2}")
# print(f"Multiplication of {num1} * {num2} = {num1 * num2}")
# print(f"Division of {num1} / {num2} = {num1 / num2}")
# print(f"Floor Divison of {num1} // {num2} = {num1 // num2}")
# print(f"Modulo Division of {num1} % {num2} = {num1 % num2}")
# print(f"exponential of {num1} ** {num2} = {num1 ** num2}")


#.....Output......

# Addition of 6 + 3 = 9
# Substraction of 6 - 3 = 3
# Multiplication of 6 * 3 = 18
# Division of 6 / 3 = 2.0
# Floor Divison of 6 // 3 = 2
# Modulo Division of 6 % 3 = 0
# exponential of 6 ** 3 = 216


"""............. Assignment Operator / Shorthand Operators ............"""

#...Assignment Operator : =
# The assignment operator is used to store a value in a variable.

# x = 10
# y = 5
# name = "Pruthviraj"

#...Shorthand Operators : (+=, -=, *=, /=, //=, %=, **=) 

# x = 10

# x += 5   # x = x + 5 → x becomes 15
# x -= 3   # x = x - 3 → x becomes 12
# x *= 2   # x = x * 2 → x becomes 24
# x /= 4   # x = x / 4 → x becomes 6.0
# x %= 5   # x = x % 5 → x becomes 1.0



"""............. Comparison Operators ............"""

# Comparison Operators : ( ==, !=, >, <, >=, <= )

# a = 10
# b = 12

# print(a == b)       # False
# print(a != b)       # True
# print(a > b)        # False
# print(a < b)        # True
# print(a >= b)       # False
# print(a <= b)       # True


"""............. Logical Operators ............"""

# Logical Operators : ( and, or, not )

#.... 1) and....
# The and operator gives True only when all conditions are True.
# If any one condition is False, result will be False.

print((12 == 12) and (56 != 77))     # output : True
print((43 < 45) and False)           # output : False

#.... 2) or....
# The or operator gives True if at least one condition is True.
# It only gives False when both conditions are False.

print((22 >= 25) or (34 != 55))      # output : True
print((10 != 10) or False)           # output : False


#.... 3) not....
# If something is True, not will make it False
# If something is False, not will make it True

x = True
print(x)     # Output: True

x = True
print(not x)   # Output: False

y = False
print(not y)   # Output: True


"""............. Conditional Statement ............"""

#....1) If and Else....
# if → used to check a condition (first condition)
# else → runs when the if condition is False


# age = int(input("Please Tell Your Age : "))

# if age >= 18: 
#     print("Yes you can vote")

# else: 
#     print("sorry you cannot vote")

#.....Output.....

# Please Tell Your Age : 12
# sorry you cannot vote


#....Ternary Operator....
# print("vote") if age >= 18 else print("not vote")


#....2) Elif....
# if → first condition
# elif → check next conditions
# else → when all conditions are false

num = -4

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#.....Output.....

#Negative number