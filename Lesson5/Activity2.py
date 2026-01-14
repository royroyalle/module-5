from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
       pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Dog(Animal):
    def move(self):
        print("I can bark")
class lion(Animal):
    def move(self):
        print("I can roar")
class snake(Animal):
    def move(self):
        print("I can crawl")

R = Human()
S = lion()
T = Dog()
U = snake()

R.move()
S.move()
T.move()
U.move()