# Function to check if a number is perfect
def is_perfect_number(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n

# List to store perfect numbers
perfect_numbers = []

# Check numbers from 1 to 2025
for num in range(1, 2026):
    if is_perfect_number(num):
        perfect_numbers.append(num)

# Print the perfect numbers
print("Perfect numbers from 1 to 2025:")
print(perfect_numbers)

# Print the total count
print("\nTotal number of perfect numbers:", len(perfect_numbers))

# Signature line
print("\nThis program is written and executed by Mannan Tayal (0231BCA047)")
