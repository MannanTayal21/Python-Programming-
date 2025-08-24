print("Demonstration of Try and Except:")
# Demonstration of try and except

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")

print("\nThis program is written and executed by Mannan Tayal (0231BCA047)")
