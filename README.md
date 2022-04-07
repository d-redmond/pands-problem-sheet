# pands-problem-sheet

Please find below a brief description of each weekly task and the resources I found helpful in completing them.

# week02_bmiCalculator

Objective: Calculate the BMI of a person by using Python.

The user is prompted to input their height and weight. A function is created to calculate the user's BMI with the parameters of height and weight. The result will be returned as a float.

https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g


# week03_secondString.py  

Objective: A program that requests the user input a string and  then outputs every second letter in reverse order.

The user prompted to input a string. This input is then assigned to a variable. A splice operator is used to print every second letter of the string in reverse order. 

https://www.w3schools.com/python/python_strings_slicing.asp

https://www.reddit.com/r/Python/comments/r8hb5n/7_proven_methods_to_reverse_the_python_string_in/

https://github.com/g00387822/reverse_string_every_second_letter

# week04_collatz.py

Objective: A program that asks the user to input any positive integer, and outputs the successive values of the following calculation. At each step the next value is calculated by taking the current value,
And if it is even divide it by two, if it is odd, multiply by three and add one. The program ends if the current value is one.

The collatz function is declared, and the user is prompted to input a whole positive number. A while/if/else loop is then used to check conditions. If the given number is not equal to 1, the program moves on to the if statement. If the given number is even it will be divided by 2 until it returns 1. If the given number is uneven, the else block is executed and the number is multiplied by 3 and 1 is added to the result. The loop ends when it returns 1. 

https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer

https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

https://www.tutorialspoint.com/collatz-sequence-in-python

# week05_weekDay.py

Objective: A program that outputs differently depending on whether today is a weekday.

I imported the datetime module and date class. The date function is then assigned to the variable day. An if/else statement is used to categorize days of the week into weekdays and weekend days. If the variable day outputs a number less then 6, a statement is printed confirming it is a weekday. Otherwise a statement is printed confirming it is a weekend day.

https://poopcode.com/check-day-weekday-weekend-python/

https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

https://www.w3schools.com/python/python_datetime.asp

# week06_squareRoot.py

Objective: A Program that takes a positive floating point number as an input and outputs an approximation of it's square root.

The function sqrt is created. The user is prompted to input a number and sqrt will return the approximate square root of this number. The number input must not be less than 0. A margin of error is specified within the function. In a while loop, Newton's Method is used to ensure that the resulting square root falls within the specified margin of error. An if statement is then used to end the loop once the resulting square root falls within the margin of error. The most accurate square root will then be printed.   

https://realpython.com/python-square-root-function/

https://en.wikipedia.org/wiki/Newton%27s_method

https://math.stackexchange.com/questions/3524205/square-roots-by-newton-s-method

https://www.reddit.com/r/learnpython/comments/lywigx/i_wrote_this_square_root_algorithm_but_its_not/

https://stackoverflow.com/questions/3581528/how-is-the-square-root-function-implemented

# week07_letterFrequency.py

Objective: A program that reads in a text file and outputs the number of e's it contains.

https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/

https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

# week08_plotTask.py

Objective: A program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

I imported the Numpy, Matplotlib, pyplot, and lines modules. I created an array with Numpy and specified the range of points that would be displayed on the graph. The squared and cubed functions were declared. The plot function was used to plot the various points. I also styled each of the lines on the graph in such a way that they have a distinct appearence using pyplot. A simple legend was also added via the legend function. Title attributes were styled via a dictionary, which was then used as a parameter in the title function. Finally each line was appropriately labelled.      

https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm

https://towardsdatascience.com/a-quick-review-of-numpy-and-matplotlib-48f455db383

https://matplotlib.org/3.5.0/tutorials/introductory/pyplot.html

https://www.youtube.com/watch?v=3GWx9QepQEY

https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/text_fontdict.html

https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html

