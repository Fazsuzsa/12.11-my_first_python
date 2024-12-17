# human error
def addiere_zahlen():
    zahl1 = input("Gib die erste Zahl ein: ")
    zahl2 = input("Gib die zweite Zahl ein: ")

    # überprüfen, ob zahl1 und zahl2 Ziffer sind
    if zahl1.isdigit() and zahl2.isdigit():
        return int(zahl1) + int(zahl2)
    else:
        return "Keine gültige Zahlen!"


print(addiere_zahlen())
