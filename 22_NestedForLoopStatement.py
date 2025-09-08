# Demonstration of nested for loop - Printing a 3x3 multiplication table
print("Demonstration of nested for loop (Multiplication Table 1 to 3):")

for i in range(1, 4):  # Outer loop (rows)
    for j in range(1, 4):  # Inner loop (columns)
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # Newline after each row

# Signature line
print("\nThis program is written and executed by Mannan Tayal (0231BCA047)")
