"""....Function...."""

# def hello():        #defining the function using (def) keyword
#     print("Hello, How Are You")

# hello()     # this is the calling the function
# hello()     # this is the calling the function
# hello()     # this is the calling the function


"""....print vs return in functions...."""

#....1) using return :
 
# def Hello():
#     return "Hello, how are you?"

# Hello()       # No output
# print(Hello())  # Output visible


#....2) using print function : 

# def Hello():
#     print("Hello, how are you?")

# Hello()      # Output visible immediately


"""....parameters and arguments...."""

# def greet(name):   # name = parameter
#     print("Hello", name)

# greet("Ankush")  # "Ankush" = argument


#....Keyword Argument....
#       - You pass the value using the parameter name.

# def student(name, age):
#     print(name, age)

# student(age=22, name="Ankush")  # arguments passed using parameter names


#....Default Parameters (Default Arguments)....
#       - Parameters that have a default value.
#       - If the caller does NOT pass value → default value is used.

def welcome(name="Guest"):
    print("Welcome", name)

welcome()             # uses default → Guest
welcome("Ankush") # overrides default → Ankush