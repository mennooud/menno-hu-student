
# a. Schrijf een functie count() die berekent hoe vaak een geheel getal x in een lijst voorkomt.
print("\nOpdracht 3.a")
getallenlijst = 1,2,3,4,5,6,7,7,7,8,8,3,3,5,65,7,8,9,90,0

def count(lijst):
    invoer = int(input("Voer geheel getal in: "))
    ratio = 0
    for i in lijst:
        if invoer == i:
            ratio += 1
    print("Getal "+ str(invoer) +" komt "+ str(ratio) + " keer voor")
count(getallenlijst)

# b. Schrijf een functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt.
print("\nOpdracht 3.b")
lijst2 = [45,65,4,4,3,4,5,6,4,5,7,4,5,6,257,6]

def GrootsteVerschil():
    print(max([y-x for x, y in zip(lijst2[:-1], lijst2[1:])]))

GrootsteVerschil()

# c.  Schrijf een functie, die bepaalt of een gegeven lijst met alleen 1’en en 0’en aan de volgende eisen voldoet:
print("\nOpdracht 3.c")
lijst3 = 1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0

def Voldoet():
    nullen = lijst3.count(0)
    enen = lijst3.count(1)
    if enen > nullen:
        print("Het aantal enen("+str(enen)+ ") is groter dan het aantal nullen("+str(nullen)+ ")")
        print(True)
        return True
    if enen < nullen:
        print("Het aantal enen("+str(enen)+ ") is kleiner dan het aantal nullen("+str(nullen)+ ")")
        print(False)
        return False
    if nullen > 12:
        print("Er zijn te veel nullen("+str(nullen)+ ")")
        print(False)
        return False
Voldoet()