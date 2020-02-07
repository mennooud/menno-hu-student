""""
Opdracht 1 - PyramidePyramide.png
Schrijf een programma dat een piramide van variabele lengte afdrukt, zoals in het voorbeeld. 
Druk ieder character apart af. De gebruiker geeft aan hoe groot de piramide
is. Implementeer je programma twee keer, de eerste keer met twee for loops, en daarna met twee while loops. Maak ook versies die de pyramide een andere kant op laten wijzen.
""""

x = int(input("Hoe groot: "))

for i in range(x):
    print("*"*(i+1))
for i in range(x):
    print("*"*(x-i-1))

i = i
while i != int(input())