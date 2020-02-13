import random

CodeSize = int(input("How many colors? (Max. 6)"))
CodeSize = CodeSize + 1

def Colors():
    x = random.randrange(1, CodeSize)
    for i in range(1):
        if x == 1:
            return ["+"]
        if x == 2:
            return ["-"]
        if x == 3:
            return ["x"]
        if x == 4:
            return ["o"]
        if x == 5:
            return ["*"]
        if x == 6:
            return ["?"]



def CorrectCode():
    while True:
        return Colors()+Colors()+Colors()+Colors()

print(CorrectCode())

def Guesses():

