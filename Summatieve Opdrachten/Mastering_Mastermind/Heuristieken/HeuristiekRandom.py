import MasterMind_Database
import random
import collections

print("Welcome to Menno's MasterMind!")

CodeSize = int(input("How many different symbols? (Max. 6)"))
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
        return tuple(Colors()+Colors()+Colors()+Colors())
cc = CorrectCode()

if input("Do you wish to see the secret code?") == "Yes" or "yes" or 1 or True:
    print(cc)


Counted = collections.Counter(cc)

def Input():
    randomanswer = tuple(random.choice("+-xo*?") for _ in range(4))
    print(randomanswer)
    return randomanswer

Guesses = 1
def Attempt():
    print("Attempt: " + str(Guesses))
    Guess = Input()
    Guess_Count = collections.Counter(Guess)
    White_Pin = sum(min(Counted[k], Guess_Count[k]) for k in Counted)
    Black_Pin = sum(a==b for a,b in zip(cc, Guess))
    White_Pin -= Black_Pin
    print('Black pin: {}. \nWhite pin: {}\n'.format(Black_Pin, White_Pin))
    return Black_Pin != 4


while Attempt():
    Guesses += 1
    pass

print("You win! It took you "+ str(Guesses) +" attempt(s) to crack the code!")

