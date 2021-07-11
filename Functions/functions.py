def greet_user(amazina):
    print("Hi "+ amazina +", Welcome to our system")

print ("Start")
name1 = "Shallom"
name2 = "Shami"
# using positional arguments
greet_user(name1)

# Calling a function using "Keyword arguments" For code readability
greet_user(amazina= name2)
print("Finish")

""" 
PARAMETERS VS ARGUMENTS

Arguments are values we pass to functions for be executed while
Parameters are variables that hold the arguments/values we pass to functions

Arugemnts are defined while calling the funtion while 
parameters are defined while creating the function
"""