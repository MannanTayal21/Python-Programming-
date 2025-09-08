print("Demonstration of Try and Except and Else and Finally:")
# Demonstration of try, except, else, and finally

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")
else:
    print("Division successful. Result is:", result)
finally:
    print("This is the finally block. It always runs.")

print("This program is written and executed by Mannan Tayal (0231BCA047)")
