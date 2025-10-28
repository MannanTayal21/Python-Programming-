# Question: Write python code to import specific function of a module.

# We use the 'from module_name import function_name' syntax.
# This allows us to use 'sqrt' and 'pi' directly without having to write 'math.sqrt'
from math import sqrt, pi 
from random import randint 

print("--- Using Specific Functions from Modules ---")

# 1. Using sqrt (from the math module)
number = 49
# Notice we just use 'sqrt()' directly, not 'math.sqrt()'
root = sqrt(number)
print(f"The square root of {number} is: {root}")

# 2. Using pi (from the math module)
radius = 5.0
# Calculate the area of a circle: pi * r^2
area = pi * radius**2
print(f"The area of a circle with radius {radius} is: {area:.2f}")

# 3. Using randint (from the random module)
# We can import multiple functions from multiple modules this way.
dice_roll = randint(1, 6)
print(f"A single dice roll gave us: {dice_roll}")

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)