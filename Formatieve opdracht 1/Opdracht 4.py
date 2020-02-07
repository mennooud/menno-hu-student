'''
Schrijf een functie die checkt of een woord een palindroom is.
Schrijf een versie die gebruikt maakt van een bibliotheekfunctie die een string voor je omdraait.
Maak ook een versie waarbij jij zelf het omdraaien verzorgt.
Probeer zo min mogelijk code te gebruiken.
'''

woord = input("Geef een woord: ")

# a. Schrijf een functie count() die berekent hoe vaak een geheel getal x in een lijst voorkomt.
print("\nOpdracht 4.a")

def Palindroom1():
    droow =[]
    lengte = len(woord)
    while lengte > 0:
        droow += woord[lengte - 1]
        lengte = lengte - 1
    droow=''.join(droow)
    print("Het gegeven woord omgedraaid is: "+droow)
    if droow == woord:
        print("Het gegeven woord is een palindroom.")
    if droow != woord:
        print("Het gegeven woord is geen palindroom")
    return
Palindroom1()
# b.
print("\nOpdracht 4.b")

def Palindroom2():
    woord = input("Geef een woord: ")
    if woord == woord[::-1]:
        print("Het woord: "+woord+ " is een palindroom")
    else:
        print("Het woord: "+woord+" is geen palindroom")
Palindroom2()