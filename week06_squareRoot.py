# week06_squareRoot.py

# Objective: A Program that takes a positive floating point number as an input
# and outputs an approximation of it's square root
# Author: Denise Redmond

# Defining a function called sqrt that takes num as input 
# and returns the square root of num
# Requests user input number that must not be less than 0
def sqrt(num):
    x = num
    marginError = 0.00001
    sqRoot = 0
    while True:
        # Calculates estimated square root of num
        # Result checked whether within margin of error
        # Loop repeats until estimated square root within margin of error
        # Newton's Method: 0.5 * (x + (num / x))
        sqRoot = 0.5 * (x + (num / x))
        if abs(sqRoot - x) < marginError:
            # Loop broken if estimated square root within margin of error
            break
        x = sqRoot
    return sqRoot

# Converts requested input to float
# Input less than 0 invalid
# Otherwise returns square root of n
n = float(input("Please enter a positive number for the square root: "))
if n <= 0:
    print("Invalid input. The inut must be a positive number")
else:
    print("The square root of",n,"is",round(sqrt(n),2))