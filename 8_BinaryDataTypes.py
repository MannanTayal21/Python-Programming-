# bytes: immutable binary data
binary_data = bytes([65, 66, 67])
print("bytes:", binary_data)

# bytearray: mutable binary data
mutable_data = bytearray([68, 69, 70])
print("bytearray:", mutable_data)

# memoryview: view over binary data without copying
view = memoryview(binary_data)
print("memoryview:", view)

print("this program was written and executed by Mannan Tayal (0231BCA047)")
