# Input range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("\nPrime numbers:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

print("\n\nPerfect numbers:")
for num in range(start, end + 1):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num:
        print(num, end=" ")

print("\n\nArmstrong numbers:")
for num in range(start, end + 1):
    power = len(str(num))
    total = sum(int(d) ** power for d in str(num))
    if total == num:
        print(num, end=" ")

print("\n\nThis program is written and executed by Mannan Tayal (0231BCA047).")
