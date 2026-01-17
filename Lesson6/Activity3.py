import random
class Quiz:
    def __init__(self):
        self.fruits = {'apple':'red', 'orange': 'orange', 'banana': 'yellow', 'watermelon': 'green'}
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_answer = input()
            if(user_answer.lower() == color):
                print("Correct Answer")
            else:
                print("Wrong Answer")
            opt = int(input("Enter 0 if you wanna quit writing or enter 1 if you wanna enter more"))
            if(opt == 0):
                break
            elif opt == 1:
                continue
fq = Quiz()
fq.quiz()

