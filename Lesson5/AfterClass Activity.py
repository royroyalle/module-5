class BMW:
    def speed(self):
        print("BMW'S Average speed is 150 km/h")
    def mileage(self):
        print("It's average mileage is 120")
class Ferrari:
    def speed(self):
        print("Ferrari's Average speed is 200 km/h")
    def mileage(self):
        print("It's average mileage is 130")
m4 = BMW()
f90 = Ferrari()
for car in (m4, f90):
    car.speed()
    car.mileage()