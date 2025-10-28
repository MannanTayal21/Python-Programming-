# Question: Write python code to use a module.

# 1. Import the module. This makes all the tools inside 'random' available.
import random 

print("--- Demonstrating the 'random' Module ---")

# --- Example 1: Generate a random integer ---
# We call the 'randint' function inside the 'random' module.
# This picks a random whole number between 1 (inclusive) and 100 (inclusive).
random_number = random.randint(1, 100)
print(f"I picked a random number between 1 and 100: {random_number}")

# --- Example 2: Pick a random item from a list ---
my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# We use the 'choice' function to pick one item randomly.
random_fruit = random.choice(my_list)
print(f"I picked a random fruit from the list: {random_fruit}")

# --- Example 3: Shuffle a list ---
# We use the 'shuffle' function to mix the order of the list IN PLACE.
random.shuffle(my_list)
print(f"I shuffled the list (new order): {my_list}")

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)