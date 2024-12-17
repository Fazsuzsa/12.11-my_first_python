def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


zahl_1 = int(input("Gib eine Zahl ein: "))
zahl_2 = int(input("Gib noch eine Zahl ein "))


def calculator():
    operation = input(
        "Addieren, subtrahieren, multiplizieren oder dividieren? Gib +, -, * oder / ein! "
    )

    if operation == "+":
        print(f"{zahl_1} + {zahl_2} = {add(zahl_1, zahl_2)}")
    elif operation == "-":
        print(f"{zahl_1} - {zahl_2} = {subtract(zahl_1, zahl_2)}")
    elif operation == "*":
        print(f"{zahl_1} * {zahl_2} = {mult(zahl_1, zahl_2)}")
    elif operation == "/":
        print(f"{zahl_1} / {zahl_2} = {div(zahl_1, zahl_2)}")
    else:
        print("Ungültige Operation! Gib +, -, * oder / ein! ")
        calculator()


calculator()
