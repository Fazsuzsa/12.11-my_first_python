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
