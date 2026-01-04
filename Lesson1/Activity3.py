class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blue = Parrot("Blu", 10)
red = Parrot("Re", 12)
print("Parrot 1 is a {}".format(blue.species))
print("Parrot 2 is a {}".format(red.species))
print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(red.name, red.age))