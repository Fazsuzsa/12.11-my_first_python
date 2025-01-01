# Aufgabe 1
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 10:
    print("Die Zahl ist größer als 10.")
else:
    print("Die Zahl ist 10 oder kleiner.")

# Aufgabe 2
zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])

woche = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
print("Der 4. Tag ist:", woche[3])
print(woche)
woche.remove("So")
print(woche)
woche[3] = "Weihnachten"
woche[4] = "Weihnachten"
print(woche)

# Aufgabe 3
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")


# Aufgabe 4
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False


zahl = int(input("Gib eine Zahl ein: "))
if ist_gerade(zahl):
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")


# anders formuliert
def ist_gerade2(zahl):
    return zahl % 2 == 0


zahl = int(input("Gib eine Zahl ein: "))
if ist_gerade(zahl):
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")

# Aufgabe 5
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")
