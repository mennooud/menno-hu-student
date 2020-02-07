'''
def RandNum(a, b):
    return a + RandomUnder(b - a + 1)

def RandUnder(n):
    if n <= 0:
        raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r

def random_bytes(n):
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)

print(RandNum(1, 1000)
'''
import random


Antwoord = random.randrange(1, int(input("Random nummer tussen 0 en: ")))

for i in range(int(Pogingen)):
    print("Doe een gok!")
    gok = input()
    gok = int(gok)

    if Antwoord == gok:
        print("Gefeliciteerd u heeft het juiste getal geraden!")
        break
    while Antwoord != gok:
        print("Helaas! Probeer opnieuw.")
        break




