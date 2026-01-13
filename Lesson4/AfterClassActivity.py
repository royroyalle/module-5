string = input("Enter String:")
class String:
    def __init__(self, string):
        self.string_value = string
    def reverse(self):
        print(string[::-1])
obj = String(string)
print("Reversed Text:")
obj.reverse()