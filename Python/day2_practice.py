"""For-loop Practice Set"""

#.....1) Print Hello World n times. .....
"""
    use a loop to repeate a print statement("Hello World")
    based on user input count n.
"""

# n = int(input("tell your number to print hello world : "))
# for i in range(n): 
#     print("Hello World")


#.....2) Print the number from 1 to n. .....
"""
    Display number in increasing order from 1 up to give number n.
"""

# n = int(input("Tell Your Number : "))
# for i in range(1, n + 1): 
#     print(i)


#.....3) Print the number from n to 1 .....
"""
    Display number in decreasing order from n down to 1.
"""

# n = int(input("tell your number : "))
# for i in range(n, 0, -1): 
#     print(i)


#.....4) sum of natural number (1 to n) .....
"""
    take input n and caculate the total sum from 1 to n.
"""

# n = int(input("tell your number : "))
# total = 0
# for i in range(1, n+1): 
#     total += i
# print(total)

#.....5) Factorial of a number .....
"""
    calculate the factorial (n!) using a loop 
    multiplying number from 1 to n.
"""

# n = int(input("tell your number : "))
# fact = 1
# for i in range(1, n+1): 
#     fact *= i
# print(fact)


#.....6) Sum of Even and Odd Numbers in Range. .....
"""
    from 1 to n. find and print the sum of all even and 
    all odd numbers separately.
"""

# n = int(input("tell your number : "))
# even = 0
# odd = 0

# for i in range(1,n+1): 
#     if i % 2 == 0: 
#         even += i
#     else: 
#         odd += i
# print(f"The sum of odd numbers are {odd}")
# print(f"The sum of even numbers are {even}")


#.....7) Print All Factor's of a Number.....
"""
    Display all numbers that divide the input number exactly (no remainder).
"""

# n = int(input("tell the number : "))

# print(f"....All factor's of {n} are....")
# for i in range(1, n+1): 
#     if n % i == 0: 
#         print(i)


#.....8) Sum of All Factor's.....
"""
    Add up all the factors found in the previous question 
    (excluding or including the number itself -- your choice).
"""

# n = int(input("tell your number : "))
# total = 0
# for i in range(1, n+1): 
#     if n % i == 0: 
#         total += i
# print(f"Sum of all the factors of {n} are {total}")


#.....9) Power Calculation (a^b).....
"""
    Input base a and exponent b, and calculating the result using a loop
    without using (**).
"""

# a = int(input("tell the value : "))
# b = int(input("tell the exponent : "))

# power = 1
# for i in range(b): 
#     power = power * a
# print(f"After power your answer is {power}")


#.....10) Print Number Check.....
"""
    Accept a number and check if it is divisible only by 1 
    and itself (i.e., prime or not)
"""

""" #....way 1...""" 

# n = int(input("give your number (Prime check) : "))
# count = 0
# for i in range(1, n + 1): 
#     if n % i == 0: 
#         count += 1
# if count == 1: 
#     print("Your number is unity number") 
# elif count == 2: 
#     print("Your number is prime number")
# else: 
#     print("your number is composite number")


""" #....way 2...""" 

n = int(input("give your number (prime check) : "))

for i in range(2,n): 
    if n % i == 0: 
        print("Sorry your number is composite")
        break 
else: 
    print("Your number is prime")



    """while-loop Practice Set"""

#.....1) Print Each Digit (Revese Order).....
"""
    Break a number into individual digits and 
    print them starting from the last digit.
"""

# num = int(input("Tell your number : "))

# while num > 0: 
#     digit = num % 10
#     print(digit)
#     num = num // 10


#.....2) Sum of Digits.....
"""
    Add all the digits of a number 
    (e.g., 123 :- 1 + 2 + 3 = 6).
"""

# num = int(input("tell Your Number : "))
# total = 0
# while num > 0: 
#     total = total + num % 10
#     num = num // 10

# print("Your digit Sum is ", total)


#.....3) Reverse a number .....
"""
    input a number and reverses its digit
    (e.g., 123 = 321).
"""

# num = int(input("tell your number : "))
# rev = 0
# while num > 0: 
#     rev = rev * 10 + (num % 10)
#     num = num // 10

# print(f"Your Reversed number is {rev}")


#.....4) Palindrome number check .....
"""
    check if a number reads the same forward and backward
    (e., 121, 1331)
"""

# num = int(input("tell your number : "))
# copy = num
# digit = 0
# while num > 0: 
#     digit = digit * 10 + (num % 10)
#     num = num // 10

# if copy == digit: 
#     print("Your number is palindrome number")

# else: 
#     print("Your number is not palindrome number")


#.....5) Automorphic Number .....
"""
    a number is a automorphic if its square ends with the number
    itself(e.g., 5=25, 76=5776) check and print result.
"""

num = int(input("tell your number : "))
copy = num
square = num ** 2

count = 0
while num > 0: 
    count = count + 1
    num = num // 10

extract = square % (10**count)
if extract == copy: 
    print("Your number is automorphic")
else: 
    print("Your number is not automorphic")