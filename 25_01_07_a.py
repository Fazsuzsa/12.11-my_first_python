# Hausaufgabe alternative Lösungen


# Aufgabe 1
def aufgabe_1():

    text_input = input("Gib einen Text ein: ").lower()
    letter_input = input("Gib eine Buchstabe ein: ").lower()

    counter = 0
    iterator = 0

    while iterator < len(text_input):
        if text_input[iterator] == letter_input:
            counter += 1
        iterator += 1

    print(f"Die Buchstabe '{letter_input}' befindet sich {counter}-mal im Text.")


# aufgabe_1()


# Aufgabe 2
def aufgabe_2():
    zahlen = []
    wievielmal = int(input("Wie viele Elemente sollen in die Liste? "))

    for _ in range(wievielmal):
        zahl = int(input("Gib eine Zahl ein: "))
        zahlen.append(zahl)

    summe = 0
    for i in zahlen:
        summe += i

    durchschnitt = summe / wievielmal
    # oder
    average = summe / len(zahlen)

    print(f"Die Summe der Zahlen ist {summe}.")
    print(f"Der Durchschnitt der Zahlen ist {durchschnitt}.")
    print(f"Der Durchschnitt ist also {average}.")

    # aufgabe_2()

    # NEUES THEMA:


class Buch:
    def __init__(self, titel, author):
        self.titel = titel
        self.author = author

    def text(self):
        print(f"Dieses Buch heißt {self.titel} und ist von {self.author} geschrieben.")


dracula = Buch("Count Dracula", "Bram Stoker")
print(dracula.titel)
print(dracula.author)

frankenstein = Buch("Frankenstein", "Mary Shelley")
print(frankenstein.titel)
frankenstein.titel = "Frankensteins Monster"
print(frankenstein.titel)

dracula.text()
frankenstein.text()


class Server:
    def __init__(self, name, ip, standort):
        self.name = name
        self.ip = ip
        self.standort = standort

    def boot(self):
        print(f"{self.name} wird mit {self.ip} hochgefahren.")

    def shutdown(self):
        print(f"{self.name} wird herunterfahren.")


my_server = Server("Server1", "192.168.0.1", "Frankfurt")
print(my_server.name)

my_server.programs = []
my_server.programs.append("google")
my_server.programs.append("goooogle")
print(my_server.programs)

my_server.boot()
my_server.shutdown()


class Auto:
    def __init__(self, name, motor, restweite, kilometer):
        self.name = name
        self.moter = motor
        self.restreichweite = restweite
        self.kilometerzahl = kilometer

    def fahren(self, km):
        if self.restreichweite >= km:
            self.kilometerzahl += km
            self.restreichweite -= km
            print(f"Das Auto fährt {km}.")
        else:
            print("Reichweite nicht mehr ausreichend.")

    def tanken(self, km):
        self.restreichweite += km


my_car = Auto("Peugeout 206", "Verbrenner", 200, 0)
my_car.fahren(30)
my_car.fahren(100)
my_car.fahren(100)

print(my_car.restreichweite)
my_car.tanken(600)
print(my_car.restreichweite)
print(f"Kilometerstand: {my_car.kilometerzahl}")

# Vererben


class Verbrenner(Auto):
    def __init__(self, name, kilometer):
        super().__init__(name, "Verbrenner", kilometer)
        self.tankstand = 100

    def tanken(self, km):
        self.tankstand += km


class E_Auto(Auto):
    def __init__(self, name, kilometer):
        super().__init__(name, "Elektro", kilometer)
        self.akkuladung = 100

    def tanken(self, km):
        self.akkuladung += km
