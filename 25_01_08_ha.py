class Haustier:
    def __init__(self, name, species, age, food, energy):
        self.name = name
        self.species = species
        self.age = age
        self.favourite_food = food
        self.energy_level = energy

    def get_description(self):
        print(f"{self.name} ist ein {self.age} Jahre alter {self.species}.")


mimi = Haustier("Mimi", "Katze", "3", "Fisch", "100")

mimi.get_description()
