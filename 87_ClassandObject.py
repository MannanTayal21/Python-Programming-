# Question: write a python code to define a class, create its objects, and access the properties in methods of the objects.

# 1. Define the Class (The Blueprint for a Pet)
class Pet:
    # This is the setup step for every new Pet.
    def __init__(self, name, species):
        # Set the Pet's properties (like name and species).
        self.name = name
        self.species = species

    # 2. Define a Method (An action the Pet can do)
    def introduce(self):
        # The method accesses the Pet's own properties using 'self.'
        print(f"Hi! My name is {self.name}, and I am a {self.species}.")

# --- Creating Objects (Making the actual Pets) ---

# Create Object 1
my_cat = Pet("Whiskers", "Cat")

# Create Object 2
my_dog = Pet("Buddy", "Dog")

# --- Accessing the Method (Telling the Pets to act) ---
print("--- Introducing the Pets ---")
my_cat.introduce()
my_dog.introduce()

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
