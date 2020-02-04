def stringdifference():
    x = 0
    y = 0
    string1 = input("geef een string: ")
    string2 = input("Geef nog een string: ")

    while x != len(string1) and y != len(string2):
        if string1[x] == string2[y]:
            x += 1
            y += 1
        else:
            break
    print("Het eerste verschil zit op index: " + str(y))
stringdifference()
