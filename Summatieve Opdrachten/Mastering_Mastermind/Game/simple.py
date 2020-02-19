import collections
import itertools
from RandomCode import main as RC
from PlayerGame import main as PG
from Database import data

print("\nWelcome to Menno's MasterMind!")
print("\nPossible symbols are: + - x o * ?")
Answer = RC.SecretCode()
Counted = collections.Counter(Answer)
Guesses = 1
gametype = "AI"

def game():
    print("Attempt: " + str(Guesses))
    if gametype == "AI":
        code = RC.RandomCode()
        data, code = Answer.items()
        while True:
            gok = data[0]
            fb = hint(code, Guess)
            for i in reversed(data):
                item_fb = hint(Guess, i)
                if fb != item_fb:
                    data.remove(i)
            print(Guess)
            hint = [0, 0]
            Guess_Count = collections.Counter(Guess)
            Last_Guess = Guess
            White_Pin = sum(min(Counted[k], Guess_Count[k]) for k in Counted)  # Thanks
            Black_Pin = sum(a == b for a, b in zip(Answer, Guess))
            White_Pin -= Black_Pin
            hint[0] = Black_Pin
            hint[1] = White_Pin
            print('\nYour last guess was: ')
            print(*Last_Guess)
            print('Black pin: {}. \nWhite pin: {}\n'.format(Black_Pin, White_Pin))
            return Black_Pin != 4

while game():
    Guesses += 1
