class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("This is the radius of the circle:", self.radius)
        print("The area is:", 3.14*self.radius**2)
    def perimeter(self):
        print("The perimeter is:",2 * 3.14*self.radius)
radi = Circle(int(input("Enter the circle's radius:")))
radi.area()
radi.perimeter()