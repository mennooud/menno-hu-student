import random
import itertools
import collections
from RandomCode import main as RC
from PlayerGame import main as PG

print("\nWelcome to Menno's MasterMind!")
print("\nPossible symbols are: + - x o * ?")

gametype = str(input("Want to play yourself or let the computer crack the code? (User/AI)")).upper()

Answer = RC.SecretCode()
Counted = collections.Counter(Answer)
Guesses = 1

def game():
    print("Attempt: " + str(Guesses))
    if gametype == "USER":
        Guess = PG.Player()
    elif gametype == "RANDOM":
        Guess = RC.RandomCode()
    elif gametype == "AI":
        Guess = ["+","+","-","-"]
    Guess = Guess
    hint = [0,0]
    Guess_Count = collections.Counter(Guess)
    Last_Guess = Guess
    White_Pin = sum(min(Counted[k], Guess_Count[k]) for k in Counted) #Thanks
    Black_Pin = sum(a==b for a,b in zip(Answer, Guess))
    White_Pin -= Black_Pin
    hint[0] = Black_Pin
    hint[1] = White_Pin
    print('\nYour last guess was: ')
    print(*Last_Guess)
    print('Black pin: {}. \nWhite pin: {}\n'.format(Black_Pin, White_Pin))
    return Black_Pin != 4

while game():
    Guesses += 1
    if Guesses == 13:
        print("You Lost!")
        break
else:
    print("You win! It took you "+ str(Guesses) +" attempt(s) to crack the code!")
