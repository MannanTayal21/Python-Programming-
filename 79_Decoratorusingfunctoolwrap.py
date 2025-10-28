# Question: Write python code to demonstrate decorator using function tool wraps.

from functools import wraps

# --- The Decorator with the "Sticky Note" (@wraps) ---
def add_excitement(func):
    """This decorator adds some excitement before running a function."""
    
    # We use @wraps(func) to copy the original function's details 
    # (name, docstring) onto this new wrapper function.
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("📢 Woohoo! Getting ready to run...")
        result = func(*args, **kwargs)
        print("🎉 Finished!")
        return result
    return wrapper

# --- The function we are decorating ---
@add_excitement
def print_homework_done(topic):
    """
    This is the original function. 
    Its name is 'print_homework_done' and this is its docstring.
    """
    return f"Homework on '{topic}' is complete!"

# --- The test ---

# 1. Run the decorated function
message = print_homework_done("Decorators")
print(f"\nFinal Message: {message}")

# 2. Check the details (name and instructions)
print("\n--- Checking the Function's Identity ---")

# Because we used @wraps, the function acts like its true self!
print(f"Function Name (Should be original): {print_homework_done.__name__}")
print(f"Function Instructions (Docstring): {print_homework_done.__doc__}")


# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
