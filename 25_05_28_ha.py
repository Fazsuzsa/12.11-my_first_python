# Debug 1
zahl = "10"
zahl_int = int(zahl)  # int() wandelt einen String in eine Ganzzahl um
ergebnis = zahl_int + 5
print(ergebnis)

# Debug 2
x = 3
if x > 0:
    print("x ist positiv")  # Einrückung fehlt

# Debug 3
for i in range(5):  # Doppelpunkt fehlt
    print(i)  # Einrückung fehlt

# Debug 4
alter = 18
if alter == 18:  # == statt = weil boolescher Vergleich
    print("Volljährig")  # Einrückung fehlt

# Debug 5
x = 4  # 100
y = 2  # 010
z = x ^ y  # bitweise XOR, z = 110 in binär
print("Ergebnis ist", z)

# Debug 6
x = 10
if x > 0:
    if x < 5:  # Einrückung fehlt, weil verschachtelt
        print("klein")  # Einrückung fehlt
    else:  # Einrückung fehlt
        print("groß")  # Einrückung fehlt


# Debug 7
counter = 0  # gegen die Endlosschleife
while True:
    print("Hallo")  # Einrückung fehlt
    counter += 1
    if counter == 2:
        break

# Debug 8
eingabe = input("Gib eine Zahl ein: ")
eingabe_int = int(eingabe)  # int() wandelt einen String in eine Ganzzahl um
if eingabe_int > 10:
    print("größer als 10")  # Einrückung fehlt
