import random
import itertools
import collections
import sys


def Database():
    Symbols = "+-xo*?"
    all_answers = set(itertools.permutations("+-xo*?", 4))
Data = Database()

