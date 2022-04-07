# week04_collatz.py

# Objective: A program that asks the user to input any positive integer, 
# and outputs the successive values of the following calculation.
# At each step the next value is calculated by taking the current value,
# And if it is even divide it by two, 
# if it is odd, multiply by three and add one.
# The program ends if the current value is one.
# Author: Denise Redmond

# Defining the function collatz()
def collatz():
    
    # The user is asked to input a positive integer
    # The input is printed and ends with an empty string
    num = int(input("Please enter a whole positive number: "))
    print(num, end = ' ')

    # While the number is not equal to 1
    # If number is even divide by two until you reach number one
    # If result is not even, the number is multiplied by three and one added to it
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        print (num, end = ' ')

# Calling collatz function
collatz()