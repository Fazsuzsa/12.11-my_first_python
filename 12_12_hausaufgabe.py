# 1. Namensabfrage mit Input

vorname = input("Was ist dein Vorname? ")
nachname = input("Was ist dein Nachname? ")

print(f"Der Typ von Vorname ist: {type(vorname)}")
print(f"Der Typ von Nachname ist: {type(nachname)}")

addition_vorname_nachname = vorname + " " + nachname
print (f"Dein Name ist {addition_vorname_nachname}")

# 2. Addition von Zahlen

zahl_1 = input("Gib eine Zahl ein: ")
zahl_1_int = int(zahl_1)
zahl_2 = input("Gib noch eine Zahl ein: ")
zahl_2_int = int(zahl_2)

addition_zahl_1_zahl_2 = zahl_1_int + zahl_2_int

print (f"Die Summe von den Zahlen ist: {addition_zahl_1_zahl_2}")