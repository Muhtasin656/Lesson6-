class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+self.meaning
flash=[]
print("welcome to the flashcard application")
while True:
    word=input("enter a the the name you want to add to the flashcards")
    meaning=input("enter the meaning of the word")
    flash.append(flashcards(word,meaning))
    option=int(input("enter 0 if you want to add another flashcard otherwie enter 1"))
    if (option):
        break
print("your flassgcards are")
for i in flash:
    print(i)