a, b, c = 1, 2, 3

# 1. Using temp variables
x, y, z = a, b, c
t1 = x; t2 = y
x = z; y = t1; z = t2
print("Temp:", x, y, z)

# 2. Using tuple unpacking
x, y, z = a, b, c
x, y, z = z, x, y
print("Tuple:", x, y, z)

print("This program is written and executed by Mannan Tayal (0231BCA047).")
