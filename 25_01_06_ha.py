# Aufgabe 1

text_input = input("Gib einen Text ein: ")
letter_input = input("Gib eine Buchstabe ein: ")

counter = 0
for x in text_input:
    if x == letter_input:
        counter = counter + 1

print(f"Die Buchstabe {letter_input} befindet sich {counter}-mal im Text.")

# Aufgabe 2

zahlen = []
summe = 0

for _ in range(5):
    user_input = int(input("Gib eine Zahl ein: "))
    zahlen.append(user_input)
    summe = summe + user_input

durchschnitt = summe / 5

print(f"Die Summe der Zahlen ist {summe}.")
print(f"Der Durchschnitt der Zahlen ist {durchschnitt}.")

# Aufgabe 3

zeilen = int(input("Wieviel Zeilen möchtest du haben? "))

for _ in range(zeilen):
    print("*")
