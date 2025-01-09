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


milch = Zutat("Milch", 50, 5)
eier = Zutat("Eier", 150, 0)
mehl = Zutat("Mehl", 300, 10)
zucker = Zutat("Zucker", 400, 5)

pfannkuchen = Rezept("Pfannkuchen", "Super leckere und fluffugen Pfannkuchen!")
pfannkuchen.zutat_hinzufuegen(milch, "250 ml")
pfannkuchen.zutat_hinzufuegen(eier, "2 Stück")
pfannkuchen.zutat_hinzufuegen(mehl, "150 g")
pfannkuchen.zutat_hinzufuegen(zucker, "50 g")

pfannkuchen.rezept_anzeigen()
pfannkuchen.kalorien()
pfannkuchen.kochzeit()
