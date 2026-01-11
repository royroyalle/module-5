n = 50
e = n/100 
class Vehicle:
    def __init__(self, name, capcacity, fare):
        self.name = name
        self.capacity = capcacity
        self.fare = n*100
class bus(Vehicle):
    pass
Schoolbus = bus("School Bus", 50, n)
print("Bus class-", Schoolbus.name)
print("Bus capacity-", Schoolbus.capacity)
print("Bus fare-", Schoolbus.fare)