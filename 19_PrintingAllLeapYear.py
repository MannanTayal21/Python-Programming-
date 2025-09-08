# Function to check for leap year
def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

# List to store leap years
leap_years = []

# Loop from year 1 to 2025
for year in range(1, 2026):
    if is_leap_year(year):
        leap_years.append(year)

# Print all leap years
print("Leap Years from 1 to 2025:")
print(leap_years)

# Print the total count
print("\nTotal number of leap years:", len(leap_years))

print("This program is written and executed by Mannan Tayal (0231BCA047)")
