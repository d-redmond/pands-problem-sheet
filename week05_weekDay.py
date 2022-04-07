# week05_weekDay.py

# Objective: A program that outputs whether or not today is a weekday
# Author: Denise Redmond

# Importing the date class from the datetime module
from datetime import date

# Datetime syntax: datetime.date.today().weekday()
day = date.today().weekday()

# # Mon-Fri is equal to 1-5
# If day of week is less than 5 output that it is a weekday
# Else print that it is a weekend
if day < 6:
    print ("Unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")