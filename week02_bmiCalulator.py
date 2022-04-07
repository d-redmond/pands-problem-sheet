# week02_bmiCalculator.py

# Objective: A program that calculates a person's Body Mass Index (BMI)
# Author: Denise Redmond

# The input function requests the user input their height cm) and weight (kg)
# The float function converts the user's input to a float type
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# The BMI formula assigned to variable BMI: weight divided by height squared
BMI = weight / (height/100)**2

# The round function rounds the BMI result to two decimal
BMI = round(BMI, 2)

# The print function prints the string "Your BMI is " and the BMI calculation
print ("Your BMI is " + str(BMI))