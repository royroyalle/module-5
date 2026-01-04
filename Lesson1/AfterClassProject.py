class Pet:
    breed = "dog"
    def __init__(self, name, color):
        self.name = name
        self.color = color
Edd = Pet("Edd", "black")
Eddie = Pet("Eddie", "brown")
print("Pet 1 is",Edd.name, Edd.breed, Edd.color)
print("Pet 2 is",Eddie.name, Eddie.breed, Eddie.color)