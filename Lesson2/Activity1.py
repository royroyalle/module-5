class IOstring():
    def __init__(self):
        self.str1 = ""
    def getstring(self):
        self.str1 = input("Kindly enter your string")
    def printstring(self):
        print("The upper case string is-", self.str1.upper())

str1 = IOstring()
str1.getstring()
str1.printstring()