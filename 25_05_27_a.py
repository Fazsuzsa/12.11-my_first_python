# variable:
first_name = "Zsuzsa"  # PEP8: snake_case
last_name = "Farkas"  # string
money = 1_000_0000  # int, besser lesbar, für große Zahlen
age = 32  # int
weight = 59.5  # float
has_a_mustache = False  # bool

print(first_name, last_name)

print(1 + 1 + 1 == 3)  # True
print(0.1 + 0.1 + 0.1 == 0.3)  # False, weil die Werte nicht exakt gleich sind
print(0.1 + 0.1 + 0.1)  # 0.30000000000000004
print(round(0.1 + 0.1 + 0.1, 4) == 0.3)  # True
print(round(0.1 + 0.1 + 0.1, 4))  # 0.3000

a = 5
b = 7

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# modulo
print(a % b)

# exponent (a hoch b)
print(a**b)

# wurzel (a hoch 0.5)
print(a**0.5)

# floor division (rundet runter die float in eine integer)
print(a // b)

# String-Konkatenation
print("hallo " + first_name)
print(3 * "hallo ")

zahl1 = 17
zahl1 += 1
zahl2 = 17
zahl2 -= 2

print(zahl1)  # 18
print(zahl2)  # 15

# compiler: übersetzt den gesamten Code erst in Maschinensprache,
# - die Ausfühtung des kompilierten Programmes ist in der Regel schneller
# - bei umfangreichen Projekten, damit der gesamte Code in eine schnelle ausführbare Form übersetzt wird und Fehler früh erkannt werden
# interpreter: führt den Code Zeile für Zeile direkt aus

# python: wird hauptsächlich interpretiert, nutzt intern aber auch einen Bytecode-Zwischenschritt (Compiler)


print(f"hallo {first_name}")
