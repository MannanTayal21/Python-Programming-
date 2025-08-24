print("Demonstration of List Comprehension:")
# Example 1: List of squares from 0 to 9
squares = [x*x for x in range(10)]
print("Squares:", squares)

# Example 2: List of even numbers from 0 to 20
evens = [x for x in range(21) if x % 2 == 0]
print("Even numbers:", evens)

# Example 3: Change words to uppercase
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]
print("Uppercase words:", upper_words)

print("\nThis program is written and executed by Mannan Tayal (0231BCA047)")
