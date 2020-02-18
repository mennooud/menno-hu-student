import random
import itertools
import collections
import sys


def Database():
    Symbols = "+-xo*?"
    all_answers = set(itertools.permutations(Symbols, 4))
    return all_answers

data = Database()
print(data)
print(len(data))

def VoorbeeldVanDatabase():
    tekendictonairy = {'1' :'+', '2' : '-', '3' : "x", '4' :  "o", '5' : "*", '6' : "?"}
    all_answers = []
    for i in range(1111, 6667):
        answer = str(i)
        if '7' in answer or '8' in answer or '9' in answer or '0' in answer:
            continue
        else:
            a = ((tekendictonairy[answer[0]]))      #Dit is niet heel clean door mij gemaakt, maar errors zorgde hiervoor
            b = ((tekendictonairy[answer[1]]))
            c = ((tekendictonairy[answer[2]]))
            d = ((tekendictonairy[answer[3]]))
            all_answers.append(a+b+c+d)
    print(all_answers)
    print(len(all_answers))
    return all_answers

VoorbeeldVanDatabase()