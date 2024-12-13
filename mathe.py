a = 1
b = 2

print("Addition", a + b)
print("Subtraktion", a - b)
print("Multiplikation", a * b)
print("Division", a / b)

note1 = 3
note2 = 4
note3 = 1

print("Durchschnitt", (note1 + note2 + note3) / 3)

# andere Lösung

result = (note1 + note2 + note3) / 3

print (f"Die Durchschnittsnote ist: {result}")

# elegante Lösung

note_11 = input("Gib Zahl1 ein: ")
note_11_int = int(note_11)
print(f"Der Typ von Zahl1 ist: {type(note_11)}")
print(f"Der Typ von Zahl1 ist: {type(note_11_int)}")

note_12 = input("Gib Zahl2 ein: ")
note_12_int = int(note_12)
print(f"Der Typ von Zahl2 ist: {type(note_12)}")
print(f"Der Typ von Zahl2 ist: {type(note_12_int)}")

addition_zahl1_zahl2 = note_11_int + note_12_int

print (f"Die Summe von Zahl1 und Zahl2 ist: {addition_zahl1_zahl2}")