# Question: Write python code to demonstrate decorator with argument.

# --- 1. THE RULE-SETTER (Takes the decorator argument) ---
def log_message(prefix):
    """
    A factory function that creates a decorator.
    'prefix' is the argument we want the decorator to use later.
    """
    
    # --- 2. THE DECORATOR (Takes the function to be decorated) ---
    def actual_decorator(func):
        
        # --- 3. THE RUNNER (The function that replaces the original function) ---
        def wrapper(*args, **kwargs):
            # This is the new, custom behavior
            print(f"[{prefix}]: Preparing to run {func.__name__}...")
            
            # Now, run the original function
            result = func(*args, **kwargs)
            
            # Print the result and the prefix again
            print(f"[{prefix}]: Done. Result was: {result}")
            return result
        
        return wrapper
        
    return actual_decorator

# --- USING THE DECORATOR ---

# We use @log_message('ALERT') to set the 'prefix' argument to 'ALERT'
@log_message('ALERT')
def launch_sequence(count):
    """A simple function that prints a countdown."""
    print(f"   Launch countdown starting from {count}...")
    while count > 0:
        count -= 1
    return "Liftoff!"

# We use @log_message('INFO') to set the 'prefix' argument to 'INFO'
@log_message('INFO')
def check_status():
    """A simple function that just returns a status."""
    return "All systems nominal."


# --- EXECUTION ---

# When we call this, the 'ALERT' prefix is automatically added to the output.
print("--- Launch Sequence Test ---")
launch_sequence(3)

print("\n--- Status Check Test ---")
# When we call this, the 'INFO' prefix is automatically added to the output.
check_status()


# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
