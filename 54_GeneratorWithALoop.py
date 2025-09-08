def count_up_to(n):
    """Generator that yields numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

# Using the generator with a loop
for number in count_up_to(5):
    print(number)

print("This program is written and executed by Mannan Tayal (0231BCA047)")
