# Aufgabe 3

zahl_1 = int(input("Gib eine Zahl ein: "))
zahl_2 = int(input("Gib eine größere Zahl ein: "))

liste = list(range(zahl_1, zahl_2 + 1))
# print(liste)


def ungerade_zahlen():
    return [a for a in liste if a % 2 != 0]


# print(ungerade_zahlen())


def summe():
    return sum(ungerade_zahlen())


print(summe())


# andere Lösung (Nassima)

x = int(input("x = "))
y = int(input("y = "))

y = y + 1
i = range(x, y)

sum = 0
z = 0
for n in i:
    if n % 2 != 0:
        sum = sum + n
        z = z + 1

print(sum)
