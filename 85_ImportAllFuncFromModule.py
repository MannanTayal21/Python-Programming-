# Question: Write python code to import all function from a module.

# Using the '*' (wildcard) tells Python to import every function, variable, and class 
# defined within the 'math' module directly into our current program's namespace.
from math import * print("--- Demonstrating Wildcard Import (from module import *) ---")

# When using 'import *', we can call functions and constants directly, without 
# having to write the 'math.' prefix first.

# 1. Use the 'pi' constant to find circumference (2 * pi * radius)
radius = 7
circumference = 2 * pi * radius
print(f"Circumference of a circle with radius {radius}: {circumference:.2f}")

# 2. Use the 'sqrt' (square root) function
value = 100
root = sqrt(value)
print(f"The square root of {value} is: {root}")

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
