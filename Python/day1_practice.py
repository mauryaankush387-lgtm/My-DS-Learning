"""If-Else Practice Set"""


#.....1) Compare Two Numbers.....
"""
    take two users inputs and determine which number is greater
    - or if they're equal.
"""

# num1 = float(input("Tell Your First Number : "))
# num2 = float(input("Tell Your Second Number : "))

# if num1 > num2: 
#     print(f"{num1} is greater than {num2}")

# elif num2 > num1: 
#     print(f"{num2} is greater than {num1}")

# else: 
#     print(f"{num1} is equal to {num2}")


#.....2) Greet by Gender (m/f).....
"""
    accept a gender input ('m' or 'f') and print greeting
    like "Hello Sir", "Hello Mam".
"""

# gen = input("Tell Your geneder in character ('m' or 'f') : ")

# if gen == 'm': 
#     print("Hello Sir")
# else: 
#     print("Hello Mam") 


#.....3) Gender with Case Handling.....
"""
    make the gender check case-insensetive ('M','F','m','f' all valid).
    if input is invalid, print("Wrong input").
"""

# gen = input("Please Tell Your Gender in character ('M','F','m','f') : ")

# if gen == 'M' or gen == 'm': 
#     print("Hello Sir, how are you?")

# elif gen == 'F' or gen == 'f': 
#     print("Hello Mam, how are you?")

# else: 
#     print("Wrong input only provide m or f ")


#.....4) Even or Odd checker.....
"""
    accept a number from the user and check whether 
    it's even or odd using modulo (%)
"""

# num = int(input("Please Tell Your Number : "))

# if num % 2 == 0: 
#     print("Your Number Is Even")
# else: 
#     print("Your Number Is Odd")


#.....5) Voting Eligibility.....
"""
    input name and age. if age >= 18, print "Eligible to vote",
    if not, print how many year's are left to become eligible.
"""

# name = input("Please Tell Your Name : ")
# age = int(input("Please Tell Your Age : "))

# if age >= 18: 
#     print(f"Hello {name} you can vote")

# else: 
#     print(f"Hello {name}, sorry you can vote after {18 - age} years")


#.....6) Day Number To Day Name.....
"""
    take an integer (1-7) and print the corresponding weekday
    (1=Monday, 2=Tuesday,..,7=Sunday). Handle invalid input too.
"""

# num = int(input("Please Tell Your Day (1-7) : "))

# if num == 1: 
#     print("Monday it is")
# elif num == 2: 
#     print("Tuesday it is")
# elif num == 3: 
#     print("Wednesday it is")
# elif num == 4: 
#     print("Thursday it is")
# elif num == 5: 
#     print("Friday it is")
# elif num == 6: 
#     print("Saturday it is")
# elif num == 7: 
#     print("Sunday it is")
# else: 
#     print("invalid input, please enter day between (1-7)")


#.....7) Greatest of three numbers.....
"""
    accept three numbers and find the greatest one among
    them using nested (if-else). aslo find if 2 are equal,
    also find if all are equal.
"""

# a = float(input("Tell your first number : "))
# b = float(input("Tell Your second number : "))
# c = float(input("Tell Your third number : "))

# if a == b and b == c: 
#     print(f"all the numbers are equal")
# elif a == b or b == c or c == a: 
#     print(f"any two numbers are equal")
# elif a > b and a > c: 
#     print(f"{a} is the greatest number")
# elif b > c and b > c: 
#     print(f"{b} is the greatest number")
# else:
#     print(f"{c} is the greatest number")


#.....8) Leap Year Checker.....
"""
    input a year and check if it's a leap year using proper rules: 
    divide by 4, not by 100 unless divide by 400
"""

# year = int(input("please tell your year : "))

# if year % 100 == 0 and year % 400 == 0:
#     print("it's a leap year")
# elif year % 100 != 0 and year % 4 == 0: 
#     print("it's a leap year")
# else: 
#     print("sorry it's not a leap year")


#.....9) Shop Discount Calculator.....
"""
    ask for a purchase amount. Apply discounts based on thresholds:
    e.g.,above 1000 --> 10% off, above 5000 --> 20% off. print final bill
    (you can also design a shop-like interface later.)
"""

# bill = int(input("tell your total amount : "))

# if bill >= 1000 and bill < 5000: 
#     final_bill = (bill * 90) / 100
#     print(f"You Got a discount of 10% your final amount is : {final_bill}")

# elif bill >= 5000: 
#     final_bill = (bill * 80) / 100
#     print(f"You Got a discount of 20% your final amount is : {final_bill}")

# else: 
#     print(f"sorry no discount for you")



#.....9) Vowel and Consonant.....
"""
    accept a single alphabet character. and check if it's a vowel ('a', 'e', 'i', 'o', 'u')
    or (consonant). Also, handle invalid characters.
"""

# char = input("Tell Your Alphabet : ")

# if len(char) > 1: 
#     print("please enter only one Alphabet")

# else: 
#     if char in "aeiouAEIOU": 
#         print("It's a vowel")
#     else: 
#         print("it's a consonant")