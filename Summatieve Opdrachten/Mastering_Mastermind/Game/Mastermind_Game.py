import random
import itertools
import collections
from RandomCode import SecretCode


print("\nWelcome to Menno's MasterMind!")
print("\nPossible symbols are: + - x o * ?")

Answer = SecretCode()


Counted = collections.Counter(Answer)
Guesses = 1

def Attempt():
    print("Attempt: " + str(Guesses))
    In1 = [input("Enter the first symbol: ")]
    In2 = [input("Enter the second symbol: ")]
    In3 = [input("Enter the third symbol: ")]
    In4 = [input("Enter the fourth symbol: ")]
    Guess = In1+In2+In3+In4
    Guess_Count = collections.Counter(Guess)
    Last_Guess = Guess
    White_Pin = sum(min(Counted[k], Guess_Count[k]) for k in Counted)
    Black_Pin = sum(a==b for a,b in zip(Answer, Guess))
    White_Pin -= Black_Pin
    print('\nYour last guess was: ')
    print(*Last_Guess)
    print('Black pin: {}. \nWhite pin: {}\n'.format(Black_Pin, White_Pin))
    return Black_Pin != 4

while Attempt():
    Guesses += 1
    if Guesses == 13:
        print("You Lost!")
        break
else:
    print("You win! It took you "+ str(Guesses) +" attempt(s) to crack the code!")
