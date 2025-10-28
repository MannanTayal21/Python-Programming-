# Question: write a python code to demonstrate docstring for a function

def calculate_area_of_square(side_length):
    """
    Calculates the area of a square given the length of one side.

    This function accepts a single numerical argument, which represents 
    the side length of a square, and returns its area (side * side).

    Args:
        side_length (int or float): The length of one side of the square.

    Returns:
        int or float: The calculated area of the square.

    Example:
        >>> calculate_area_of_square(5)
        25
    """
    # Simple calculation: Area = side * side
    area = side_length * side_length
    return area

# --- Demonstration ---

# 1. Calling the function to see the result
result = calculate_area_of_square(7)
print(f"The area of a square with side 7 is: {result}")

# 2. Accessing and printing the docstring using the .__doc__ attribute
print("\n--- Function Documentation (Docstring) ---")
print(calculate_area_of_square.__doc__)

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
