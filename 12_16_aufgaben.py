# Funktionen in Python
def square(zahl):
    return zahl * zahl


user_input = float(input("Gib mir eine Zahl: "))
result = square(user_input)
print(result)


# Funktionen ohne Argumente:
def write_something():
    print("Dieser Text kommt aus einer Funktion!")


write_something()
write_something()
write_something()


# Funktion, die User nach Alter fragt und auf Konsole ausgibt
def altersafbrage():
    alter = int(input("wie alt bist du? "))
    print(f"Du bist also {alter} Jahre alt.")


altersafbrage()
altersafbrage()


# Funktion, die User nach Namen fragt und auf Konsole ausgibt
def namensafbrage():
    name = input("wie heißt du? ")
    print(f"Du heißt also {name}.")


namensafbrage()


# ... mit return
def namensabfrage_2():
    name = input("wie heißt du? ")
    return f"Du heißt also {name}."


print(namensabfrage_2())


# Mehrere Argumente:
def add(zahl1, zahl2):
    return zahl1 + zahl2


print(add(5, 7))
