"""......Loops......"""
# when we want to perform repetitive task we use loops.
# ...types of loops: 
# 1) for loop 
# 2) while loop


"""....1) for loop...."""
#      - used when we know the number of repetitions in advance. 
#      - controlled by sequence / range.
#      - range function (start, stop, steps)

#....example :-
# for i in range(1,6,1): 
#     print(i)

#....output....
# 1
# 2
# 3
# 4
# 5

""".... for loop on string ...."""
# string is a sequence of characteers.

#....example :-
# word = "PYTHON"
# for i in word: 
#     print(i)

#....output....
# P
# Y
# T
# H
# O
# N


""".... for loop with index (using len() and range() )...."""

#....example :-

name = "ANKUSH"
for i in range(len(name)): 
    print(i, name[i])

#....output....
#   0 A
#   1 N
#   2 K
#   3 U
#   4 S
#   5 H



"""....2) while loop...."""
#         - works on the basis of condition
#         - this loop will stop when the 
#           codition becomes false.
#         - used when the number of iterations 
#            is not known in advance.



#.....example......

# n = int(input("Enter number: "))
# total = 0
# i = 1

# while i <= n:
#     total += i
#     i += 1

# print("Sum =", total)

#.....output......
# Enter number: 5
# Sum = 15


"""....While with else...."""
#       - else block runs when the loop condition
#         becomes False (not broken manually).

#.....example......

# i = 1
# while i <= 3:
#     print(i)
#     i += 1
# else:
#     print("Loop finished successfully")

#.....output......
# 1
# 2
# 3
# Loop finished successfully


"""....Breaking a While Loop...."""

# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

#.....output......
# 1
# 2
# 3
# 4

# break stops the loop immediately when i == 5.


"""....Using continue in While Loop...."""

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

#.....output......
# 1
# 2
# 4
# 5