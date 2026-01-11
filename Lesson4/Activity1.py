class Myclass:
    __privar = 27;
    def __privMeth(self):
        print("Im inside a class called Myclass")
    def hello(self):
        print("Private Variable Value:", Myclass.__privar)
foo = Myclass()
foo.hello()
foo.__privMeth