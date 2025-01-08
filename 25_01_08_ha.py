class Haustier:
    def __init__(self, name, species, age, food, energy):
        self.name = name
        self.species = species
        self.age = age
        self.favourite_food = food
        self.energy_level = energy

    def get_description(self):
        print(f"{self.name} ist ein {self.age} Jahre alter {self.species}.")

    def play(self, duration):
        self.energy_level = self.energy_level - duration * 5
        if self.energy_level >= 0:
            print(
                f"{self.name} hat {duration} Minuten gespielt, der neue Energielevel ist {self.energy_level}."
            )
        else:
            print(
                f"{self.name} konnte nur {self.energy_level/5} Minuten spielen, der neue Energielevel ist 0."
            )


mimi = Haustier("Mimi", "Katze", "3", "Fisch", 100)


mimi.get_description()
mimi.play(50)
