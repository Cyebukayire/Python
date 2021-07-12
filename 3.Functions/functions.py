def greet_user(amazina):
    print("Hi "+ amazina +", Welcome to our system")

def greet_users(first_name, last_name):
    print("hello "+ first_name +" "+ last_name)


print ("Start")

name1 = "Shallom"
name2 = "Shami"
# using positional arguments
greet_user(name1)

# Calling a function using "Keyword arguments" For code readability
greet_user(amazina= name2)

# You can not use keyword arguments first
# greet_users(first_name="Peace", "Hanson") #Gives an error
greet_users("Peace", last_name="Hanson")

print("Finish")

""" 
PARAMETERS VS ARGUMENTS

Arguments are values we pass to functions to be executed while
Parameters are variables that hold the arguments/values we pass to functions

Arugemnts are defined while calling the funtion while 
parameters are defined while creating the function
"""