# week03_secondString.py

# Objective: A program that requests the user input a string and  then outputs every second letter in reverse order
# Author: Denise Redmond

# Requests the user input a string and the input is assigned to the variable String
string = input ("Please enter string: ")

# Prints every second letter of the input string in reverse order
# Splice operator syntax = [start:finish:step size & direction]
print(string[::-2])