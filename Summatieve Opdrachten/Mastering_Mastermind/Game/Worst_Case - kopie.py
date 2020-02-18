import random
import itertools
import collections
import sys

from RandomCode import SecretCode
from RandomCode import RandomCode
from Database import Database

print("\nWelcome to Menno's MasterMind!")
print("\nPossible symbols are: + - x o * ?")

secret_code = SecretCode()
all_answers = Database()
all_scores = collections.defaultdict(dict)

Symbols = "+-xo*?"
s = Symbols
Answer = secret_code
Counted = collections.Counter(Answer)
Guesses = 1
Guess = []
def Guess():
    print("Attempt: " + str(Guesses))
    First_Guess = [s[0],s[0],s[1],s[1]]
    Guess = First_Guess
    Guess_Count = collections.Counter(Guess)
    Last_Guess = Guess
    White_Pin = sum(min(Counted[k], Guess_Count[k]) for k in Counted)
    Black_Pin = sum(a == b for a, b in zip(Answer, Guess))
    White_Pin -= Black_Pin
    print('\nYour last guess was: ')
    if Guesses == 2:
        print(First_Guess)
    else:
        print(*Last_Guess)
    print('Black pin: {}. \nWhite pin: {}\n'.format(Black_Pin, White_Pin))

    return Black_Pin != 4


while Guess():
    Guesses += 1
    if Guesses == 13:
        print("You Lost!")
        break
else:
    print("You win! It took you "+ str(Guesses) +" attempt(s) to crack the code!")
