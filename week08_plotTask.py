# week08_plotTask.py

# Objective: A program called plottask.py that displays a plot of the functions below
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
# Author: Denise Redmond

# Import numpy module for arrays
# Import matplotlib, pyplot, and lines modules for data plotting capabilities
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# An array is created for the given range
xpoints = np.array(range(0, 4))

# Equations for the squared and cubed functions
x2 = xpoints * xpoints 
x3 = xpoints * xpoints * xpoints 

# Matplotlib used to style the lines on graph
# Each linestyle a distinct style and labelled appropriately
plt.plot(x2, linestyle = "solid", color = "red", label = "x2")
plt.plot(x3, linestyle = "dotted", color = "blue", label = "x3")

# Legend added
plt.legend()

# Title created via plt.title
# Title styled via dictionary 
titleFont = {'family': 'arial',
        'color':  'black',
        'weight': 'bold',
        'size': 16,
        }
plt.title("Plot of Functions", fontdict=titleFont)

# Each axis labelled appropriately
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.show()