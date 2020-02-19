import itertools
import random
import collections
import sys

def Database():
    Symbols = ["+","-","x","o","*","?"]
    all_answers = list(itertools.product(Symbols, repeat = 4))
    return all_answers
data = Database()

print(data)
print(random.choice(data))