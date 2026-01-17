class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+ self.meaning+')'
flash = []
print("Welcome to the flashcard application")
while(True):
    word = input("Enter the word")
    meaning = input("Enter the meaning")
    flash.append(flashcard(word, meaning))
    opt = int(input("Enter 0 if you wanna quit writing or enter 1 if you wanna enter more"))
    if(opt == 0):
        break
    elif opt == 1:
         continue
print("The flashcards you have entered are:")
for i in flash:
    print(">", i)