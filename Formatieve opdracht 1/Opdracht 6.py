#a
print("\nOpdracht 6.a")
lijst = [12,345,45,7,9,45,67,87,45,34]

def Gemiddelde(x):
    aantal = len(x)
    som = sum(x)
    print(abs(som/aantal))
Gemiddelde(lijst)

#b
print("\nOpdracht 6.b")
lijst1 = [12,345,45,7,9,45,67,87,45,34]
lijst2 = [43,654,7,45,2,34,5,]
lijst3 = [12,654,5,8,3,8,]

lijsten = [lijst1,lijst2,lijst3]
def Gemiddelde(x):
    combinatie = x[0] + x[1] + x[2]
    aantal = len(combinatie)
    som = sum(combinatie)
#    print(aantal)
#    print(som)
    print(+abs(som/aantal))

Gemiddelde(lijsten)


