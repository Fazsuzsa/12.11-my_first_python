# Aufgabe 1
class Zutat:
    def __init__(self, name, kalorien, zeit):
        self.name = name
        self.kalorien_pro_100g = kalorien
        self.zubereitungszeit = zeit


class Rezept:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung
        self.zutatenliste = {}  # dictionary

    def zutat_hinzufuegen(self, zutat, menge):
        self.zutatenliste[zutat] = menge

    def kalorien(self):
        kalorien_counter = 0
        for zutat in self.zutatenliste:
            kalorien_counter += zutat.kalorien_pro_100g
        print(f"Die Gesamtkalorien sind: {kalorien_counter} kcal.")

    def kochzeit(self):
        kochzeit = 0
        for zutat in self.zutatenliste:
            if zutat.zubereitungszeit > kochzeit:
                kochzeit = zutat.zubereitungszeit
        print(f"Die Kochzeit beträgt {kochzeit} Minuten.")

    def rezept_anzeigen(self):
        print(f"Rezept: {self.name}")
        print("Zutaten: ")
        for zutat, menge in self.zutatenliste.items():
            print(f"- {zutat.name}: {menge}")
        print(f"Beschreibung des Rezepts: {self.beschreibung}")
