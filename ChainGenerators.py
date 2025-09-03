def gen1():
    yield from [1, 2, 3]

def gen2():
    yield from ['a', 'b', 'c']

def chained_generators():
    yield from gen1()
    yield from gen2()

# Using the chained generator
for item in chained_generators():
    print(item)

print("This program is written and executed by Mannan Tayal (0231BCA047)")
