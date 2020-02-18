import random
import itertools
import collections

def RandomCode():
    answer = tuple(random.choice("+-xo*?") for _ in range(4))
    return answer

def SecretCode():
    answer = tuple(random.choice("+-xo*?") for _ in range(4))
    see_code = input("\nDo you wish to see the secret code? (Y/N)")
    if see_code.upper() == "Y" or see_code.upper() == "YES":
        print("\nThe correct code is: ")
        print(*answer)
    elif see_code.upper() == "N" or see_code.upper() == "NO":
        print("\nThe code is hidden.")
    return answer

