# Question: write a python code to list and demonstrate various standard library module of python.

import os
import sys
import datetime
import json
import math

print("--- Demonstration of Essential Standard Library Modules ---")
print("-" * 50)

# 1. os Module (Operating System Interfaces)
# The 'os' module provides functions for interacting with the operating system.
print("\n[1. os Module Demonstration (File/Directory Interaction)]")
try:
    # Get the current working directory where the script is being run
    current_dir = os.getcwd()
    print(f"Current working directory (os.getcwd()): {current_dir}")
    
    # Check if a specific file or directory exists
    file_status = os.path.exists("standard_modules_demo.py")
    print(f"Does this script file exist (os.path.exists)? {file_status}")
except Exception as e:
    print(f"Error demonstrating os module: {e}")

print("-" * 50)


# 2. sys Module (System-Specific Parameters and Functions)
# The 'sys' module allows you to interact with the Python interpreter itself.
print("\n[2. sys Module Demonstration (Interpreter Information)]")
# Show the version of the Python interpreter being used
print(f"Python Version (sys.version): {sys.version.split()[0]}")

# Show the command line arguments passed to the script (the script name itself is the first argument)
print(f"Script Name (sys.argv[0]): {sys.argv[0]}")

print("-" * 50)


# 3. datetime Module (Date and Time Operations)
# Used for manipulating dates and times.
print("\n[3. datetime Module Demonstration (Current Time)]")
# Get the current date and time
now = datetime.datetime.now()
print(f"Current Date and Time (datetime.datetime.now()): {now}")

# Get just the current date
today = datetime.date.today()
print(f"Today's Date (datetime.date.today()): {today}")

print("-" * 50)


# 4. json Module (JavaScript Object Notation)
# Used for working with JSON data, which is common for web APIs and configuration.
print("\n[4. json Module Demonstration (Data Serialization)]")
# A simple Python dictionary (Object)
data_to_serialize = {
    "name": "User 1",
    "score": 95,
    "is_active": True
}
print(f"Original Python Data (Dictionary): {data_to_serialize}")

# Convert the Python dictionary into a JSON formatted string (Serialization)
json_string = json.dumps(data_to_serialize, indent=4)
print("\nSerialized JSON String (json.dumps):")
print(json_string)

print("-" * 50)


# 5. math Module (Mathematical Functions and Constants)
# Provides access to common mathematical functions.
print("\n[5. math Module Demonstration (Calculations)]")
# Use the math.pi constant and the math.pow (power) function
radius = 4
area = math.pi * math.pow(radius, 2)
print(f"Area of circle (radius 4) using math.pi and math.pow: {area:.2f}")

# Use the math.ceil (ceiling) and math.floor function
number = 12.7
print(f"math.ceil(12.7): {math.ceil(number)}")
print(f"math.floor(12.7): {math.floor(number)}")

print("-" * 50)


# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
