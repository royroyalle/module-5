class Bird:
    def __init__(self):
        print("Bird is ready")
    def swim(self):
        print("Swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("Run Faster")
peggy = Penguin()
peggy.whoisthis()
peggy.run()
peggy.swim()