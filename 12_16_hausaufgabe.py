x = int(input("Gib eine Zahl ein: "))
y = int(input("Gib noch eine Zahl ein "))


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {mult(x, y)}")
print(f"{x} / {y} = {div(x, y)}")

def calculator():

