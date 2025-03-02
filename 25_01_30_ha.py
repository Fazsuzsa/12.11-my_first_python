# FALSCH:

# def begruessung name:
# print("Hallo, " + Name)

# def addiere_zahlen(a, b)
#     ergebnis = a + b
#     return ergebis

# def subtrahiere_zahlen(a, b):
#     return a - c

# def main()
#     zahl1 = input("Gib eine Zahl ein: ")
#     zahl2 = input("Gib eine weitere Zahl ein: ")

#     summe = addiere_zahlen(zahl1, zahl2)
#     print("Die Summe ist: " + summe)

#     differenz = subtrahiere_zahlen(zahl1, zahl2)
#     print("Die Differenz ist: " + differenz)

#     begruessung("Max")

# if __name__ = "__main__":
#     main()

# RICHTIG mit Beschreibung der Verbesserungen:


def begruessung(name):  # Klammern
    print("Hallo, " + name)  # Einrückung, "n" klein


def addiere_zahlen(a, b):  # Doppelpunkt
    ergebnis = a + b
    return ergebnis  # "n" hat gefehlt


def subtrahiere_zahlen(a, b):
    return a - b  # "b" statt "c"


def main():  # Doppelpunkt
    zahl1 = int(input("Gib eine Zahl ein: "))  # "int"
    zahl2 = int(input("Gib eine weitere Zahl ein: "))  # "int"

    summe = addiere_zahlen(zahl1, zahl2)
    print("Die Summe ist:", summe)  # komma statt plus

    differenz = subtrahiere_zahlen(zahl1, zahl2)
    print("Die Differenz ist:", differenz)  # komma statt plus

    begruessung("Max")


if __name__ == "__main__":  # "==" statt "="
    main()
