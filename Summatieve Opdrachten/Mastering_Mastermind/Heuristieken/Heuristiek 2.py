import itertools


Symbols = "+-xo*?"
all_answers = set(itertools.product(Symbols, repeat = 4))
print(all_answers)