# Question: write python code to demonstrate decorator

import time

# --- 1. THE DECORATOR FUNCTION ---
def timer_decorator(func):
    """
    A simple decorator that measures and prints the execution time 
    of the function it wraps.
    """
    def wrapper(*args, **kwargs):
        # Start timer
        start_time = time.time()
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # End timer and calculate duration
        end_time = time.time()
        duration = end_time - start_time
        
        # Print the result of the timing
        print(f"\n[TIMER]: Function '{func.__name__}' ran in {duration:.4f} seconds.")
        
        # Return the original function's result
        return result
    
    # The decorator returns the wrapper function
    return wrapper

# --- 2. USING THE DECORATOR ---

# By placing @timer_decorator above the function, we are telling Python:
# "Instead of defining 'simulate_task', replace it with timer_decorator(simulate_task)."
@timer_decorator
def simulate_task(seconds):
    """A function that just pauses for a given number of seconds."""
    print(f"Starting task that will take {seconds} seconds...")
    time.sleep(seconds) # Pause execution
    print("Task finished.")
    return f"Task completed successfully after {seconds}s."

# --- 3. EXECUTION ---

# Call the function. It now has the added "timing" logic from the decorator.
task_result = simulate_task(2)

# Print the return value of the function
print(f"Function return value: {task_result}")


# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
