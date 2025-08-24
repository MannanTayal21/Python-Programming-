print("Demonstration of Try and Except and Finally:")
# Demonstration of try, except, and finally

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")
finally:
    print("This block always runs (finally block).")

print("This program is written and executed by Mannan Tayal (0231BCA047)")
