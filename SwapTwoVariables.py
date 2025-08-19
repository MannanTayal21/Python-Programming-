# Swap using temp variable
a, b = 10, 20
temp = a
a = b
b = temp
print("Temp variable:", a, b)

# Swap using arithmetic
a, b = 10, 20
a = a + b
b = a - b
a = a - b
print("Arithmetic:", a, b)

# Swap using tuple
a, b = 10, 20
a, b = b, a
print("Tuple:", a, b)

# Swap using XOR
a, b = 10, 20
a = a ^ b
b = a ^ b
a = a ^ b
print("XOR:", a, b)

print("This program is written and executed by Mannan Tayal (0231BCA047).")
