# Aufgabe 3
zahl_1 = int(input("Gib eine Zahl ein: "))
zahl_2 = int(input("Gib eine größere Zahl ein: "))

liste = list(range(zahl_1, zahl_2 + 1))


def ungerade_zahlen():
    return [x for x in liste if x % 2 != 0]


def summe():
    return sum(ungerade_zahlen())


print(summe())
