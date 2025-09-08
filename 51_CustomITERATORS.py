print("Program to Create and Use a Custom Iterator:\n")
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = Reverse('giraffe')
for char in rev:
    print(char)  # Outputs: e, f, f, a, r, i, g

print("\nThis program is written and executed by Mannan Tayal (0231BCA047)")
