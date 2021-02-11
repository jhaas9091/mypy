"""Module #5 Assignment
Julie Haas
LIS 5937
Spring 2021"""

"1. Write a Python program to execute a string containing Python code"
def addyears(name, age):
    age += 10
    print(name + " will be " + str(age) + " in 10 years.")


addyears(name="Anna", age=14)





"2. Write a Python function to insert a string in the middle of a string"

"Function was defined assuming input string would not need to change from 'The weather is __ today'."
def weatherrep(str,weather):
    return str[:14] + " " + weather + " " + str[-5:]

print (weatherrep("The weather is __ today",'Cloudy'))
print (weatherrep("The weather is __ today",'Sunny'))
