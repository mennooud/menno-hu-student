import random
import itertools
import collections
import sys

from RandomCode import SecretCode
from RandomCode import RandomCode
from Database import Database

print("\nWelcome to Menno's MasterMind!")
print("\nPossible symbols are: + - x o * ?")
number_attempts = int(input("How many attempts to crack the code: ")+ 1)
secret_code = SecretCode()
all_answers = Database()


Answer = secret_code
Counted = collections.Counter(Answer)
Guesses = 1

def RandomGuess():
    print("Attempt: " + str(Guesses))
    First_Guess = RandomCode()
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

while RandomGuess():
    Guesses += 1
    if Guesses == 13:
        print("You Lost!")
        break
else:
    print("You win! It took you "+ str(Guesses) +" attempt(s) to crack the code!")
