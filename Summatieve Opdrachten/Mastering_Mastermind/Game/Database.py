import itertools
import random

def Database():
    Symbols = ["+","-","x","o","*","?"]
    all_answers = list(itertools.product(Symbols, repeat = 4))
    return all_answers
data = Database()

