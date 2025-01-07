# Aufgabe 1

text_input = input("Gib einen Text ein: ").lower()
letter_input = input("Gib eine Buchstabe ein: ").lower()

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

x = int(input("Wieviel Reihe möchtest du? "))

for i in range(x):
    for _ in range(i + 1):
        print("*", end="")
    print("")
