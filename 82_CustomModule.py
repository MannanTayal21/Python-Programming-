# This is our custom module file. It contains functions we want to reuse.

def simple_add(num1, num2):
    """Adds two numbers."""
    return num1 + num2

def simple_multiply(num1, num2):
    """Multiplies two numbers."""
    return num1 * num2

# If you were to run this file directly, this block of code would execute.
if __name__ == "__main__":
    print("This is the math_helpers module running directly.")
    print(f"2 + 3 = {simple_add(2, 3)}")
# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
