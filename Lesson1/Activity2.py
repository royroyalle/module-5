class car:
    def __init__(self, maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage
model = car(240, 180)
print("Model Max speed = ",model.maxspeed)
print("Model Max mileage = ", model.mileage)