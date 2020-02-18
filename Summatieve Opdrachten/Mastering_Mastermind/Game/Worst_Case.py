import random
import itertools
import collections
import sys

from RandomCode import SecretCode
from RandomCode import RandomCode
from Database import Database


class MasterMind:
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

    def __init__(self, guess, answer):
        self.all_answers
        self.all_scores
        self.Guesses
        for guess, answer in itertools.product(self.all_answers, repeat= 2):
            self.all_scores[guess][answer] = self.Attempt(guess, answer)

    def firstGuess(self):
        print("Attempt: " + str(self.Guesses))
        First_Guess = [s[0],s[0],s[1],s[1]]
        Guess = First_Guess
        Guess_Count = collections.Counter(Guess)
        Last_Guess = Guess
        White_Pin = sum(min(Counted[k], Guess_Count[k]) for k in Counted)
        self.White_Pin = White_Pin
        Black_Pin = sum(a == b for a, b in zip(Answer, Guess))
        self.White_Pin -= Black_Pin
        print('\nYour last guess was: ')
        if self.Guesses == 2:
            print(First_Guess)
        else:
            print(*Last_Guess)
        print('Black pin: {}. \nWhite pin: {}\n'.format(Black_Pin, White_Pin))
        return Black_Pin != 4

        while firstGuess(self.Black_Pin):
            self.Guesses += 1
            break

    def Attempt(self, guess, answer):
        wrong_guess_pins = []
        wrong_answer_pins = []
        self.Black_pin = []
        self.White_Pin = []

        for guess_pin, answer_pin in zip(guess, answer):
            if guess_pin == answer_pin:
                self.Black_Pin + 1
            else:
                wrong_guess_pins.append(guess_pin)
                wrong_answer_pins.append(answer_pin)

        for peg in wrong_guess_pins:
            if peg in wrong_answer_pins:
                wrong_answer_pins.remove(peg)
                self.White_Pin + 1

        return print('Black pin: {}. \nWhite pin: {}\n'.format(self.Black_Pin, self.White_Pin))

        print("Attempt: " + str(self.Guesses))
        Guess = []
        Guess_Count = collections.Counter(Guess)
        Last_Guess = Guess
        White_Pin = sum(min(Counted[k], Guess_Count[k]) for k in Counted)
        Black_Pin = sum(a==b for a,b in zip(Answer, Guess))
        White_Pin -= Black_Pin
        print('\nYour last guess was: ')
        print(*Last_Guess)
        print('Black pin: {}. \nWhite pin: {}\n'.format(Black_Pin, White_Pin))
        return Black_Pin != 4


        while Attempt(self.Black_Pin != 4):
            Guesses += 1
            if Guesses == 13:
                print("You Lost!")
                break
        else:
            print("You win! It took you "+ str(Guesses) +" attempt(s) to crack the code!")
