class Vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self. maxspeed = maxspeed
        self.mileage = mileage
class bus(Vehicle):
    pass
SchoolBus = bus("Volvo", 180, 12)
print("Vehicle name:", SchoolBus.name)
print("Vehicle max speed:", SchoolBus.maxspeed) 
print("Vehicle mileage:", SchoolBus.mileage)