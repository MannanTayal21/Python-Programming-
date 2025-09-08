from datetime import datetime

dob = input("Enter your birthdate (DD-MM-YYYY): ")
given_date = input("Enter date to check age on (DD-MM-YYYY): ")

dob = datetime.strptime(dob, "%d-%m-%Y")
given = datetime.strptime(given_date, "%d-%m-%Y")

age = given.year - dob.year

# Adjust if birthday not reached yet in the given year
if (given.month, given.day) < (dob.month, dob.day):
    age -= 1

print(f"Your age on {given_date} is: {age} years.")
print("This program is written and executed by Mannan Tayal (0231BCA047).")
