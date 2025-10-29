# Question: write a python code to demonstrate method overloading and method overriding.

# --- 1. Basic Item Class (The Original Blueprint) ---
class BasicItem:
    def __init__(self, name):
        self.name = name

    # A. Method Overriding Target: Simple damage value
    def get_value(self):
        """The default, simple value."""
        return 10

    # B. Pythonic Overload Demo: Flexible function with an optional argument
    def inspect(self, show_detail=False):
        """A single function that acts differently based on the input."""
        if show_detail:
            # Case 1 (Detailed check)
            print(f"[{self.name}]: Detailed inspection complete. Value is {self.get_value()}.")
        else:
            # Case 2 (Quick check)
            print(f"[{self.name}]: Quick check passed.")

# --- 2. Upgraded Item Class (Inherits and Overrides) ---
class UpgradedItem(BasicItem):
    # A. Method Overriding: We replace the parent's 'get_value'
    def get_value(self):
        """This OVERRIDES the BasicItem method with a higher value."""
        return 50 # New value is much higher!

# --- Demonstration ---
print("--- Overriding Demo ---")
original = BasicItem("Simple Tool")
upgrade = UpgradedItem("Master Tool")

# The upgrade object uses the NEW 'get_value' (Overriding)
print(f"The Simple Tool value is: {original.get_value()}")
print(f"The Master Tool value is: {upgrade.get_value()} (This is the overridden value!)")


print("\n--- 'Overloading' Demo (Function Flexibility) ---")
# This is the same function, but it handles different inputs (Flexibility)
upgrade.inspect()             # Calling with one argument (Basic)
upgrade.inspect(show_detail=True) # Calling with two arguments (Detailed)

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
