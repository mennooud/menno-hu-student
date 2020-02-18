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
    hint = [0,0]
    Symbols = "+-xo*?"
    print("Attempt: " + str(Guesses))           #Dit is alweer niet het netste, maar zo kan je wel een verkeerde invoeren zonder crash. Try expect kan ook.
    In1 = '0'
    In2 = '0'
    In3 = '0'
    In4 = '0'
    while In1 not in Symbols:
        In1 = input("Enter the first symbol: ")
    while In2 not in Symbols:
        In2 = input("Enter the second symbol: ")
    while In3 not in Symbols:
        In3 = input("Enter the third symbol: ")
    while In4 not in Symbols:
        In4 = input("Enter the fourth symbol: ")
    Guess = [In1]+[In2]+[In3]+[In4]
    print(Guess)
    Guess_Count = collections.Counter(Guess)
    Last_Guess = Guess
    White_Pin = sum(min(Counted[k], Guess_Count[k]) for k in Counted) #Thanks
    Black_Pin = sum(a==b for a,b in zip(Answer, Guess))
    White_Pin -= Black_Pin
    #print(type(Black_Pin))             Zodat je type weet als je hiermee verder gaat
    hint[0] = Black_Pin                 #Hetgeen wat je navroeg voor als algoritme gokt
    hint[1] = White_Pin
    print(hint)

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